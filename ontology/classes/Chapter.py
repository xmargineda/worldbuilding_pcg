from ontology.classes.Thing import Thing
from ontology.classes.formating_functions import *

class Chapter(Thing):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'contains' : {'values': [], 'type':'fact', 'prop_reg': 'reflexiveList', 'reflect':'isContainedBy'},
            'nextChapter' : {'values' : [], 'type':'chapt', 'prop_reg': 'reflexiveList', 'reflect':'prevChapter'},
            'prevChapter' : {'values': [], 'type':'chapt', 'prop_reg': 'reflexiveList', 'reflect':'nextChapter'}
        })

