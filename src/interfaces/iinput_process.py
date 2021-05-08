# This is an interface file and should not be changed, they idea is to implement the methods contained in here into its corresponding src/components file

class iinput_process:
    def remove_characters(self, text, caracters_to_remove = {'.', ';', ',', ' '}):
        " This function sholud process all the text from the input resource and eliminate the characters which are contained in the argument list "
        pass
    
    def format_output(self, text):
        " This function needs to transform the input character chain into the desired format "
        pass
    
    def add_aditional_information(self, word, year, source, RAE):
        " This function simply adds a word's basic information "
        pass
    