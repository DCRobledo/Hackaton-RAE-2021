from common.constants import *
from common.metaclasses import *
from common.enums import *

from obj.composer_obj import word_group

class analitics_processor(metaclass=SingletonMeta):
    def __init__(self):
        super().__init__()
        
    def analyze_group(self, word_group, subanalyzer):
        # TO IMPLEMENT
        output = conclusion(word_group)
        return output
    
    
class conclusion:
    def __init__(self, type):
        this.type = set_type(type)
        
    def set_type(self, type):
        if type in range(1, 5):
            return tuple_type(type)
        else:
            return tuple_type.OTHER   
        
class tuple_frecuency(conclusion):
    def __init__(self, average, type = tuple_type.FRECUENCY):
        this.average = average
        this.type = type
        
class subtuple_frecuency:
    def __init__(self, word, type, frecuency, rank):
        this.word = word
        this.type = set_type(type)
        this.frecuency = frecuency
        this.rank = rank
    
    def set_type(self, type):
        if type in range(1, 8):
            return word_type(type)
        else:
            return word_type.OTHER
        
        
class tuple_technicisms(conclusion):
    def __init__(self, word, type = tuple_type.TECHNICISMS):
        this.word = word
        this.type = type
        
class subtuple_technicisms:
    def __init__(self, year, frecuency):
        this.year = year
        this.frecuency = frecuency
        
    
class tuple_foreign_words(conclusion):
    def __init__(self, word, alternative, type = tuple_type.FOREIGN_WORDS):
        this.word = word
        this.alternative = alternative
        this.type = type
        
        
class tuple_most_frecuent_type(conclusion):
    def __init__(self, type = tuple_type.MOST_FRECUENT_TYPE):
        this.type = type
        
class subtuple_most_frecuent_type:
    def __init__(self, type, frecuency):
        this.type = set_type(type)
        this.frecuency = frecuency
    
    def set_type(self, type):
        if type in range(1, 8):
            return word_type(type)
        else:
            return word_type.OTHER
        
    
class tuple_definition(conclusion):
    def __init__(self, word, definition, type = tuple_type.DEFINITION):
        this.word = word
        this.definition = definition
        this.type = type
        
    
        
    
    
class subanalyzer:
    def __init__(self, goal):
        this.goal = set_goal(goal)
        
    def set_goal(self, goal):
        if type in range(1, 5):
            return analyzer_goal(goal)
        else:
            return analyzer_goal.OTHER
        
    def form_conclusion(self, word_group):
        pass
    
class frecuency_analyzer(subanalyzer):
    def __init__(self, goal = analyzer_goal.FRECUENCY):
        super().__init__(goal)
    
    def form_conclusion(self, word_group):
        # TO IMPLEMENT
        output = conclusion(tuple_type.FRECUENCY)
        return output
    
class technicisms_analyzer(subanalyzer):
    def __init__(self, goal = analyzer_goal.TECHNICISMS):
        super().__init__(goal)
    
    def form_conclusion(self, word_group):
        # TO IMPLEMENT
        output = conclusion(tuple_type.TECHNICISMS)
        return output
    
class foreign_words_analyzer(subanalyzer):
    def __init__(self, goal = analyzer_goal.FOREIGN_WORDS):
        super().__init__(goal)
    
    def form_conclusion(self, word_group):
        # TO IMPLEMENT
        output = conclusion(tuple_type.FOREIGN_WORDS)
        return output
    
class most_frequent_type_analyzer(subanalyzer):
    def __init__(self, goal = analyzer_goal.MOST_FRECUENT_TYPE):
        super().__init__(goal)
    
    def form_conclusion(self, word_group):
        # TO IMPLEMENT
        output = conclusion(tuple_type.MOST_FRECUENT_TYPE)
        return output
    
class definition_analyzer(subanalyzer):
    def __init__(self, goal = analyzer_goal.DEFINITION):
        super().__init__(goal)
    
    def form_conclusion(self, word_group):
        # TO IMPLEMENT
        output = conclusion(tuple_type.DEFINITION)
        return output