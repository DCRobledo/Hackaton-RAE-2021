from common.constants import *
from common.metaclasses import *
from common.enums import *
from common.store import *

class composer_processor(metaclass=SingletonMeta):
    def __init__(self):
        super().__init__()
        
    def form_group(self, classified_word):
        word_group.AtEnd(classified_word)
        
    def get_group(self):
        return word_group
    
class word_group(linked_list):
    def __init__(self):
        super().__init__()