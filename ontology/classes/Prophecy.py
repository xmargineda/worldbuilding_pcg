from ontology.classes.Event import Event
from ontology.classes.formating_functions import *

class Prophecy(Event):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'origin' : {'values': [], 'description':'What is the origin of this prophecy?', 'type':'data', 'prop_reg': 'list'},
            'location' : {'values': [], 'description':'A location connected to this prophecy.', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'event'}
            })
