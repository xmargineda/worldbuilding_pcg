from ontology.classes.formating_functions import *

class Thing:

    variables = {
        'str_name' : {'values': '', 'type':'data', 'prop_reg': 'functional'},
        'description' : {'values' : [], 'description':'The defining caracteristics of the entity', 'type':'data', 'prop_reg': 'list'},
        'onto_instance' : {'values': None, 'type':'none', 'prop_reg': 'functional'}
    }
    
    def __init__(self):
        self.variables = {
        'str_name' : {'values': '', 'type':'data', 'prop_reg': 'functional'},
        'description' : {'values' : [], 'description':'The defining caracteristics of the entity', 'type':'data', 'prop_reg': 'list'},
        'onto_instance' : {'values': None, 'type':'none', 'prop_reg': 'functional'}
    }

    def __str__(self):
        st = ''
        for v in self.variables:
            if v not in ['str_name','description'] and self.variables[v]['values'] not in [ [], None, '' ]:
                match self.variables[v]['type']:
                    case 'data':
                        st += f' {v}: {self.variables[v]["values"]}\n'
                    case 'entity':
                        st += f' {v}: {list(map(lambda x: x.variables["str_name"]["values"], self.variables[v]["values"]))}\n'
                    case 'fact':
                        st += f' {v}: {list(map(lambda x: x.variables["fact"]["values"], self.variables[v]["values"]))}\n'
                    case 'chapt':
                        st += f' {v}: {list(map(lambda x: x.variables["str_name"]["values"], self.variables[v]["values"]))}\n'
                    case _:
                        pass

        return f' str_name: {self.variables["str_name"]["values"]}\n description: {self.variables["description"]["values"]}\n{st}'

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

    def add_attribute(self, atr, val):
        if atr in self.variables:
            match self.variables[atr]["prop_reg"]:
                case "functional":
                    self.variables[atr]["values"] = val
                case "list":
                    if val not in self.variables[atr]["values"]:
                        self.variables[atr]["values"].append(val)
                case "reflexiveList":
                    if val not in self.variables[atr]["values"]:
                        self.variables[atr]["values"].append(val)
                        val.add_attribute(self.variables[atr]['reflect'], self)

    def remove_attribute(self, atr, val):
        if atr in self.variables:
            match self.variables[atr]["prop_reg"]:
                case "functional":
                    self.variables[atr]["values"] = None
                case "list":
                    if val in self.variables[atr]["values"]:
                        self.variables[atr]["values"].remove(val)
                case "reflexiveList":
                    if val in self.variables[atr]["values"]:
                        self.variables[atr]["values"].remove(val)
                        val.remove_attribute(self.variables[atr]['reflect'], self)
