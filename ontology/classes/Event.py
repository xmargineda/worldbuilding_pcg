from ontology.classes.Entity import Entity
from ontology.classes.formating_functions import *

class Event(Entity):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'duration' : {'values': [], 'description':'The average length of the specified event.', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'object' : {'values': [], 'description':'The new {gen} is involved in this event.', 'type':'entity', 'gen_cont':['Item'], 'contx_expr': 'wordList', 'contx_str':' During {name}, {val} got involved.', 'prop_reg': 'reflexiveList', 'reflect': 'usage_event'}
            })
