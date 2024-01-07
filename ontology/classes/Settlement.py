from ontology.classes.Location import Location
from ontology.classes.formating_functions import *

class Settlement(Location):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'economy' : {'values': [], 'description':'The main industries, the most prominent exports and/or imports...', 'type':'data', 'prop_reg': 'list'},
            'demographic' : {'values': [], 'description':'Information about the demographic of population of the settlement', 'type':'data', 'prop_reg': 'list'},
            'population' : {'values': [], 'description':'Number of citizens in the settlement', 'type':'data', 'prop_reg': 'list'},
            'citizen' : {'values': [], 'description':'A character that is a citizen of this location', 'type':'entity', 'prop_reg': 'reflexiveList', 'reflect': 'residence'}
        })

    def short_description(self):
        desc = f'{self.variables["str_name"]["values"]} is a location within the story where a group of people live.'
        if self.variables["population"]["values"]:
            desc += f' There are {self.variables["population"]["values"][0]} living in {self.variables["str_name"]["values"]}.'
        if self.variables["description"]["values"]:
            desc += f' Here\'s some information about {self.variables["str_name"]["values"]}:\n{random_list_formater(self.variables["description"]["values"], 2, 2)}'
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some events that are related to {self.variables["str_name"]["values"]}:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'

        return desc
