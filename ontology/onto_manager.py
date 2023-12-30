from owlready2 import *
import time
import random

#'str_name'
char_adj_num = 3

                
def recursive_subclass_locator(dom):
    if len(list(dom.subclasses())) == 0:
        return [dom]
    else:
        res = []
        for subc in list(dom.subclasses()):
            res.extend(recursive_subclass_locator(subc))
        return res


def ontology_manager(req_q, res_q):
    #onto = get_ontology("file://ontology/ontoTFG.owl").load()
    onto = get_ontology("file://ontology/ontoTFGinstances.owl").load()

   
    
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

    while True:
        while req_q.empty():
            time.sleep(0.1)
        ## Here request from onto_req_q are treated, normally queries about the ontology
        req = req_q.get()

        match req['func']:
            case 'entity_creation':
                match req['txt'][1]:
                    case 'Character':
                        onto.Character(name = req['txt'][0])
                    case 'Place':
                        onto.Place(name = req['txt'][0])
                    case 'Settlement':
                        onto.Settlement(name = req['txt'][0])
                    case 'Group':
                        onto.Group(name = req['txt'][0])
                    case 'Entity':
                        onto.Entity(name = req['txt'][0])
                    case _:
                        print('Entity not recognized: ' + str(req['txt']))
            
            case 'chapter_batch_creation':
                txt = req['txt']
                pre_chapt = []
                pre_action = []
                for ch in txt:
                    chapter = onto.Chapter(name = ch[0], description = ch[1])
                    
                    for st in ch[2]:
                        
                        act = onto.Action()
                        act.fact = st
                        chapter.contains.append(act)
                        if not isinstance(pre_action, list):
                            act.prevAction.append(pre_action)
                        pre_action = act
                        print(act.name)

                    if not isinstance(pre_chapt, list):
                        chapter.prevChapter.append(pre_chapt)
                    pre_chapt = chapter
            
            case 'querry':
                qrry = "onto.search("
                
                q = req['txt']
                for k in list(q.keys()):
                    qrry = qrry + k + '=' + q[k]
                
                qrry = qrry + ')'
                
                res = eval(qrry, {'onto':onto})
                print(res)
                res_q.put({'func':'querry','type':'res','txt':res})

            case 'short_description':
                obj = req['txt']
                desc = ''
                print(obj)
                match obj['type']:
                    case 'Main_Character':
                        char = onto.search(str_name=obj['name'], is_a = onto.Character)[0]
                        name = char.str_name
                        desc = name + ' is a main character within the story.'

                        if len(char.profession) > 0:
                            desc += ' ' + name + ' works as a ' + char.profession[0] + '.'

                        if len(char.description) > 0:
                            desc += ' Here\'s some information about ' + name + ':\n' + random_list_formater(char.description, char_adj_num, 2)


                        if len(char.isInvolvedIn) > 0:
                            desc += ' Here are some events that ' + name + ' is involved in:\n' + random_list_formater( list(map(lambda x: x.fact, char.isInvolvedIn)), 3, 2 )

                    case 'Primary_Character':
                        char = onto.search(str_name=obj['name'], is_a = onto.Character)[0]
                        name = char.str_name
                        desc = name + ' is a primary character within the story.'

                        if len(char.profession) > 0:
                            desc += ' ' + name + ' works as a ' + char.profession[0] + '.'

                        if len(char.description) > 0:
                            desc += ' Here\'s some information about ' + name + ':\n' + random_list_formater(char.description, char_adj_num, 2)


                        if len(char.isInvolvedIn) > 0:
                            desc += ' Here are some events that ' + name + ' is involved in:\n' + random_list_formater( list(map(lambda x: x.fact, char.isInvolvedIn)), 3, 2 )

                    case 'Secondary_Character':
                        char = onto.search(str_name=obj['name'], is_a = onto.Character)[0]
                        name = char.str_name
                        desc = name + ' is a secondary character within the story.'

                        if len(char.profession) > 0:
                            desc += ' ' + name + ' works as a ' + char.profession[0] + '.'

                        if len(char.description) > 0:
                            desc += ' Here\'s some information about ' + name + ':\n' + random_list_formater(char.description, char_adj_num, 2)


                        if len(char.isInvolvedIn) > 0:
                            desc += ' Here are some events that ' + name + ' is involved in:\n' + random_list_formater( list(map(lambda x: x.fact, char.isInvolvedIn)), 3, 2 )

                    case 'Place':
                        loc = onto.search(str_name=obj['name'], is_a = onto.Place)[0]
                        name = loc.str_name
                        desc = name + ' is a place within the story with some kind of relevance.'

                        if len(loc.value) > 0:
                            desc += ' The reason why ' + name + ' is relevant is the following: ' + random_list_formater(loc.value, char_adj_num, 1) + '.'
                        
                        if len(loc.description) > 0:
                            desc += ' Here\'s some information about ' + name + ':\n' + random_list_formater(loc.description, 2, 1) + '.'

                        if len(loc.isInvolvedIn) > 0:
                            desc += ' Here are some events that are related to ' + name + ':\n' + random_list_formater( list(map(lambda x: x.fact, loc.isInvolvedIn)), 3, 2 )

                    case 'Settlement':
                        loc = onto.search(str_name=obj['name'], is_a = onto.Settlement)[0]
                        name = loc.str_name
                        desc = name + ' is a location within the story where a group of people live.'
                        
                        if len(loc.population) > 0:
                            desc += ' There are ' + loc.population[0] + 'living in ' + name   + '.'

                        if len(loc.description) > 0:
                            desc += ' Here\'s some information about ' + name + ':\n' + random_list_formater(loc.description, 2, 2)

                        if len(loc.isInvolvedIn) > 0:
                            desc += ' Here are some events that are related to ' + name + ':\n' + random_list_formater( list(map(lambda x: x.fact, loc.isInvolvedIn)), 3, 2 )
                    
                    case 'Group':
                        gr = onto.search(str_name=obj['name'], is_a = onto.Group)[0]
                        name = gr.str_name
                        desc = name + ' is a group of people that regurlarly work together within the story.'

                        if len(gr.description) > 0:
                            desc += ' Here\'s some information about ' + name + ':\n' + random_list_formater(gr.description, 2, 2)

                        if len(gr.objective) > 0:

                            if len(gr.objective) == 1:
                                desc += ' The reason this group exists is the following: ' + gr.objective[0] + '.'
                            else:
                                desc += ' The reasons this group exists are the following: ' + random_list_formater(gr.objective, 3, 1) + '.'
                        
                        if len(gr.lead) > 0:
                            desc += ' The group is lead by ' + gr.lead[0].str_name + '.'

                        # if len(gr.organization) > 0:
                        #     desc += ' The group is organized in the following way: ' + gr.organization[0] + '.'

                        if len(gr.isInvolvedIn) > 0:
                            desc += ' Here are some events that are related to the group:\n' + random_list_formater( list(map(lambda x: x.fact, gr.isInvolvedIn)), 3, 2 )

                    case 'Item':
                        it = onto.search(str_name=obj['name'], is_a = onto.Item)[0]
                        name = it.str_name
                        desc = name + ' is an object of importance within the story.'

                        if len(it.description) > 0:
                            desc += ' Here\'s some information about ' + name + ':\n' + random_list_formater(it.description, 2, 2) 

                        if len(it.value) > 0:
                            desc += ' The reason why ' + name + ' is relevant is the following: ' + random_list_formater(it.value, char_adj_num, 1) + '.'
                        
                        if len(it.use) > 0:
                            desc += ' The item can be used in one of the following ways: ' + random_list_formater(it.use, char_adj_num, 1) + '.'
                        
                        if len(it.isInvolvedIn) > 0:
                            desc += ' Here are some events that are related to the object:\n' + random_list_formater( list(map(lambda x: x.fact, it.isInvolvedIn)), 3, 2 )

                    case 'Entity':
                        ent = onto.search(str_name=obj['name'], is_a = onto.Entity)[0]
                        name = ent.str_name
                        desc = name + ' is an important element within the narrative.'

                        if len(ent.description) > 0:
                            desc += name + ' can be described in the following ways:\n' + random_list_formater(ent.description, 2, 2)
                        
                        if len(ent.isInvolvedIn) > 0:
                            desc += ' Here are some events that are related to ' + name + ' :\n' + random_list_formater( list(map(lambda x: x.fact, ent.isInvolvedIn)), 3, 2 )

                    
                req_res = {'func':'short_description','type':'res','txt':desc}
                if 'process' in req:
                    req_res['process'] = req['process']
                    req_res['id'] = 'short_description_'+name.replace(' ','_')
                res_q.put(req_res)

            case 'medium_description':
                print('medium_description')

            case 'large_description':
                print('large_description')

            case 'onto_review':
                
                empt = {}

                for inst in onto.Entity.instances():
                    empt[inst] = []
                    inst_prop_ls = list(map(lambda x:str(x) ,inst.get_properties()))
                    for prop in dprop_ls[str(inst.is_a[0])]:
                        if prop not in inst_prop_ls:
                            empt[inst].append(prop)

                chosen = False

                while not chosen:
                    ri = random.randint(0,len(empt)-1)
                    ent = list(empt.keys())[ri]
                    rj = random.randint(0,len(empt[ent])-1)
                    chosen = True
                print('CHOSEN PROPERTY')
                print(empt[ent][rj])


                res_q.put({'func':'data_prop_generate','type':'req','txt':[str(ent), empt[ent][rj], str(ent.is_a[0])]})
                #res_q.put({'func':'data_prop_generate','type':'req','txt':[str(ent), empt[ent][rj], str(ent.is_a[0])]})
                










                    
                

                    

        

            

        



