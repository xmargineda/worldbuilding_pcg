import time
import random
from queue import *
from process_prompts import *
from owlready2 import *
from ontology.classes.Action import Action
from ontology.classes.Chapter import Chapter
from ontology.classes.Character import Character
from ontology.classes.Descriptor import Descriptor
from ontology.classes.Entity import Entity
from ontology.classes.Fact import Fact
from ontology.classes.Group import Group
from ontology.classes.Item import Item
from ontology.classes.Location import Location
from ontology.classes.Main_Character import Main_Character
from ontology.classes.NonMain_Character import NonMain_Character
from ontology.classes.Place import Place
from ontology.classes.Settlement import Settlement
from ontology.classes.Thing import Thing

active_processes = {}

last_given_id = 0

generating_process_id = -1
prev_generating_time = time.time()

generation_resting_time = 1

ontology_tree = {'Thing':['Chapter','Entity','Fact'], 'Chapter':[], 'Entity':['Character','Event','Group','Item','Location'], 'Character':['Main_Character', 'NonMain_Character'], 'Event':[], 'Group':[], 'Item':[], 'Location':['Settlement', 'Place'], 'Settlement':[], 'Place':[], 'Fact':['Action', 'Descriptor'], 'Action':[], 'Descriptor':[]}


def generating_function_check():
    laptime = round((time.time() - prev_generating_time), 2)
    if generation_resting_time < laptime and generating_process_id == -1:
        return True


# rcv : llm, onto, main //It's the reciever
# func : raw_input_processing, raw_input_character,
def evaluate_request(req, generate):
    evl = []
    
    if generate:
        global generating_process_id
        generating_process_id = 1
        evl.append({'func':'onto_review', 'rcv': 'onto'})

    # Input processing
    if req['func'] == 'raw_input_processing' and req['type'] == 'req': 
        evl.append({'txt':(raw_input_character_txt + req['txt'] + '\nCatergorization:\n'), 'func':'raw_input_character', 'temp':0.01, 'max_tokens':300, 'rcv': 'llm'})
    
    # Entities output processing
    elif req['func'] == 'raw_input_character' and req['type'] == 'res': 
        
        entity_list = req['txt'].split('Catergorization:\n')[2].split('Text:')[0].split('\n')
        entity_list = list(map(lambda e: list(map(lambda x: x.strip(), e[1:].split('->'))), entity_list))
        entity_list_parsed = ''
        for e in entity_list:
            evl.append({'txt':e, 'func':'entity_creation', 'rcv': 'onto'})
            entity_list_parsed = entity_list_parsed + '- ' + e[0] + '\n'
        evl.append({'txt':(raw_input_story_txt + req['txt'].split('Text:')[2].split('Catergorization:')[0].strip()  + '\nEntities:\n' + entity_list_parsed + 'Story:\n'), 'func':'raw_input_story_action', 'temp':0.01, 'max_tokens':300, 'rcv': 'llm'})
    
    #Story actions output processing
    elif req['func'] == 'raw_input_story_action' and req['type'] == 'res': 
        chapter_list = req['txt'].split('Story:')[2].split('Chapter')[1:]
        ch_list = []
        for c in chapter_list:
            aux = c.split(':')
            name = aux[0].strip().strip('\"')
            aux = aux[1].strip('\n').split('\n')
            desc = aux[0].strip()
            aux = aux[1:]
            st_act = list(map(lambda st: st.split('. ')[1], aux))
            ch_list.append([name, desc, st_act])
        print(ch_list)
        evl.append({'txt':ch_list, 'func':'chapter_batch_creation', 'rcv': 'onto'})
    
    ##Get short description from ontology
    elif req['func'] == 'short_description' and req['type'] == 'res':
        
        if 'process' in req:
            active_processes[req['process']]['requirements'][active_processes[req['process']]['requirements'].index(req['id'])] = req['txt']
            active_processes[req['process']]['values'] += 1
            if active_processes[req['process']]['values'] == len(active_processes[req['process']]['requirements']):
                evl.append({'func':active_processes[req['process']]['func']+'_llm', 'rcv': 'self', 'process':req['process'], 'type':'req'})
        
    ## Start for generating data properties
    elif req['func'] == 'data_prop_generate' and req['type'] =='req':
        name = req['txt'][0].split('.')[-1]
        prop = req['txt'][1].split('.')[-1]
        tp = req['txt'][2].split('.')[-1]
        active_processes['gen_data_prop_' + name + '_' + prop] = {'entity':name, 'property':prop, 'func':'data_prop_generate', 'requirements':['short_description_'+name], 'values': 0}
        desc_dict = {'name':name.replace('_',' '),'type':tp}
        
        evl.append({'txt':desc_dict, 'func':'short_description', 'rcv': 'onto', 'process':'gen_data_prop_' + name + '_' + prop})

    elif req['func'] == 'data_prop_generate_llm' and req['type'] =='req':
        prss = active_processes[req['process']]
         
        txt = data_property_generator_text[0] + data_prop_table[prss['property']] + data_property_generator_text[1]
        if prss['entity'][-1] == 's':
            txt += prss['entity'].replace('_',' ') + '\' '
        else:
            txt += prss['entity'].replace('_',' ') + '\'s '
        txt += prss['property'] + data_property_generator_text[2] + prss['requirements'][0] 

        txt += data_property_generator_text[-1]
        evl.append({'txt':txt, 'func':'data_prop_generate_llm', 'temp':2.00, 'max_tokens':300, 'rcv': 'llm'})
    
    elif req['func'] == 'data_prop_generate_llm' and req['type'] =='res':
        
        print(req['txt'])
        print(req['txt'].split('Generated list:\n')[1].split('\n'))
        active_processes
        

    elif req['func'] == 'debug':
        desc_dict = {'name':'Fiona','type':'Character'}
        evl.append({'txt':desc_dict, 'func':'short_description', 'rcv': 'onto'})
        desc_dict = {'name':'Cerise','type':'Character'}
        evl.append({'txt':desc_dict, 'func':'short_description', 'rcv': 'onto'})
        desc_dict = {'name':'Coelus','type':'Group'}
        evl.append({'txt':desc_dict, 'func':'short_description', 'rcv': 'onto'})
        desc_dict = {'name':'Arcane Prism','type':'Item'}
        evl.append({'txt':desc_dict, 'func':'short_description', 'rcv': 'onto'})
        desc_dict = {'name':'Segalia','type':'Settlement'}
        evl.append({'txt':desc_dict, 'func':'short_description', 'rcv': 'onto'})
    
    return evl


