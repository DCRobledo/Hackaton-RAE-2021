from common.constants import *
from common.metaclasses import *
from common.enums import *

from obj.input_process_obj import word

class filter_processor(metaclass=SingletonMeta):
    def __init__(self):
        super().__init__()
        
    def filter_word(self, word):
        # TO IMPLEMENT
        output = filtered_word()
        return output

class filtered_word(word):
    def __init__ (self, word, year, source, RAE, type):
        this.word = word
        this.year = year
        this.source = source
        this.RAE = RAE
        this.type = set_type(type)
    
    def set_type(self, type):
        if type in range(1, 8):
            return word_type(type)
        else:
            return word_type.OTHER