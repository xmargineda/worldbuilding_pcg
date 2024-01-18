from ontology.classes.Event import Event
from ontology.classes.formating_functions import *

class Historic_Incident(Event):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'time_elapsed' : {'values': [], 'description':'How much time has passed since an occurance of the event.', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'location' : {'values': [], 'description':'This historic incident took place in the new {gen}.', 'type':'entity', 'gen_cont':['Location','Settlement','Place'], 'contx_expr': 'wordList', 'contx_str':' The event took place in {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'event'},
            'participant' : {'values': [], 'description':'The new {gen} is involved in this historic event.', 'type':'entity', 'gen_cont':['Group','NonMain_Character'], 'contx_expr': 'wordList', 'contx_str':' {name} had {val} as partticipants.', 'prop_reg': 'reflexiveList', 'reflect': 'involvement'}
            })

    def short_description(self):
        desc =  f'{self.variables["str_name"]["values"]} is a historic incident within the story.'
        if self.variables["description"]["values"]:
            desc += f'{random_list_formater(self.variables["description"]["values"], 3, 3)}'
        desc += self.entity_context_gathering(3)
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some relevant occurrences that are involved with the historic incident:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'
        
        return desc