def search(universe, srch_param, find_group = True):
    
    if 'class' in srch_param:
        expl_area = universe[srch_param['class']]
    else:
        expl_area = []
        for k in universe:
            expl_area.extend(universe[k])
    res = []
    for ent in expl_area:
        plaus = True
        for par in srch_param:
            if par != 'class':
                value = eval('ent.' + par)
                if not isinstance(srch_param[par], list) and value != srch_param[par]:
                    plaus = False
                    break 
                else:
                    if any(list(map(lambda x: not x in value, srch_param[par]))):
                        plaus = False
                        break
        if plaus:
            if not find_group:
                return ent
            else:
                res.append(ent)
    
    if find_group:
        return res
    else:
        return None
            
        
        #check if the search parameter are followed

def recursive_subclass_locator(dom):
    if len(list(dom.subclasses())) == 0:
        return [dom]
    else:
        res = []
        for subc in list(dom.subclasses()):
            res.extend(recursive_subclass_locator(subc))
        return res

def recursive_superclass(cla):
    print(cla)
    res = []
    res.append(str(cla).split('.')[-1].strip('\'>'))
    for c in cla.__bases__:
        if 'class \'object\'' in str(c):
            return res
        else:            
            res.extend(recursive_superclass(c))
    return res


def initialize_classes(onto):
    instances = {}
    for inst in onto.individuals():
        cl = str(inst.is_a[0]).split('.')[1]
        obj = eval(cl +'()')
        obj.onto_instance = inst
        for prp in inst.get_properties():
            name_prp = str(prp).split('.')[1]
            prp_val = eval('inst.'+name_prp)
            if type(prp_val) == str:
                exec('obj.add_' + name_prp + '(\'' + str(prp_val) + '\')')
            else:
                if type(prp_val) != owlready2.prop.IndividualValueList:
                    prp_val = [prp_val]

                for prp_v in prp_val:
                    if not str(prp_v).split('.')[0] == 'ontoTFGinstances':
                        exec('obj.add_' + name_prp + '(\'' + prp_v + '\')')

        if cl in instances:
            instances[cl].append(obj)
        else:
            instances[cl] = [obj]

    noRepeatList = []
    for key in instances:
        for val in instances[key]:
             
            if key in ['Action', 'Descriptor']:
                val_id = (val.fact)
            else:
                val_id = (val.str_name)

            for prp in val.onto_instance.get_properties():
                isObjProp = False
                for r in prp.range:
                    if str(r).split('.')[0] == 'ontoTFGinstances':
                        isObjProp = True
                        break
                if isObjProp:
                    name_prp = str(prp).split('.')[1]
                    prp_val = eval('val.onto_instance.'+name_prp)
                    
                    for prp_v in prp_val:
                        srch = {}
                        
                        if str(prp_v.is_a[0]) in ['ontoTFGinstances.Action', 'ontoTFGinstances.Descriptor']:
                            srch['fact'] = prp_v.fact
                            identifier = prp_v.fact
                        else:
                            srch['str_name'] = prp_v.str_name
                            identifier =prp_v.str_name
                        if identifier not in noRepeatList:
                            srch['class'] = str(prp_v.is_a[0]).split('.')[1]
                            res = search(universe = instances, srch_param = srch, find_group = False)
                            
                            exec('val.add_' + name_prp + '(res)')
            noRepeatList.append(val_id)

    aux_ls = list(onto.object_properties()).copy()
    aux_ls2 = list(onto.data_properties()).copy()

    dprop_ls = {}
    for prop in aux_ls2:
        for dom in prop.domain:
            dom_ls = recursive_subclass_locator(dom)
            for sdom in dom_ls:
                if str(sdom) in dprop_ls.keys():
                    dprop_ls[str(sdom)].append(str(prop))
                else:
                    dprop_ls[str(sdom)] = [str(prop)]

    oprop_ls = {}
    for prop in aux_ls:
        for dom in prop.domain:
            dom_ls = recursive_subclass_locator(dom)
            for sdom in dom_ls:
                if str(sdom) in oprop_ls.keys():
                    oprop_ls[str(sdom)].append(str(prop))
                else:
                    oprop_ls[str(sdom)] = [str(prop)]

    #print(dprop_ls)
    #print(oprop_ls)

    return instances

