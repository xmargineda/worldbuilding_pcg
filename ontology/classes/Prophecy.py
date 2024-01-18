from ontology.classes.Event import Event
from ontology.classes.formating_functions import *

class Prophecy(Event):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'origin' : {'values': [], 'description':'What is the origin of this prophecy?', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'location' : {'values': [], 'description':'The new {gen} is connected to this prophecy.', 'type':'entity', 'gen_cont':['Location', 'Place', 'Settlement'], 'contx_expr': 'wordList', 'contx_str':' The prophecy is linked to locations such as {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'event'}
            })

    def short_description(self):
        desc =  f'{self.variables["str_name"]["values"]} is a prophecy wihin the story.'
        if self.variables["description"]["values"]:
            desc += f'{random_list_formater(self.variables["description"]["values"], 3, 3)}'
        desc += self.entity_context_gathering(3)
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some relevant occurrences that are involved with the prophecy:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'
        
        return desc