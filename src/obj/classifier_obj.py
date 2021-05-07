from common.constants import *
from common.metaclasses import *
from common.enums import *


from obj.filters_obj import filtered_word

class filter_processor(metaclass=SingletonMeta):
    def __init__(self):
        super().__init__()
        
    def classify_word(self, word):
        # TO IMPLEMENT
        output = classified_word()
        return output

class classified_word(filtered_word):
    def __init__ (self, word, year, source, RAE, type, category, scope, composition):
        this.word = word
        this.year = year
        this.source = source
        this.RAE = RAE
        this.type = type
        this.category = set_category(category)
        this.scope = set_scope(scope)
        this.composition = set_composition(composition)
        
    def set_category(self, category):
        if category in range(1, 4):
            return word_category(category)
        else:
            return word_category.OTHER
        
    def set_scope(self, scope):
        if scope in range(1, 3):
            return word_scope(scope)
        else:
            return word_scope.OTHER
        
    def set_composition(self, composition):
        if composition in range(1, 3):
            return word_composition(composition)
        else:
            return word_composition.OTHER
        
class classifier():
    def __init__(self, discriminatory, domain, type):
        this.discriminatory = discriminatory
        this.domain = domain
        this.type = set_type(type)
        
    def set_type(self, type):
        if type in range(1, 3):
            return classifier_type(type)
        else:
            return classifier_type.OTHER
        
class category_classifier(classifier):
    def __init__(self, discriminatory, domain, type = classifier_type.CATEGORY):
        super().__init__(discriminatory, domain, type)
        
class scope_classifier(classifier):
    def __init__(self, discriminatory, domain, type = classifier_type.SCOPE):
        super().__init__(discriminatory, domain, type)
        
class composition_classifier(classifier):
    def __init__(self, discriminatory, domain, type = classifier_type.COMPOSITION):
        super().__init__(discriminatory, domain, type)
        
    