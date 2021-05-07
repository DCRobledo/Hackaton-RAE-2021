from enum import Enum

class text_scope(Enum):
    ENERGY = 1
    ENVIRONMENT = 2
    OTHER = 3
    
class word_type(Enum):
    NOUN = 1
    PRONOUN = 2
    VERB = 3
    ADJECTIVE = 4
    ADVERB = 5
    PREPOSITION = 6
    CONJUNCTION = 7
    INTERJECTION = 8
    OTHER = 9
    
class word_category(Enum):
    NEOLOGISM = 1
    TECHNICISM = 2
    FOREIGN_WORD = 3
    OTHER = 4
    
class word_scope(Enum):
    ENERGY = 1
    ENVIRONMENT = 2
    OTHER = 3
    
class word_composition(Enum):
    DERIVATIVE = 1
    COMPOUND = 2
    OTHER = 3
    
class classifier_type(Enum):
    CATEGORY = 1
    SCOPE = 2
    COMPOSITION = 3
    OTHER = 4
    
class analyzer_goal(Enum):
    FRECUENCY = 1
    TECHNICISMS = 2
    FOREIGN_WORDS = 3
    MOST_FRECUENT_TYPE = 4
    DEFINITION = 5
    OTHER = 6
    
class tuple_type(Enum):
    FRECUENCY = 1
    TECHNICISMS = 2
    FOREIGN_WORDS = 3
    MOST_FRECUENT_TYPE = 4
    DEFINITION = 5
    OTHER = 6
    
class graphic_type(Enum):
    TABLE = 1
    GRAPH = 2
    OTHER = 3
    
class graph_type(Enum):
    BAR = 1
    LINEAR = 2
    OTHER = 3
    
