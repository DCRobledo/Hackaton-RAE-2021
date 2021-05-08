# This is an interface file and should not be changed, they idea is to implement the methods contained in here into its corresponding src/components file

from src.common.enums import analyzer_goal

from datetime import date

class ianalytics:
    def analyze_group(self, word_group, goal):
        if goal == analyzer_goal.FRECUENCY:
            form_frecuency_conclusion(word_group)
            
        elif goal == analyzer_goal.FOREIGN_WORDS:
            form_foreign_words_conclusion(word_group)
            
        elif goal == analyzer_goal.MOST_FRECUENT_TYPE:
            form_most_frecuent_type_conclusion(word_group)
            
        elif goal == analyzer_goal.TECHNICISMS:
            form_technicisms_conclusion(word_group)
            
        elif goal == analyzer_goal.DEFINITION:
            form_definition_conclusion(word_group)
            
    def form_frecuency_conclusion(self, word_group):
        filtered_group = filter_by_year(word_group, year = date.today().year)
        return order_by_frecuency(filtered_group)
        
    def form_foreign_words_conclusion(self, word_group):
        filtered_group = filter_foreign_words(word_group)
        
        alternatives = get_alternatives(filtered_group)
        
        return (order_by_frecuency(filtered_group), alternatives)
        
    def form_most_frecuent_type_conclusion(self, word_group):
        return get_frecuency_per_type(word_group)
        
    def form_technicisms_conclusion(self, word_group):
        filtered_group = filter_technicisms(word_group)
        
        return order_by_frecuency_in_year_range(filtered_group, range = {2015, 2021})
        
    def form_definition_conclusion(self, word_group):
        return (word_group, get_definition(word_group))
    
    
    
    def filter_by_year(self, word_group, year):
        " This function filter the words within a group by year "
        pass
    
    def order_by_frecuency(self, word_group):
        " This function orders the whole word group by their frecuencies "
        pass
    
    def filter_foreign_words(self, word_group):
        " This function filter the words within a group by whether or not they are a foreign word "
        pass
    
    def get_alternatives(self, word_group):
        " This function gets the alternativates for each foreign word "
        pass
    
    def filter_technicisms(self, word_group):
        " This function filter the words within a group by whether or not they are a technicism "
        pass
    
    def get_frecuency_per_type(self, word_group):
        " This functions return the frecuency for each type of word "
        pass
    
    def order_by_frecuency_in_year_range(self, word_group, range):
        " This function orders the whole word group by their frecuencies within a range of years"
        pass
    
    def get_definition(self, word_group):
        " This function gets the definition of every word within a word group "
        pass
        
        