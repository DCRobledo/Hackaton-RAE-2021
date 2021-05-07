from common.constants import *
from common.metaclasses import *
from common.enums import *

class input_processor(metaclass=SingletonMeta):
    def __init__(self):
        super().__init__()
        
    def process_input(self, input):
        # TO IMPLEMENT
        output = word()
        return output

class text_source:
    def __init__(self, fd, year, scope):
        this.fd = fd
        this.year = year
        this.scope = set_scope(scope)
        
    def set_scope(self, scope):
        if scope in range(1, 3):
            return text_scope(scope)
        else:
            return text_scope.OTHER
            
class word:
    def __init__ (self, word, year, source, RAE):
        this.word = word
        this.year = year
        this.source = source
        this.RAE = RAE