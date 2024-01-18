from ontology.classes.Entity import Entity
from ontology.classes.formating_functions import *

class Group(Entity):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'objective' : {'values': [], 'description':'What is the objective of this organization?', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'organization' : {'values': [], 'description':'How does the group organize?', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'leader' : {'values': [], 'description':'The new {gen} is a leader of this group', 'type':'entity', 'gen_cont':['NonMain_Character'], 'contx_expr': 'wordList', 'contx_str':' {name} is lead by {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'leads'},
            'involvement' : {'values': [], 'description':'This group is involved in the new {gen}', 'type':'entity', 'gen_cont':['Historic_Incident'], 'contx_expr': 'wordList', 'contx_str':' The group is involved with these historical incidents: {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'participant'},
            'member' : {'values': [], 'description':'The new {gen} is a member of this group.', 'type':'entity', 'gen_cont':['NonMain_Character'], 'contx_expr': 'wordList', 'contx_str':' Some of the members of this group are the following: {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'associated_group'},
            'possession' : {'values': [], 'description':'The new {gen} is in possession of this group.', 'type':'entity', 'gen_cont':['Item'], 'contx_expr': 'wordList', 'contx_str':' {name} is in possesion of {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'holder'},
            'ubication' : {'values': [], 'description':'This group is currently located in the new {gen}.', 'type':'entity', 'gen_cont':['Settlement','Place'], 'contx_expr': 'wordList', 'contx_str':' {name} are set in the following locations: {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'occupant'}
        })


    def short_description(self):
        desc = f'{self.variables["str_name"]["values"]} is a group of people that regurlarly work together within the story.'
        if self.variables["description"]["values"]:
            desc += f'{random_list_formater(self.variables["description"]["values"], 2, 3)}'
        desc += self.entity_context_gathering(3)
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some events that are related to the group:\n' + random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )
        return desc