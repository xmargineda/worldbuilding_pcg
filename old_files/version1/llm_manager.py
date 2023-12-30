import requests
import time

# For local streaming, the websockets are hosted without ssl - http://
HOST = 'localhost:5000'
URI = f'http://{HOST}/api/v1/generate'

# For reverse-proxied streaming, the remote will likely host with ssl - https://
# URI = 'https://your-uri-here.trycloudflare.com/api/v1/generate'


def print_basic_model_info(response):
    basic_settings = ['truncation_length', 'instruction_template']
    print("Model: ", response['result']['model_name'])
    print("Lora(s): ", response['result']['lora_names'])
    for setting in basic_settings:
        print(setting, "=", response['result']['shared.settings'][setting])

# model info
def model_info():
    response = model_api({'action': 'info'})
    return response

def model_api(request):
    response = requests.post(f'http://{HOST}/api/v1/model', json=request)
    return response.json()

def model_load(model_name):
    return model_api({'action': 'load', 'model_name': model_name})

def run(prompt,temp, max_tokens):
    request = {
        'prompt': prompt,
        'max_new_tokens': max_tokens,
        'auto_max_new_tokens': False,
        'max_tokens_second': 0,

        # Generation params. If 'preset' is set to different than 'None', the values
        # in presets/preset-name.yaml are used instead of the individual numbers.
        'preset': 'None',
        'do_sample': True,
        'temperature': temp,      #0.01 FOR STORY ACTIONS | 0.7 is average i think
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

    if (model_info()['result']['model_name']) == 'None':
        resp = model_load(model)
    
    while True:
        while req_q.empty():
            time.sleep(0.1)
        req = req_q.get()
        res_dict = {'txt':run(req['txt'], req['temp'], req['max_tokens']), 'func':req['func'], 'type':'res'} 
        if 'process' in req:
            res_dict['process'] = req['process']
            res_dict['id'] = req['id']
        res_q.put(res_dict)

        



