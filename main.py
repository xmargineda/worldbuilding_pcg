import time
import random
import multiprocessing
import threading
from queue import Queue
import requests
from llm_manager import *
from query_manager import *
from queue import *
from process_prompts import *
from owlready2 import *
from ontology.classes.Action import Action
from ontology.classes.Chapter import Chapter
from ontology.classes.Character import Character
#from ontology.classes.Descriptor import Descriptor
from ontology.classes.Entity import Entity
#from ontology.classes.Fact import Fact
from ontology.classes.Group import Group
from ontology.classes.Item import Item
from ontology.classes.Location import Location
from ontology.classes.Main_Character import Main_Character
from ontology.classes.NonMain_Character import NonMain_Character
from ontology.classes.Place import Place
from ontology.classes.Settlement import Settlement
from ontology.classes.Thing import Thing


ontology_tree = {'Thing':['Chapter','Entity','Fact'], 'Chapter':[], 'Entity':['Character','Event','Group','Item','Location'], 'Character':['Main_Character', 'NonMain_Character'], 'Event':[], 'Group':[], 'Item':[], 'Location':['Settlement', 'Place'], 'Settlement':[], 'Place':[], 'Fact':['Action', 'Descriptor'], 'Action':[], 'Descriptor':[]}

def sendAndWaitForLLM(msg):
    llm_req.put(msg)
    while llm_res.empty():
        time.sleep(0.1)
    return llm_res.get()

def prompt_user(prompt, options, onlyOne = False):
    if isinstance(options, list):
        count = 1
        edited_options = []
        for o in options:
            edited_options.append(f'{count}. ' + o)
            count += 1
        while True:
            print(f'{prompt}\n\n')
            for opt in edited_options:
                print(opt)
            chosen = input('\n\nPlease answer the number of the options you have selected separated by commas (ex. 1, 2, 5, 7): ')
            chosen = list(map(lambda x: x.strip(), chosen.split(',')))
            print(chosen)
            if (len(chosen) <= 1 or not onlyOne):
                break

        res = []
        for n in chosen:
            res.append(options[int(n)-1])
        return res
    else:
        while True:
            input_val = input(f'{prompt}\n\n{options}\n\nPlease answer yes or no (y/n): ')
            if input_val == 'y':
                return options
            elif input_val == 'n':
                return [] 


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
                value = eval('ent.variables[\'' + par + '\'][\'values\']')
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
        obj.variables['onto_instance']['values'] = inst
        for prp in inst.get_properties():
            name_prp = str(prp).split('.')[1]
            prp_val = eval('inst.'+name_prp)
            if type(prp_val) == str:
                obj.add_attribute(atr = name_prp, val =prp_val)
            else:
                if type(prp_val) != owlready2.prop.IndividualValueList:
                    prp_val = [prp_val]

                for prp_v in prp_val:
                    if not str(prp_v).split('.')[0] == 'ontoTFGinstances':
                        obj.add_attribute(atr = name_prp, val =prp_v)

        if cl in instances:
            instances[cl].append(obj)
        else:
            instances[cl] = [obj]

    noRepeatList = []
    for key in instances:
        for val in instances[key]:
             
            if key == 'Action':
                val_id = (val.variables['fact']['values'])
            else:
                val_id = (val.variables['str_name']['values'])

            for prp in val.variables['onto_instance']['values'].get_properties():
                isObjProp = False
                for r in prp.range:
                    if str(r).split('.')[0] == 'ontoTFGinstances':
                        isObjProp = True
                        break
                if isObjProp:
                    name_prp = str(prp).split('.')[1]
                    prp_val = eval('val.variables[\'onto_instance\'][\'values\'].'+name_prp)
                    
                    for prp_v in prp_val:
                        srch = {}
                        
                        if str(prp_v.is_a[0]) == 'ontoTFGinstances.Action':
                            srch['fact'] = prp_v.fact
                            identifier = prp_v.fact
                        else:
                            srch['str_name'] = prp_v.str_name
                            identifier =prp_v.str_name
                        if identifier not in noRepeatList:
                            srch['class'] = str(prp_v.is_a[0]).split('.')[1]
                            res = search(universe = instances, srch_param = srch, find_group = False)
                            val.add_attribute(atr = name_prp, val = res)
            noRepeatList.append(val_id)
            print(val)

    return instances

    #take away noRepeatList if we can
    #replace the onto object check with the 'data things'