def isItDone(instances):
    #FUNCTION TO REPRESENT IF THE GENERATOR SHOULD STOP
    return False

def pick_pipeline(instances):
    entities = []

    for k in instances.keys():
        temp = eval(f'{k}()')
        if isinstance(temp, Entity):
            entities.extend(instances[k])
    
    chosen = False

    while not chosen:
        ri = random.randint(0,len(entities)-1)
        ent = entities[ri]
        properties = list(ent.__dict__.keys())

        rj = random.randint(0,len(properties)-1)
        if properties[rj] not in ['str_name', 'onto_instance'] and ent.__dict__[properties[rj]] == []:
            chosen = True
    print('CHOSEN PROPERTY')
    print(f'{ent.str_name}\'s {properties[rj]}')
        
    return {'pipeline':'property_value_generation', 'entity':ent, 'property':properties[rj], 'value':ent.__dict__[properties[rj]]}



def process_manager(main_req_q, main_res_q, llm_req_q, llm_res_q, onto_req_q, onto_res_q):
    
    llm_priority_q = PriorityQueue()
    onto_priority_q = PriorityQueue()
    self_q = Queue()

    #onto = get_ontology("file://ontology/ontoTFG.owl").load()
    onto = get_ontology("file://ontology/ontoTFGinstances.owl").load()


    sync_reasoner()
    instances = initialize_classes(onto)

    #print(instances['Item'][1].__dict__)
    #print(instances['Item'][1].__class__.__name__)
    print(recursive_superclass(instances['Item'][1].__class__))
    
    while not isItDone(instances):
        obj = pick_pipeline(instances)
        print(obj['entity'].short_description())
        time.sleep(60)
        match obj['pipeline']:
            case 'property_value_generation':
                prop_val_generation_pipeline(obj)

        #run_llm
        #prompt_user
        #update

        

    # while True:
    #     generate = False
    #     while main_req_q.empty() and llm_res_q.empty() and onto_res_q.empty() and self_q.empty() and not generate:
    #         time.sleep(0.1)
    #         generate = generating_function_check()

    #     if not main_req_q.empty():
    #         req = main_req_q.get()
    #     elif not llm_res_q.empty():
    #         req = llm_res_q.get()
    #     elif not onto_res_q.empty():
    #         req = onto_res_q.get()
    #     elif not self_q.empty():
    #         req = self_q.get()
    #     else:
    #         req = {'func':'skip'}

    #     evl = evaluate_request(req, generate)
    #     for e in evl:
    #         if e['rcv'] == 'llm':
    #             llm_req_q.put(e)
    #         elif e['rcv'] == 'onto':
    #             onto_req_q.put(e)
    #         elif e['rcv'] == 'main':
    #             main_req_q.put(e)
    #         elif e['rcv'] == 'self':
    #             self_q.put(e)

        

