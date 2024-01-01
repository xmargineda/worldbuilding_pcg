from ontology.classes.Thing import Thing
from ontology.classes.formating_functions import *

class Fact(Thing):
    
    def __init__(self):
        super().__init__()
        self.variables.update({
            
            
        })
        

    

    

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str}'