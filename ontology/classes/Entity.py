from ontology.classes.Thing import Thing
from ontology.classes.formating_functions import *

class Entity(Thing):
    

    def __init__(self):
        super().__init__()
        self.variables.update({
            'isInvolvedIn' : {'values' : [], 'description':'The facts that the entity is involved in', 'type':'fact', 'prop_reg': 'reflexiveList', 'reflect':'isRelatedTo'}
        })

    def entity_context_gathering(self, size):
        non_empty_vars = [key for key, value in self.variables.items() if value['values'] not in [ [], None, ''] and key not in ['str_name', 'description','onto_instance', 'isInvolvedIn']]
        if len(non_empty_vars) < 1:
            return ''
        sel_vars = random.sample(non_empty_vars, min(size, len(non_empty_vars)))
        context = ''

        for key in sel_vars:
            match self.variables[key]['contx_expr']:
                case 'singleWord':
                    if isinstance(self.variables[key]["values"], list):
                            v = self.variables[key]["values"][0]
                    else:
                        v = self.variables[key]["values"]

                    if self.variables[key]['type'] == 'entity':
                        v = v.variables['str_name']['values']
                        
                    context += self.variables[key]['contx_str'].format(name = self.variables['str_name']['values'], val = v)

                case 'wordList':
                    if self.variables[key]['type'] == 'entity':
                        v = random_list_formater( list(map(lambda x: x.variables["str_name"]["values"], self.variables[key]["values"])), 3, 1 )
                    elif self.variables[key]['type'] == 'data':
                        v = random_list_formater(self.variables[key]["values"], 3, 1 )
                    context += self.variables[key]['contx_str'].format(name = self.variables['str_name']['values'], val =  v)

                case 'sentenceList':
                    context += random_list_formater(self.variables[key]["values"], 3, 3)

        return context


    def short_description(self):
        desc = f'{self.variables["str_name"]["values"]} is an important element within the narrative.'
        if self.variables["description"]["values"]:
            desc += f'{random_list_formater(self.variables["description"]["values"], 2, 3)}'      
        desc += self.entity_context_gathering(3)
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some events that are related to the object:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'

        return desc

