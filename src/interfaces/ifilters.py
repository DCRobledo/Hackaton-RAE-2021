# This is an interface file and should not be changed, they idea is to implement the methods contained in here into its corresponding src/components file

class ifilters:
    def filter_word(self, word):
        check_bad_types(word)
        check_good_types(word)
        
    
    def check_bad_types(self, word):
        check_article(word)
        check_pronoun(word)
        check_preposition(word)
        check_conjunction(word)
        check_interjection(word)
    
    def check_article(self, word):
        " This function checks if a word is an article, in which case it eliminates that word "
        pass
    
    def check_pronoun(self, word):
        " This function checks if a word is an pronoun, in which case it eliminates that word "
        pass
    
    def check_preposition(self, word):
        " This function checks if a word is an preposition, in which case it eliminates that word "
        pass
    
    def check_conjunction(self, word):
        " This function checks if a word is an conjuction, in which case it eliminates that word "
        pass
    
    def check_interjection(self, word):
        " This function checks if a word is an interjection, in which case it eliminates that word "
        pass
    
    def check_good_types(self, word):
        check_noun(word)
        check_adjetive(word)
        check_adverb(word)
        check_verb(word)
        
    def check_noun(self, word):
        " This function assings the noun word type to a word in case it detects that it belongs to that family "
        pass
    
    def check_adjetive(self, word):
        " This function assings the adjetive word type to a word in case it detects that it belongs to that family "
        pass
    
    def check_adverb(self, word):
        " This function assings the adverb word type to a word in case it detects that it belongs to that family "
        pass
    
    def check_verb(self, word):
        " This function assings the verb word type to a word in case it detects that it belongs to that family "
        pass
        