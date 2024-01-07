from ontology.classes.Event import Event
from ontology.classes.formating_functions import *

class Prophecy(Event):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'origin' : {'values': [], 'description':'What is the origin of this prophecy?', 'type':'data', 'prop_reg': 'list'},
            'location' : {'values': [], 'description':'A location connected to this prophecy.', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'event'}
            })

    def short_description(self):
        desc =  f'{self.variables["str_name"]["values"]} is a prophecy wihin the story.'
        if self.variables["origin"]["values"]:
            desc += f' {random_list_formater( list(map(lambda x: x.variables["str_name"]["values"], self.variables["origin"]["values"])), 3, 3 )}.'
        if self.variables["location"]["values"]:
            desc += f' The prophecy foretells events that are believed to happen in {self.variables["str_name"]["values"]} {random_list_formater( list(map(lambda x: x.variables["str_name"]["values"], self.variables["location"]["values"])), 3, 1 )}'
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some relevant occurrences that are involved with the prophecy:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'
        
        return desc