from ontology.classes.Fact import Fact
from ontology.classes.formating_functions import *

class Action(Fact):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'nextAction' : {'values': []},
            'prevAction' : {'values': []}
        })


    def add_nextAction(self, action):
        self.variables["nextAction"]["values"].append(action)
        if self not in action.variables["prevAction"]["values"]:
            action.add_prevAction(self)

    def remove_nextAction(self, action):
        self.variables["nextAction"]["values"].remove(action)
        if self in action.variables["prevAction"]["values"]:
            action.remove_prevAction(self)

    def add_prevAction(self, action):
        self.variables["prevAction"]["values"].append(action)
        if self not in action.variables["nextAction"]["values"]:
            action.add_nextAction(self)

    def remove_prevAction(self, action):
        self.variables["prevAction"]["values"].remove(action)
        if self in action.variables["nextAction"]["values"]:
            action.remove_nextAction(self)

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} nextAction: {list(map(lambda x: x.variables["fact"]["values"], self.variables["nextAction"]["values"]))}\n prevAction: {list(map(lambda x: x.variables["fact"]["values"], self.variables["prevAction"]["values"]))}\n'