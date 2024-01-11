from ontology.classes.Entity import Entity
from ontology.classes.formating_functions import *

class Location(Entity):    
    

    def __init__(self):
        super().__init__()
        self.variables.update({
            'appearance' : {'values': [], 'description':'The general look of this area and any relevant details', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'climate' : {'values' : [], 'description':'The kind of climate that the area has', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'fauna' : {'values': [], 'description':'The more common animals that roam the area (if any)', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'flora' : {'values': [], 'description':'The vegetation and nature that the area has (if any)', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'geography' : {'values': [], 'description':'A description of the terrain within and surrounding the area', 'type':'data', 'contx_expr': 'sentenceList', 'prop_reg': 'list'},
            'asset' : {'values': [], 'description':'An item contained within this location', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' This location keeps {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'placement'},
            'event' : {'values': [], 'description':'An event that happened or will happen in this location', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' {val} happened in this location.', 'prop_reg': 'reflexiveList', 'reflect': 'location'},
            'occupant' : {'values': [], 'description':'A character or group residing in this location.', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' Inside {name}, we can find residing, {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'ubication'},
            'subsection' : {'values': [], 'description':'A smaller subregion that is contained by this location (if there is any).', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' Within {name}, smaller locations are contanied such as {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'supersection'},
            'supersection' : {'values': [], 'description':'A larger unified region that contains this location (if there is any).', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' The location is contained within larger locations such as {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'subsection'},
            'tradition' : {'values': [], 'description':'A tradition that is regularly held in this location (if there is any).', 'type':'entity', 'contx_expr': 'wordList', 'contx_str':' This location celebrates {val}.', 'prop_reg': 'reflexiveList', 'reflect': 'venue'}
        })
