# This is an interface file and should not be changed, they idea is to implement the methods contained in here into its corresponding src/components file

from src.common.enums import tuple_type

class ioutput_process:
    def create_graphics(self, conclusion):
        if conclusion == tuple_type.FRECUENCY:
            create_frecuency_graphics(conclusion)
            
        elif conclusion == tuple_type.DEFINITION:
            create_definition_graphics(conclusion)
            
        elif conclusion == tuple_type.FOREIGN_WORDS:
            create_foreign_words_graphics(conclusion)
            
        elif conclusion == tuple_type.MOST_FRECUENT_TYPE:
            create_most_frecuent_type_graphics(conclusion)
            
        elif conclusion == tuple_type.TECHNICISMS:
            create_technicisms_graphics(conclusion)
            
    def create_frecuency_graphics(self, conclusion):
        return (create_table(conclusion, tuple_type.FRECUENCY), create_bar_graph(conclusion, tuple_type.FRECUENCY))
        
    def create_definition_graphics(self, conclusion):
        return create_table(conclusion, tuple_type.DEFINITION)
        
    def create_foreign_words_graphics(self, conclusion):
        return create_table(conclusion, tuple_type.FOREIGN_WORDS)
        
    def create_most_frecuent_type_graphics(self, conclusion):
        return create_bar_graph(conclusion, tuple_type.MOST_FRECUENT_TYPE)
        
    def create_technicisms_graphics(self, conclusion):
        return create_linear_graph(conclusion, tuple_type.TECHNICISMS)
    
    
    def create_table(self, conclusion, type):
        " Function explanation "
        pass
    
    def create_bar_graph(self, conclusion, type):
        " Function explanation "
        pass
    
    def create_linear_graph(self, conclusion, type):
        " Function explanation "
        pass
        
        