from ontology.classes.Thing import Thing
from ontology.classes.formating_functions import *

class Action(Thing):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'fact' : {'values': '', 'type':'data', 'prop_reg': 'functional'},
            'nextAction' : {'values': [], 'type':'fact', 'prop_reg': 'reflexiveList', 'reflect':'prevAction'},
            'prevAction' : {'values': [], 'type':'fact', 'prop_reg': 'reflexiveList', 'reflect':'nextAction'},
            'isContainedBy' : {'values': [], 'type':'chapt', 'prop_reg': 'reflexiveList', 'reflect':'contains'},
            'isRelatedTo' : {'values': [], 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect':'isInvolvedIn'}
        })
