import requests
import time
from notifypy import Notify


# For local streaming, the websockets are hosted without ssl - http://
HOST = 'localhost:5000'
URI = f'http://{HOST}/api/v1/generate'

# For reverse-proxied streaming, the remote will likely host with ssl - https://
# URI = 'https://your-uri-here.trycloudflare.com/api/v1/generate'

def model_api(request):
    response = requests.post(f'http://{HOST}/api/v1/model', json=request)
    return response.json()

def model_load(model_name):
    return model_api({'action': 'load', 'model_name': model_name})

def run(prompt):
    request = {
        'prompt': prompt,
        'max_new_tokens': 400,
        'auto_max_new_tokens': False,
        'max_tokens_second': 0,

        # Generation params. If 'preset' is set to different than 'None', the values
        # in presets/preset-name.yaml are used instead of the individual numbers.
        'preset': 'None',
        'do_sample': True,
        'temperature': 0.01  ,      #0.01 FOR STORY ACTIONS | 0.7 is average i think
        'top_p': 0.1,
        'typical_p': 1,
        'epsilon_cutoff': 0,  # In units of 1e-4
        'eta_cutoff': 0,  # In units of 1e-4
        'tfs': 1,
        'top_a': 0,
        'repetition_penalty': 1.18,
        'repetition_penalty_range': 0,
        'top_k': 40,
        'min_length': 0,
        'no_repeat_ngram_size': 0,
        'num_beams': 1,
        'penalty_alpha': 0,
        'length_penalty': 1,
        'early_stopping': False,
        'mirostat_mode': 0,
        'mirostat_tau': 5,
        'mirostat_eta': 0.1,
        'grammar_string': '',
        'guidance_scale': 1,
        'negative_prompt': '',

        'seed': -1,
        'add_bos_token': True,
        'truncation_length': 2048,
        'ban_eos_token': False,
        'custom_token_bans': '',
        'skip_special_tokens': True,
        'stopping_strings': ['*----*'] #IMPORTANT FOR STORY ACTIONS
    }

    response = requests.post(URI, json=request)

    if response.status_code == 200:
        result = response.json()['results'][0]['text']
        return (prompt + result)
    else:
        print (response.status_code)

model = "TheBloke_vicuna-13B-1.1-GPTQ"

def main():

    notification = Notify()
    notification.title = "PROMPT FINISHED"
    notification.message = "Please come back to make the LLM continue"
    print("?- CHOOSE A SET OF PROMPTS")
    pl = open("prompt_list.txt", "r")
    prompt_list = pl.readlines()
    counter = 0
    for p in prompt_list:
        print(str(counter) + '- ' + p, end='')
        counter = counter + 1
    n_prompt = int(input('\n?- '))
    prompt_d = prompt_list[n_prompt]
    prompt_dir = "prompts\\" + prompt_d.strip() + "\\"

    print("?- CHOOSE A MODEL")
    ml = open("model_list.txt", "r")
    mod_list = ml.readlines()
    counter = 0
    for m in mod_list:
        print(str(counter) + '- ' + m, end='')
        counter = counter + 1
    n_mod = int(input('\n?- '))
    mod = mod_list[n_mod]
    if mod[-1] == '\n':
        mod = mod[:-1]

    resp = ""
    if "Skip" not in mod:
        print("!- LOADING MODEL " + mod)
        resp = model_load(mod)
        #resp = "skip"
        print("!- MODEL LOADED")
    if 'error' in resp:
        print(f"❌ FAIL Error: {resp['error']['message']}")
    else:
        f = open(prompt_dir+"prompts.txt", "r")
        content = []
        old_prompts = ""
        
        while True:
            prompt = ""
            content = content + f.readlines()
            #print(content)
            for i,x in enumerate(content):
                if (x[0:5] == "-----"):
                    prompt = prompt [:-1]
                    promptn, prompt = prompt.split("\n",1)
                    content = content[(i+1):]
                    break
                elif (x[0:3] == "###"):
                    old_prompts = old_prompts + x
                elif (x[0:3] != "###"):
                    prompt += x
            if prompt != "":
                print ("!- NOW TRYING " + promptn)
                r = open(prompt_dir + 'results\\'+ promptn +'.txt', 'w+')
                r.write("MODEL: " + model + "\n")
                r.write(promptn + "\n")
                r.write(run(prompt) + "\n")
                r.write("-----------------------------------------------------------\n")
                r.close()
                old_prompts = old_prompts + promptn + '\n' + prompt + '\n-----\n'
                print ("!- FINISHED " + promptn)
                notification.send()
                #answ =(input("?- START NEXT PROMPT? (y/n)")).lower()
                answ = 'y'
                if answ == 'n':
                    f.close()
                    f = open(prompt_dir + "prompts.txt", "w")
                    f.write("\n".join(content))
                    f.close()
                    of = open(prompt_dir + "old_prompts.txt", "a")
                    of.write(old_prompts)
                    of.close()
                    break

                    
                
            

        


main()


