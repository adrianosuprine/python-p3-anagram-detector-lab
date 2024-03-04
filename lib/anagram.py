# your code goes here!
# pseudocode
# start
#   create empty list to store anagrams
#   iterate over the list of possible anagrams
#   compare each word on the list with the initialized one
#   append any anagram found in the list
#   return list of anagrams
# end
class Anagram:
    # takes a word on initialization
    def __init__(self,word):
        self.word = word
    
    def match(self,possible_anagrams):
        # creates empty list to store any anagrams
        anagrams = []
        for anagram in possible_anagrams:
           
            if sorted(self.word.lower()) == sorted(anagram.lower()):
                anagrams.append(anagram)
        return anagrams
       
            
            
            
listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])
# => ['inlets']            
            
