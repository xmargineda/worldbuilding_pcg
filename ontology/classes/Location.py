from ontology.classes.Entity import Entity
from ontology.classes.formating_functions import *

class Location(Entity):    
    

    def __init__(self):
        super().__init__()
        self.variables.update({
            'appearance' : {'values': [], 'description':'The general look of this area and any relevant details', 'type':'data'},
            'climate' : {'values' : [], 'description':'The kind of climate that the area has', 'type':'data'},
            'fauna' : {'values': [], 'description':'The more common animals that roam the area (if any)', 'type':'data'},
            'flora' : {'values': [], 'description':'The vegetation and nature that the area has (if any)', 'type':'data'},
            'geography' : {'values': [], 'description':'A description of the terrain within and surrounding the area', 'type':'data'}
        })

    def add_appearance(self, st):
        self.variables["appearance"]["values"].append(st)

    def remove_appearance(self, st):
        self.variables["appearance"]["values"].remove(st)

    def add_climate(self, st):
        self.variables["climate"]["values"].append(st)

    def remove_climate(self, st):
        self.variables["climate"]["values"].remove(st)

    def add_fauna(self, st):
        self.variables["fauna"]["values"].append(st)

    def remove_fauna(self, st):
        self.variables["fauna"]["values"].remove(st)

    def add_flora(self, st):
        self.variables["flora"]["values"].append(st)

    def remove_flora(self, st):
        self.variables["flora"]["values"].remove(st)

    def add_geography(self, st):
        self.variables["geography"]["values"].append(st)

    def remove_geography(self, st):
        self.variables["geography"]["values"].remove(st)

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str} appearance: {self.variables["appearance"]["values"]}\n climate: {self.variables["climate"]["values"]}\n fauna: {self.variables["fauna"]["values"]}\n flora: {self.variables["flora"]["values"]}\n geography: {self.variables["geography"]["values"]}\n'