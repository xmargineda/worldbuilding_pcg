from ontology.classes.Character import Character
from ontology.classes.formating_functions import *

class Main_Character(Character):

    def __init__(self):
        super().__init__()

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str}'

    def short_description(self):
        desc =  f'{self.variables["str_name"]["values"]} is a main character within the story.'
        if self.variables["profession"]["values"]:
            desc += f' {self.variables["str_name"]["values"]} works as a {self.variables["profession"]["values"][0]}.'
        if self.variables["description"]["values"]:
            desc += f' Here\'s some information about {self.variables["str_name"]["values"]}:\n{random_list_formater(self.variables["description"]["values"], 3, 2)}'
        if self.variables["isInvolvedIn"]["values"]:
            desc += f' Here are some events that {self.variables["str_name"]["values"]} is involved in:\n{random_list_formater( list(map(lambda x: x.variables["fact"]["values"], self.variables["isInvolvedIn"]["values"])), 3, 2 )}'
        
        return desc
