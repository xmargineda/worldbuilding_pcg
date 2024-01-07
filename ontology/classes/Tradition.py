from ontology.classes.Event import Event
from ontology.classes.formating_functions import *

class Tradition(Event):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'frequency' : {'values': [], 'description':'The amount of time passed between each iteration of the tradition.', 'type':'data', 'prop_reg': 'list'},
            'origin' : {'values': [], 'description':'What is the supposed origin of this tradition?', 'type':'data', 'prop_reg': 'list'},
            'rituals' : {'values': [], 'description':'What are the rituals and customs involved in this tradition? (if there are any)', 'type':'data', 'prop_reg': 'list'},
            'venue' : {'values': [], 'description':'A location where this tradition is celebrated.', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'tradition'}
            })
