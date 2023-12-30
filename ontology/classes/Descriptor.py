from ontology.classes.Fact import Fact
from ontology.classes.formating_functions import *

class Descriptor(Fact):
    

    def __init__(self):
        super().__init__()
        self.variables.update({
            'defines' : {'values': []}
        })

    def add_defines(self, ent):
        self.variables["defines"]["values"].append(ent)
        if self not in ent.variables["isDefined"]["values"]:
            ent.add_isDefined(self)

    def remove_defines(self, ent):
        self.variables["defines"]["values"].remove(ent)
        if self in ent.variables["isDefined"]["values"]:
            ent.remove_isDefined(self)

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} defines: {list(map(lambda x: x.variables["str_name"]["values"], self.variables["defines"]["values"]))}\n'
