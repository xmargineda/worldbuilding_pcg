from ontology.classes.Event import Event
from ontology.classes.formating_functions import *

class Tradition(Event):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'frequency' : {'values': [], 'description':'The amount of time passed between each iteration of the tradition.', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'origin' : {'values': [], 'description':'What is the supposed origin of this tradition?', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'rituals' : {'values': [], 'description':'What are the rituals and customs involved in this tradition? (if there are any)', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'venue' : {'values': [], 'description':'This tradition is celebrated in the new {gen}.', 'type':'entity', 'gen_cont':['Settlement','Place'], 'contx_expr': 'wordList', 'contx_str':' {name} is usually celebrated in {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'tradition'}
            })


    def short_description(self):
        desc =  f'{self.variables["str_name"]["values"]} is a tradition from the story.'
        if self.variables["description"]["values"]:
            desc += f'{random_list_formater(self.variables["description"]["values"], 3, 3)}'
        desc += self.entity_context_gathering(3)
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some relevant occurrences that are involved with the tradition:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'
        
        return desc
