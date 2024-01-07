from ontology.classes.Event import Event
from ontology.classes.formating_functions import *

class Historic_Incident(Event):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'time_elapsed' : {'values': [], 'description':'How much time has passed since an occurance of the event.', 'type':'data', 'prop_reg': 'list'},
            'location' : {'values': [], 'description':'A location connected to this historic incident.', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'event'},
            'participant' : {'values': [], 'description':'A group or character involved in this event.', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'involvement'}
            })

