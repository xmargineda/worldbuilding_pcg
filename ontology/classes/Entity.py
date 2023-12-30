from ontology.classes.Thing import Thing
from ontology.classes.formating_functions import *

class Entity(Thing):
    

    def __init__(self):
        super().__init__()
        self.variables.update({
            'isDefined' : {'values': [], 'description':'The facts that define the entity', 'type':'fact'},
            'isInvolvedIn' : {'values' : [], 'description':'The facts that the entity is involved in', 'type':'fact'}
        })

    def add_isDefined(self, df):
        self.variables["isDefined"]["values"].append(df)
        if self not in df.variables["defines"]["values"]:
            df.add_defines(self)

    def remove_isDefined(self, df):
        self.variables["isDefined"]["values"].remove(df)
        if self in df.variables["defines"]["values"]:
            df.remove_defines(self)

    def add_isInvolvedIn(self, fact):
        self.variables["isInvolvedIn"]["values"].append(fact)
        if self not in fact.variables["isRelatedTo"]["values"]:
            fact.add_isRelatedTo(self)

    def remove_isInvolvedIn(self, fact):
        self.variables["isInvolvedIn"]["values"].remove(fact)
        if self in fact.variables["isRelatedTo"]["values"]:
            fact.remove_isRelatedTo(self)

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} isDefined: {list(map(lambda x: x.variables["fact"]["values"], self.variables["isDefined"]["values"]))}\n isInvolvedIn: {list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"]))}\n'


    def short_description(self):
        desc = f'{self.variables["str_name"]["values"]} is an important element within the narrative.'
        if self.description:
            desc += f'{self.variables["str_name"]["values"]} can be described in the following ways:\n{random_list_formater(self.variables["description"]["values"], 2, 2)}'        
        if self.isInvolvedIn:
            desc += f' Here are some events that are related to {self.variables["str_name"]["values"]} :\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'

        return desc

