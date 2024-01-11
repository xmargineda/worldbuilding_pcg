from ontology.classes.Character import Character
from ontology.classes.formating_functions import *

class Main_Character(Character):

    def __init__(self):
        super().__init__()

    def short_description(self):
        desc =  f'{self.variables["str_name"]["values"]} is a main character within the story.'
        # if self.variables["profession"]["values"]:
        #     desc += f' {self.variables["str_name"]["values"]} works as a {random_list_formater(self.variables["profession"]["values"], 3, 1)}.'
        if self.variables["description"]["values"]:
            desc += f'{random_list_formater(self.variables["description"]["values"], 3, 3)}'
        desc += self.entity_context_gathering(3)
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some events that {self.variables["str_name"]["values"]} is involved in:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'
        
        return desc
