from ontology.classes.Location import Location
from ontology.classes.formating_functions import *

class Settlement(Location):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'economy' : {'values': [], 'description':'The main industries, the most prominent exports and/or imports...', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'demographic' : {'values': [], 'description':'Information about the demographic of population of the settlement', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'population' : {'values': [], 'description':'Number of citizens in the settlement', 'type':'data', 'contx_expr': 'singleWord', 'contx_str':' {val}.', 'prop_reg': 'list'},
            'citizen' : {'values': [], 'description':'The new {gen} is a citizen of this settlement', 'type':'entity', 'gen_cont':['NonMain_Character'], 'contx_expr': 'wordList', 'contx_str':' Some of the citizens from {name} are {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'residence'}
        })

    def short_description(self):
        desc = f'{self.variables["str_name"]["values"]} is a location within the story where a group of people live.'
        if self.variables["description"]["values"]:
            desc += f'{random_list_formater(self.variables["description"]["values"], 2, 3)}'
        desc += self.entity_context_gathering(3)
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some events that are related to {self.variables["str_name"]["values"]}:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'

        return desc