def save_ontology(inst, onto):
    print('start save')
    for cl in inst:
        for ins in inst[cl]:
            if ins.variables['onto_instance']['values'] == None:
                ins.variables['onto_instance']['values'] = eval(f"onto.{cl}(str_name)")

    for cl in inst:
        for ins in inst[cl]:
            onto_inst = ins.variables['onto_instance']['values']
            for prop in ins.variables:
                if prop != 'onto_instance':
                    prop_val = ins.variables[prop]['values']

                    if isinstance(prop_val,list):
                        onto_prop_lst = eval(f"onto_inst.{prop}")
                        for prop_v in prop_val:
                            if prop_v not in onto_prop_lst:
                                if isinstance(prop_v,str):
                                    prop_v_str = '\'' + prop_v + '\''
                                elif isinstance(prop_v,Thing):
                                    prop_v_str = "prop_v.variables['onto_instance']['values']"
                                else:
                                    prop_v_str = prop_v
                                exec(f"onto_inst.{prop}.append({prop_v_str})")
                    else:
                        if isinstance(prop_val,str):
                            prop_val = '\'' + prop_val + '\''
                        exec(f"onto_inst.{prop} = {prop_val}")
    
    onto.save(file = "ontology/result.owl", format = "rdfxml")


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
        properties = list(ent.variables.keys())
        rj = random.randint(0,len(properties)-1)
        if properties[rj] not in ['str_name', 'onto_instance'] and ent.variables[properties[rj]]['values'] == []:
            if ent.attribute_type(properties[rj]) == 'data':
                return { 'pipeline':'data_property_generation', 'entity':ent, 'property':properties[rj], 'value':ent.variables[properties[rj]]['values']}
            elif ent.attribute_type(properties[rj]) == 'entity':
                return { 'pipeline':'entity_property_generation', 'entity':ent, 'property':properties[rj], 'value':ent.variables[properties[rj]]['values']}


def data_property_generation_pipeline(obj):
    
    tpc = obj['entity'].variables['str_name']['values'] + '\''
    
    if tpc[-2] != 's':
        tpc += 's'
    tpc += ' ' + obj['property']
    msg = data_property_generator_text.format(gen_words=gen_words_data_prop_table[obj['property']], topic=tpc , topic_definition = obj['entity'].attribute_description(obj['property']) ,info_topic=obj['entity'].short_description())
    print('start pipe ' + tpc)
    answ = sendAndWaitForLLM({'txt':msg,'temp':2.00, 'max_tokens':300})
    print(answ['txt'])
    
    gen_cont = answ['txt'].split('Generated content:\n')[1].split('\n')
    gen_cont = list(map(lambda x: x.strip('-').strip('.'), gen_cont))
    
    
    gen_cont = prompt_user(prompt = f'The following content has been generated in reference to {tpc}:', options = gen_cont)
    #print(gen_cont)
    #print(obj['entity'])
    #NEXT STEP -> Update
    p = obj['property']
    for c in gen_cont:
        obj['entity'].add_attribute(atr = p, val = c)
        #exec(f'obj[\'entity\'].add_{p}(c)')
    #print(obj['entity'])


def entity_property_generation_pipeline(obj):
    
    tpc = obj['entity'].variables['str_name']['values'] + '\''
    
    if tpc[-2] != 's':
        tpc += 's '
    tpc += obj['property']
    msg = data_property_generator_text.format(gen_words=gen_words_data_prop_table[obj['property']], topic=tpc , topic_definition = obj['entity'].attribute_description(obj['property']) ,info_topic=obj['entity'].short_description())
    print('start pipe ' + tpc)
    answ = sendAndWaitForLLM({'txt':msg,'temp':2.00, 'max_tokens':300})
    print(answ['txt'])
    #prompt_user(disabled for now?)
    gen_cont = answ['txt'].split('Generated content:\n')[1].split('\n')
    gen_cont = list(map(lambda x: x.strip('-').strip('.'), gen_cont))
    #print(gen_cont)
    #print(obj['entity'])
    #NEXT STEP -> Update
    p = obj['property']
    for c in gen_cont:
        obj['entity'].add_attribute(atr = p, val = c)
        # exec(f'obj[\'entity\'].add_{p}(c)')
    #print(obj['entity'])


if __name__ == '__main__':
    
    global llm_req, llm_res, query_req, query_res
    llm_req = multiprocessing.Queue() #This queue sends the requests to the LLM
    llm_res = multiprocessing.Queue() #This queue sends the formated results of the LLM
    #query_req = Queue() #This queue sends the requests to the LLM
    #query_res = Queue() #This queue sends the formated results of the LLM

    pr_llm = multiprocessing.Process(target=llm_manager, args=(llm_req, llm_res))
    #th_query = threading.Thread(target=query_manager, args=(query_req, query_res))

    try:
        pr_llm.start()
        #th_query.start()
        #onto = get_ontology("file://ontology/ontoTFG.owl").load()
        onto = get_ontology("file://ontology/ontoTFGinstances.owl").load()

        sync_reasoner()
        instances = initialize_classes(onto)

        #print(instances['Item'][1].__dict__)
        #print(instances['Item'][1].__class__.__name__)
        #print(recursive_superclass(instances['Item'][1].__class__))
        
        while not isItDone(instances):
            obj = pick_pipeline(instances)
            #print(obj['entity'].short_description())
            
            match obj['pipeline']:
                case 'data_property_generation':
                    data_property_generation_pipeline(obj)
                case 'entity_property_generation':
                    #entity_property_generation
                    pass
                #case 'entity_property_relation':
                #case 'story_action_generation':

            #run_llm
            #prompt_user
            #update

        save_ontology(instances, onto)
        pr_llm.terminate()
        pr_llm.join()
        #th_query.join()
  
    except KeyboardInterrupt:
        print("Interrupt caught")
        pr_llm.terminate()
        pr_llm.join()
        #th_query.join()
        save_ontology(instances, onto)
