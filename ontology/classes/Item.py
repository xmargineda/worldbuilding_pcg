from ontology.classes.Entity import Entity
from ontology.classes.formating_functions import *

class Item(Entity):
    
    def __init__(self):
        super().__init__()
        self.variables.update({
            'appearance' : {'values': [], 'description':'The look of this item and any relevant details', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'material' : {'values': [], 'description':'The materials it is made of', 'type':'data', 'contx_expr': 'wordList', 'contx_str':' The item is made of {val}.', 'prop_reg': 'list'},
            'use' : {'values': [], 'description':'What are the different ways this item can be used', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'value' : {'values': [], 'description':'Why is this item relevant within the story', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'holder' : {'values': [], 'description':'A character or group that is in possesion of this item', 'type':'entity',  'contx_expr': 'singleWord', 'contx_str':' {name} is in the hands of {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'possession'},
            'placement' : {'values': [], 'description':'A location where the item is residing.', 'type':'entity',  'contx_expr': 'singleWord', 'contx_str':' {name} is residing in {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'asset'},
            'usage_event' : {'values': [], 'description':'An event where this item was used (if there is any).', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' {name} was used in the following events: {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'object'}
        })

    def short_description(self):
        desc = f'{self.variables["str_name"]["values"]} is an object of importance within the story.'
        if self.variables["description"]["values"]:
            desc += f'{random_list_formater(self.variables["description"]["values"], 2, 3)}'         
        # if self.variables["use"]["values"]:
        #     desc += f'{random_list_formater(self.variables["use"]["values"], 3, 3)}'
        desc += self.entity_context_gathering(3)
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some events that are related to the object:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'

        return desc