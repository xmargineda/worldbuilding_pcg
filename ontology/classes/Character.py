from ontology.classes.Entity import Entity
from ontology.classes.formating_functions import *

class Character(Entity):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'appearance' : {'values': [], 'description':'The general look of this character and any relevant details', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'dislikes' : {'values' : [], 'description':'The topics that the character doesn\'t like to engage with', 'type':'data', 'contx_expr': 'wordList', 'contx_str':' Some of the likes of this character are {val}.', 'prop_reg': 'list'},
            'likes' : {'values': [], 'description':'The topics that the character likes to engage with', 'type':'data', 'contx_expr': 'wordList', 'contx_str':' Some of the dislikes of this character are {val}.', 'prop_reg': 'list'},
            'objective' : {'values': [], 'description':'The current goals of the character', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'profession' : {'values': [], 'description':'The usual paid ocupation of the character (if they have any)', 'type':'data', 'contx_expr': 'wordList', 'contx_str':' {name} works as a {val}.', 'prop_reg': 'list'},
            
            'leads' : {'values': [], 'description':'The group or groups that the character leads', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' {name} leads {val}.', 'prop_reg': 'reflexiveList', 'reflect':'leader'},
            
            'associated_group' : {'values': [], 'description':'A group from which the character is a memeber', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' {name} is a member of {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'member'},
            'child' : {'values': [], 'description':'A character who is a direct decendant from this character', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' The character is the parent of {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'parent'},
            'involvement' : {'values': [], 'description':'A historical incident which this character is involved with', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' The character has been involved in {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'participant'},
            'parent' : {'values': [], 'description':'A character who is a parent of this character.', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' {name} is a child of {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'child'},
            'possession' : {'values': [], 'description':'An item which is in possession of this character.', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' {name} is in possesion of {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'holder'},
            'residence' : {'values': [], 'description':'A settlement where this character usually resides.', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' The character usually resides in {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'citizen'},
            'sibling' : {'values': [], 'description':'A character that is a sibling of this character.', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' The character is the sibiling of {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'sibling'},
            'ubication' : {'values': [], 'description':'The current location of this character.', 'type':'entity',  'contx_expr': 'singleWord', 'contx_str':' {name} is currently in {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'occupant'}
            
        })
