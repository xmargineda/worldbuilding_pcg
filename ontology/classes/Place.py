from ontology.classes.Location import Location
from ontology.classes.formating_functions import *

class Place(Location):

    def __init__(self):
        super().__init__()
        self.variables.update({
            'value' : {'values': [], 'description':'Why is the location special within the narrative', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'}
        })

    def short_description(self):
        desc = f'{self.variables["str_name"]["values"]} is a place within the story with some kind of relevance.'
        # if self.variables["value"]["values"]:
        #     desc += f'{random_list_formater(self.variables["value"]["values"], 3, 3)}'
        if self.variables["description"]["values"]:
            desc += f'{random_list_formater(self.variables["description"]["values"], 2, 3)}'
        desc += self.entity_context_gathering(3)
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some events that are related to {self.variables["str_name"]["values"]}:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'
        
        return desc
