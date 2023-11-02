import requests
import time
import multiprocessing
from ontology.onto_manager import * 

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

def llm_manager(req_q, res_q):
    time.sleep(100)

# def onto_manager(llm_res_q, onto_req_q, onto_res_q):
#     onto = get_ontology("file://ontoTFG2.owl").load()



if __name__ == '__main__':

    llm_req_q = multiprocessing.Queue() #This queue sends the requests to the LLM
    llm_res_q = multiprocessing.Queue() #This queue sends the formated results of the LLM
    onto_req_q = multiprocessing.Queue() #This queue sends the requests to the ontology manager (mostly queries)
    onto_res_q = multiprocessing.Queue() #This queue sends the formated results of the ontology manager (mostly queries)
    # req_q = 1
    # res_q = 1
    pr_man = multiprocessing.Process(target=llm_manager, args=(llm_req_q, llm_res_q))
    pr_llm = multiprocessing.Process(target=ontology_manager, args=(llm_res_q, onto_req_q, onto_res_q))
    
    try:
        pr_man.start()
        pr_llm.start()
        loop = True
        while loop:
            print("?- What is your command?\n-exit")
            inp = input()
            if inp == "exit":
                loop = False
            elif inp == "checkO":
                onto_req_q.put("a")
                while onto_res_q.empty():
                    time.sleep(0.1)
                print(onto_res_q.get())
            else:
                print("!- Command not identified\n")
        pr_man.terminate()
        pr_llm.terminate()
        pr_man.join()
        pr_llm.join()


    except KeyboardInterrupt:
        print("Interrupt caught")
        pr_man.terminate()
        pr_llm.terminate()
        pr_man.join()
        pr_llm.join()

            

        



