from ontology.classes.Event import Event
from ontology.classes.formating_functions import *

class Historic_Incident(Event):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'time_elapsed' : {'values': [], 'description':'How much time has passed since an occurance of the event.', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'location' : {'values': [], 'description':'A location connected to this historic incident.', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' The event took place in {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'event'},
            'participant' : {'values': [], 'description':'A group or character involved in this event.', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' {name} had {val} as partticipants.', 'prop_reg': 'reflexiveList', 'reflect': 'involvement'}
            })

    def short_description(self):
        desc =  f'{self.variables["str_name"]["values"]} is a historic incident within the story.'
        desc += self.entity_context_gathering(3)
        # if self.variables["time_elapsed"]["values"]:
        #     desc += f'{random_list_formater(self.variables["time_elapsed"]["values"], 3, 3 )}'
        # if self.variables["location"]["values"]:
        #     desc += f' The historic incident took place in {random_list_formater( list(map(lambda x: x.variables["str_name"]["values"], self.variables["location"]["values"])), 3, 1 )}'
        # if self.variables["participant"]["values"]:
        #     desc += f' Some of the characters and groups that took part in this event are the following: {random_list_formater( list(map(lambda x: x.variables["str_name"]["values"], self.variables["participant"]["values"])), 3, 1 )}'
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some relevant occurrences that are involved with the historic incident:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'
        
        return desc

