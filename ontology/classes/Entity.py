from ontology.classes.Thing import Thing
from ontology.classes.formating_functions import *

class Entity(Thing):
    

    def __init__(self):
        super().__init__()
        self.variables.update({
            'isInvolvedIn' : {'values' : [], 'description':'The facts that the entity is involved in', 'type':'fact', 'prop_reg': 'reflexiveList', 'reflect':'isRelatedTo'}
        })



    def short_description(self):
        desc = f'{self.variables["str_name"]["values"]} is an important element within the narrative.'
        if self.description:
            desc += f'{self.variables["str_name"]["values"]} can be described in the following ways:\n{random_list_formater(self.variables["description"]["values"], 2, 2)}'        
        if self.isInvolvedIn:
            desc += f' Here are some events that are related to {self.variables["str_name"]["values"]} :\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'

        return desc

