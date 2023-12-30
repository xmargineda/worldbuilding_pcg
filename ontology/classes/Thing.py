from ontology.classes.formating_functions import *

class Thing:

    variables = {
        'str_name' : {'values': ''},
        'description' : {'values' : [], 'description':'The defining caracteristics of the entity', 'type':'data'},
        'onto_instance' : {'values': None}
    }
    
    def __init__(self):
        self.variables = {
        'str_name' : {'values': ''},
        'description' : {'values' : []},
        'onto_instance' : {'values': None}
    }

    def add_str_name(self, st):
        self.variables["str_name"]["values"] = st

    def remove_str_name(self):
        self.variables["str_name"]["values"] = ''

    def add_description(self, st):
        self.variables["description"]["values"].append(st)

    def remove_description(self, st):
        self.variables["description"]["values"].remove(st)

    def __str__(self):
        return f' str_name: {self.variables["str_name"]["values"]}\n description: {self.variables["description"]["values"]}\n'

    def attribute_description(self, atr):
        if atr in self.variables and 'description' in self.variables[atr]:
            return self.variables[atr]['description']
        else:
            return None

    def attribute_type(self, atr):
        if atr in self.variables and 'type' in self.variables[atr]:
            return self.variables[atr]['type']
        else:
            return None