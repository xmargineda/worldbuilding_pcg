from ontology.classes.Entity import Entity
from ontology.classes.formating_functions import *

class Group(Entity):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'objective' : {'values': [], 'description':'What is the objective of this organization?', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'organization' : {'values': [], 'description':'How does the group organize?', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'leader' : {'values': [], 'description':'Who leads the group?', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' {name} is lead by {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'leads'},
            'involvement' : {'values': [], 'description':'A historical incident which this group is involved with', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' The group is involved with these historical incidents: {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'participant'},
            'member' : {'values': [], 'description':'A character that is a member of the group.', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' Some of the members of this group are the following: {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'associated_group'},
            'possession' : {'values': [], 'description':'An item which is in possession of this group.', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' {name} is in possesion of {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'holder'},
            'ubication' : {'values': [], 'description':'The current location of this group.', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' {name} are set in the following locations: {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'occupant'}
        })


    def short_description(self):
        desc = f'{self.variables["str_name"]["values"]} is a group of people that regurlarly work together within the story.'
        if self.variables["description"]["values"]:
            desc += f'{random_list_formater(self.variables["description"]["values"], 2, 3)}'
        desc += self.entity_context_gathering(3)
        # if self.variables["objective"]["values"]:
        #     desc += f'{random_list_formater( self.variables["objective"]["values"], 3, 3 )}'
        #     # if len(self.variables["objective"]["values"]) == 1:
        #     #     desc += f' The reason this group exists is the following: {self.variables["objective"]["values"][0]}.'
        #     # else:
        #     #     desc += f' The reasons this group exists are the following: {random_list_formater(self.variables["objective"]["values"], 3, 1)}.'
        # if self.variables["leader"]["values"]:
        #     desc += f' The group is lead by {random_list_formater( list(map(lambda x: x.variables["str_name"]["values"], self.variables["leader"]["values"])), 3, 1 )}.'
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some events that are related to the group:\n' + random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )
        # if self.organization:
        #     desc += ' The group is organized in the following way: ' + self.organization[0] + '.'
        return desc