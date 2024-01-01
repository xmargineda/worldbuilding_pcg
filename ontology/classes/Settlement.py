from ontology.classes.Location import Location
from ontology.classes.formating_functions import *

class Settlement(Location):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'economy' : {'values': [], 'description':'The main industries, the most prominent exports and/or imports...', 'type':'data'},
            'demographic' : {'values': [], 'description':'Information about the demographic of population of the settlement', 'type':'data'},
            'population' : {'values': [], 'description':'Number of citizens in the settlement', 'type':'data'}
        })

    def add_economy(self, st):
        self.variables["economy"]["values"].append(st)

    def remove_economy(self, st):
        self.variables["economy"]["values"].remove(st)

    def add_population(self, st):
        self.variables["population"]["values"].append(st)

    def remove_population(self, st):
        self.variables["population"]["values"].remove(st)

    def add_demographic(self, n):
        self.variables["demographic"]["values"] = n

    def remove_demographic(self):
        self.variables["demographic"]["values"] = None

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} economy: {self.variables["economy"]["values"]}\n population: {self.variables["population"]["values"]}\n'

    def short_description(self):
        desc = f'{self.variables["str_name"]["values"]} is a location within the story where a group of people live.'
        if self.variables["population"]["values"]:
            desc += f' There are {self.variables["population"]["values"][0]} living in {self.variables["str_name"]["values"]}.'
        if self.variables["description"]["values"]:
            desc += f' Here\'s some information about {self.variables["str_name"]["values"]}:\n{random_list_formater(self.variables["description"]["values"], 2, 2)}'
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some events that are related to {self.variables["str_name"]["values"]}:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'

        return desc
