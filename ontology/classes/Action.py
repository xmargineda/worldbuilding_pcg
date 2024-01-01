from ontology.classes.Thing import Thing
from ontology.classes.formating_functions import *

class Action(Thing):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'fact' : {'values': ''},
            'nextAction' : {'values': []},
            'prevAction' : {'values': []},
            'isContainedBy' : {'values': []},
            'isRelatedTo' : {'values': []}
        })

    def add_fact(self, st):
        self.variables["fact"]["values"] = st

    def remove_fact():
        self.variables["fact"]["values"] = ''

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


    def add_isContainedBy(self, chapt):
        self.variables["isContainedBy"]["values"].append(chapt)
        if self not in chapt.variables["contains"]["values"]:
            chapt.add_contains(self)

    def remove_isContainedBy(self, chapt):
        self.variables["isContainedBy"]["values"].remove(chapt)
        if self in chapt.variables["contains"]["values"]:
            chapt.remove_contains(self)

    def add_isRelatedTo(self, ent):
        self.variables["isRelatedTo"]["values"].append(ent)
        if self not in ent.variables["isInvolvedIn"]["values"]:
            ent.add_isInvolvedIn(self)

    def remove_isRelatedTo(self, ent):
        self.variables["isRelatedTo"]["values"].remove(ent)
        if self in ent.variables["isInvolvedIn"]["values"]:
            ent.remove_isInvolvedIn(self)

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} fact: {self.variables["fact"]["values"]}\n isContainedBy: {list(map(lambda x: x.variables["str_name"]["values"], self.variables["isContainedBy"]["values"]))}\n isRelatedTo: {list(map(lambda x: x.variables["str_name"]["values"], self.variables["isRelatedTo"]["values"]))}\n nextAction: {list(map(lambda x: x.variables["fact"]["values"], self.variables["nextAction"]["values"]))}\n prevAction: {list(map(lambda x: x.variables["fact"]["values"], self.variables["prevAction"]["values"]))}\n'