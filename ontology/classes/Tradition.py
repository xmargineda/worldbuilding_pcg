from ontology.classes.Event import Event
from ontology.classes.formating_functions import *

class Tradition(Event):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'frequency' : {'values': [], 'description':'The amount of time passed between each iteration of the tradition.', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'origin' : {'values': [], 'description':'What is the supposed origin of this tradition?', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'rituals' : {'values': [], 'description':'What are the rituals and customs involved in this tradition? (if there are any)', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'venue' : {'values': [], 'description':'A location where this tradition is celebrated.', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' {name} is usually celebrated in {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'tradition'}
            })


    def short_description(self):
        desc =  f'{self.variables["str_name"]["values"]} is a tradition from the story.'
        desc += self.entity_context_gathering(3)
        # if self.variables["origin"]["values"]:
        #     desc += f'{random_list_formater( self.variables["origin"]["values"], 3, 3 )}'
        # if self.variables["rituals"]["values"]:
        #     desc += f'{random_list_formater( self.variables["rituals"]["values"], 3, 3 )}'
        # if self.variables["venue"]["values"]:
        #     desc += f' The tradition is usually celebrated in {random_list_formater( list(map(lambda x: x.variables["str_name"]["values"], self.variables["venue"]["values"])), 3, 1 )}'
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some relevant occurrences that are involved with the tradition:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'
        
        return desc
