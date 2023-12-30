from ontology.classes.Entity import Entity
from ontology.classes.formating_functions import *

class Character(Entity):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'appearance' : {'values': [], 'description':'The general look of this character and any relevant details', 'type':'data'},
            'dislikes' : {'values' : [], 'description':'The topics that the character doesn\'t like to engage with', 'type':'data'},
            'likes' : {'values': [], 'description':'The topics that the character likes to engage with', 'type':'data'},
            'objective' : {'values': [], 'description':'The current goals of the character', 'type':'data'},
            'profession' : {'values': [], 'description':'The usual paid ocupation of the character (if they have any)', 'type':'data'},
            'leads' : {'values': [], 'description':'The group or groups that the character leads', 'type':'entity'}
        })


    def add_appearance(self, st):
        self.variables["appearance"]["values"].append(st)

    def remove_appearance(self, st):
        self.variables["appearance"]["values"].remove(st)

    def add_dislikes(self, st):
        self.variables["dislikes"]["values"].append(st)

    def remove_dislikes(self, st):
        self.variables["dislikes"]["values"].remove(st)

    def add_likes(self, st):
        self.variables["likes"]["values"].append(st)

    def remove_likes(self, st):
        self.variables["likes"]["values"].remove(st)

    def add_objective(self, st):
        self.variables["objective"]["values"].append(st)

    def remove_objective(self, st):
        self.variables["objective"]["values"].remove(st)

    def add_profession(self, st):
        self.variables["profession"]["values"].append(st)

    def remove_profession(self, st):
        self.variables["profession"]["values"].remove(st)

    def add_leads(self, gr):
        self.variables["leads"]["values"].append(gr)
        if self not in gr.variables["leader"]["values"]:
            gr.add_leader(self)

    def remove_leads(self, gr):
        self.variables["leads"]["values"].remove(gr)
        if self in gr.variables["leader"]["values"]:
            gr.remove_leader(self)

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} appearance: {self.variables["appearance"]["values"]}\n dislikes: {self.variables["dislikes"]["values"]}\n likes: {self.variables["likes"]["values"]}\n objective: {self.variables["objective"]["values"]}\n profession: {self.variables["profession"]["values"]}\n leads: {list(map(lambda x: x.variables["str_name"]["values"], self.variables["leads"]["values"]))}\n'
