from ontology.classes.Thing import Thing
from ontology.classes.formating_functions import *

class Chapter(Thing):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'contains' : {'values': []},
            'nextChapter' : {'values' : []},
            'prevChapter' : {'values': []}
        })

    def add_nextChapter(self, chapt):
        self.variables["nextChapter"]["values"].append(chapt)
        if self not in chapt.variables["prevChapter"]["values"]:
            chapt.add_prevChapter(self)

    def remove_nextChapter(self, chapt):
        self.variables["nextChapter"]["values"].remove(chapt)
        if self in chapt.variables["prevChapter"]["values"]:
            chapt.remove_prevChapter(self)

    def add_prevChapter(self, chapt):
        self.variables["prevChapter"]["values"].append(chapt)
        if self not in chapt.variables["nextChapter"]["values"]:
            chapt.add_nextChapter(self)

    def remove_prevChapter(self, chapt):
        self.variables["prevChapter"]["values"].remove(chapt)
        if self in chapt.variables["nextChapter"]["values"]:
            chapt.remove_nextChapter(self)

    def add_contains(self, fact):
        self.variables["contains"]["values"].append(fact)
        if self not in fact.variables["isContainedBy"]["values"]:
            fact.add_isContainedBy(self)

    def remove_contains(self, fact):
        self.variables["contains"]["values"].remove(fact)
        if self in fact.variables["isContainedBy"]["values"]:
            fact.remove_isContainedBy(self)

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} contains: {list(map(lambda x: x.variables["fact"]["values"], self.variables["contains"]["values"]))}\n nextChapter: {list(map(lambda x: x.variables["str_name"]["values"], self.variables["nextChapter"]["values"]))}\n prevChapter: {list(map(lambda x: x.variables["str_name"]["values"], self.variables["prevChapter"]["values"]))}\n'