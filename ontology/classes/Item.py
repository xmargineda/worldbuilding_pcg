from ontology.classes.Entity import Entity
from ontology.classes.formating_functions import *

class Item(Entity):
    
    def __init__(self):
        super().__init__()
        self.variables.update({
            'appearance' : {'values': [], 'description':'The look of this item and any relevant details', 'type':'data'},
            'material' : {'values': [], 'description':'The materials it is made of', 'type':'data'},
            'use' : {'values': [], 'description':'What are the different ways this item can be used', 'type':'data'},
            'value' : {'values': [], 'description':'Why is this item relevant within the story', 'type':'data'}
        })

    def add_appearance(self, st):
        self.variables["appearance"]["values"].append(st)

    def remove_appearance(self, st):
        self.variables["appearance"]["values"].remove(st)

    def add_material(self, st):
        self.variables["material"]["values"].append(st)

    def remove_material(self, st):
        self.variables["material"]["values"].remove(st)

    def add_use(self, st):
        self.variables["use"]["values"].append(st)

    def remove_use(self, st):
        self.variables["use"]["values"].remove(st)

    def add_value(self, st):
        self.variables["value"]["values"].append(st)

    def remove_value(self, st):
        self.variables["value"]["values"].remove(st)

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} appearance: {self.variables["appearance"]["values"]}\n material: {self.variables["material"]["values"]}\n use: {self.variables["use"]["values"]}\n value: {self.variables["value"]["values"]}\n'

    def short_description(self):
        desc = f'{self.variables["str_name"]["values"]} is an object of importance within the story.'
        if self.variables["description"]["values"]:
            desc += f' Here\'s some information about {self.variables["str_name"]["values"]}:\n{random_list_formater(self.variables["description"]["values"], 2, 2)}'         
        if self.variables["use"]["values"]:
            desc += f' The item can be used in one of the following ways: {random_list_formater(self.variables["use"]["values"], 3, 1)}.'
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some events that are related to the object:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'

        return desc