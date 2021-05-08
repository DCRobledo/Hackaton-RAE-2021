from src.common.constants import *
from src.common.metaclasses import *
from src.common.enums import *

class output_processor(metaclass=SingletonMeta):
    def __init__(self):
        super().__init__()
        
    def process_output(self, output):
        # TO IMPLEMENT
        output = graphic()
        return output
    
class graphic:
    def __init__(self, conclusion, type):
        this.type = set_type(type)
        this.conclusion = conclusion
        
    def set_type(self, type):
        if type in range (1, 3):
            return graph_type(type)
        else:
            return graphic_type.OTHER
        
class table(graphic):
    def __init__(self, conclusion, type = graphic_type.TABLE):
        super().__init__(conclusion, type)
        
    def form_table(self, conclusion = this.conclusion):
        # TO IMPLEMENT
        pass
    
class graph(graphic):
    def __init__(self, graph_type, conclusion, type = graphic_type.GRAPH):
        super().__init__(conclusion, type)
        this.graph_type = graph_type
        
    def form_graph(self, graph_type, conclusion = this.conclusion):
        pass
    
class bar_graph(graph):
    def __init__(self, conclusion, type, graph_type = graph_type.BAR):
        super().__init__(graph_type, conclusion, type)
        this.graph_type = graph_type
        
    def form_graph(self, graph_type, conclusion = this.conclusion):
        # TO IMPLEMENT
        
        pass
    
class linear_graph(graph):
    def __init__(self, conclusion, type, graph_type = graph_type.LINEAR):
        super().__init__(graph_type, conclusion, type)
        this.graph_type = graph_type
        
    def form_graph(self, graph_type, conclusion = this.conclusion):
        # TO IMPLEMENT
        
        pass