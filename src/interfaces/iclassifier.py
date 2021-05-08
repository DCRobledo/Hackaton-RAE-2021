# This is an interface file and should not be changed, they idea is to implement the methods contained in here into its corresponding src/components file
class iclassifier:
    def classify_word(self, word):
        set_category(word)
        set_scope(word)
        set_composition(word)
        
    def set_category(self, word):
        " This function decides in which category belongs the word to classify "
        pass
        
    def set_scope(self, word):
        " This function decides in which scope belongs the word to classify "
        pass
        
    def set_composition(self, word):
        " This function decides in which composition belongs the word to classify "
        pass