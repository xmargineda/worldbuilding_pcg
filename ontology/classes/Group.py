from ontology.classes.Entity import Entity
from ontology.classes.formating_functions import *

class Group(Entity):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'objective' : {'values': [], 'description':'What is the objective of this organization?', 'type':'data'},
            'organization' : {'values': [], 'description':'How does the group organize?', 'type':'data'},
            'leader' : {'values': [], 'description':'Who leads the group?', 'type':'entity'}
        })

    def add_objective(self, st):
        self.variables["objective"]["values"].append(st)

    def remove_objective(self, st):
        self.variables["objective"]["values"].remove(st)

    def add_organization(self, st):
        self.variables["organization"]["values"].append(st)

    def remove_organization(self, st):
        self.variables["organization"]["values"].remove(st)

    def add_leader(self, char):
        self.variables["leader"]["values"].append(char)
        if self not in char.variables["leads"]["values"]:
            char.add_leads(self)

    def remove_leader(self, char):
        self.variables["leader"]["values"].remove(char)
        if self in char.variables["leads"]["values"]:
            char.remove_leads(self)

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} objective: {self.variables["objective"]["values"]}\n organization: {self.variables["organization"]["values"]}\n leader: {list(map(lambda x: x.variables["str_name"]["values"], self.variables["leader"]["values"]))}\n'


    def short_description(self):
        desc = f'{self.variables["str_name"]["values"]} is a group of people that regurlarly work together within the story.'
        if self.variables["description"]["values"]:
            desc += f' Here\'s some information about the {self.variables["str_name"]["values"]}:\n' + random_list_formater(self.variables["description"]["values"], 2, 2)
        if self.variables["objective"]["values"]:
            if len(self.variables["objective"]["values"]) == 1:
                desc += f' The reason this group exists is the following: {self.variables["objective"]["values"][0]}.'
            else:
                desc += f' The reasons this group exists are the following: {random_list_formater(self.variables["objective"]["values"], 3, 1)}.'
        if self.variables["leader"]["values"]:
            desc += f' The group is lead by {self.variables["leader"]["values"][0].variables["str_name"]["values"]}.'
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some events that are related to the group:\n' + random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )
        # if self.organization:
        #     desc += ' The group is organized in the following way: ' + self.organization[0] + '.'
        return desc