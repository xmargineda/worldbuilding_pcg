from ontology.classes.Entity import Event
from ontology.classes.formating_functions import *

class Event(Entity):

    def __init__(self):
        super().__init__()
    
    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str}'

