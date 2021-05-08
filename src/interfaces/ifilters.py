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
        " Function explanation "
        pass
    
    def check_pronoun(self, word):
        " Function explanation "
        pass
    
    def check_preposition(self, word):
        " Function explanation "
        pass
    
    def check_conjunction(self, word):
        " Function explanation "
        pass
    
    def check_interjection(self, word):
        " Function explanation "
        pass
    
    def check_good_types(self, word):
        check_noun(word)
        check_verb(word)
        check_adverb(word)
        check_verb(word)
        
    def check_noun(self, word):
        " Function explanation "
        pass
    
    def check_verb(self, word):
        " Function explanation "
        pass
    
    def check_adverb(self, word):
        " Function explanation "
        pass
    
    def check_verb(self, word):
        " Function explanation "
        pass
        