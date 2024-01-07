from ontology.classes.Entity import 
from ontology.classes.formating_functions import *

class Event(Entity):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'duration' : {'values': [], 'description':'The average length of the specified event.', 'type':'data', 'prop_reg': 'list'},
            'object' : {'values': [], 'description':'An item involved in this event.', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'usage_event'}
            })
