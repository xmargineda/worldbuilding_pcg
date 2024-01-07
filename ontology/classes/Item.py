from ontology.classes.Entity import Entity
from ontology.classes.formating_functions import *

class Item(Entity):
    
    def __init__(self):
        super().__init__()
        self.variables.update({
            'appearance' : {'values': [], 'description':'The look of this item and any relevant details', 'type':'data', 'prop_reg': 'list'},
            'material' : {'values': [], 'description':'The materials it is made of', 'type':'data', 'prop_reg': 'list'},
            'use' : {'values': [], 'description':'What are the different ways this item can be used', 'type':'data', 'prop_reg': 'list'},
            'value' : {'values': [], 'description':'Why is this item relevant within the story', 'type':'data', 'prop_reg': 'list'},
            'holder' : {'values': [], 'description':'A character or group that is in possesion of this item', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'possession'},
            'placement' : {'values': [], 'description':'A location where the item is residing.', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'asset'},
            'usage_event' : {'values': [], 'description':'An event where this item was used (if there is any).', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'object'}
        })

    def short_description(self):
        desc = f'{self.variables["str_name"]["values"]} is an object of importance within the story.'
        if self.variables["description"]["values"]:
            desc += f' Here\'s some information about {self.variables["str_name"]["values"]}:\n{random_list_formater(self.variables["description"]["values"], 2, 2)}'         
        if self.variables["use"]["values"]:
            desc += f' The item can be used in one of the following ways: {random_list_formater(self.variables["use"]["values"], 3, 1)}.'
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some events that are related to the object:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'

        return desc