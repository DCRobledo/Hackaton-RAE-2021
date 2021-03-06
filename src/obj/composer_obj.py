from src.common.constants import *
from src.common.metaclasses import *
from src.common.enums import *
from src.common.store import *

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