from ontology.classes.Entity import Entity
from ontology.classes.formating_functions import *

class Character(Entity):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'appearance' : {'values': [], 'description':'The general look of this character and any relevant details', 'type':'data', 'prop_reg': 'list'},
            'dislikes' : {'values' : [], 'description':'The topics that the character doesn\'t like to engage with', 'type':'data', 'prop_reg': 'list'},
            'likes' : {'values': [], 'description':'The topics that the character likes to engage with', 'type':'data', 'prop_reg': 'list'},
            'objective' : {'values': [], 'description':'The current goals of the character', 'type':'data', 'prop_reg': 'list'},
            'profession' : {'values': [], 'description':'The usual paid ocupation of the character (if they have any)', 'type':'data', 'prop_reg': 'list'},
            
            'leads' : {'values': [], 'description':'The group or groups that the character leads', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect':'leader'},
            
            'associated_group' : {'values': [], 'description':'A group from which the character is a memeber', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'member'},
            'child' : {'values': [], 'description':'A character who is a direct decendant from this character', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'parent'},
            'involvement' : {'values': [], 'description':'A historical incident which this character is involved with', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'participant'},
            'parent' : {'values': [], 'description':'A character who is a parent of this character.', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'child'},
            'possession' : {'values': [], 'description':'An item which is in possession of this character.', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'holder'},
            'residence' : {'values': [], 'description':'A settlement where this character usually resides.', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'citizen'},
            'sibling' : {'values': [], 'description':'A character that is a sibling of this character.', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'sibling'},
            'ubication' : {'values': [], 'description':'The current location of this character.', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'occupant'}
            
        })
