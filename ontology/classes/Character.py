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
            'profession' : {'values': [], 'description':'The usual paid occupation of the character (if they have any)', 'type':'data', 'contx_expr': 'wordList', 'contx_str':' {name} works as a {val}.', 'prop_reg': 'list'},
            
            'leads' : {'values': [], 'description':'The character is a leader of the new {gen}.', 'type':'entity', 'gen_cont':['Group'], 'contx_expr': 'wordList', 'contx_str':' {name} leads {val}.', 'prop_reg': 'reflexiveList', 'reflect':'leader'},
            
            'associated_group' : {'values': [], 'description':'The character is a member of the new {gen}.', 'type':'entity', 'gen_cont':['Group'], 'contx_expr': 'wordList', 'contx_str':' {name} is a member of {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'member'},
            'child' : {'values': [], 'description':'The character is a parent of the new {gen}.', 'type':'entity', 'gen_cont':['NonMain_Character'], 'contx_expr': 'wordList', 'contx_str':' The character is the parent of {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'parent'},
            'involvement' : {'values': [], 'description':'The character is involved with the {gen}.', 'type':'entity', 'gen_cont':['Historic_Incident'], 'contx_expr': 'wordList', 'contx_str':' The character has been involved in {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'participant'},
            'parent' : {'values': [], 'description':'The character a direct decendant of the new {gen}.', 'type':'entity', 'gen_cont':['NonMain_Character'], 'contx_expr': 'wordList', 'contx_str':' {name} is a child of {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'child'},
            'possession' : {'values': [], 'description':'The character is in direct possesion of the new {gen}.', 'type':'entity', 'gen_cont':['Item'], 'contx_expr': 'wordList', 'contx_str':' {name} is in possesion of {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'holder'},
            'residence' : {'values': [], 'description':'The character usually resides in the new {gen}.', 'type':'entity', 'gen_cont':['Settlement'], 'contx_expr': 'wordList', 'contx_str':' The character usually resides in {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'citizen'},
            'sibling' : {'values': [], 'description':'The character is a sibling of the new {gen}.', 'type':'entity', 'gen_cont':['NonMain_Character'], 'contx_expr': 'wordList', 'contx_str':' The character is the sibiling of {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'sibling'},
            'ubication' : {'values': [], 'description':'The character is currently in the new {gen}.', 'type':'entity', 'gen_cont':['Settlement','Place'],  'contx_expr': 'singleWord', 'contx_str':' {name} is currently in {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'occupant'}
        })
