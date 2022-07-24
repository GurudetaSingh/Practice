class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_words = [word[::-1] for word in s.split(" ")]
            
        new_sentence = " ".join(reversed_words)
        
        return new_sentence
                
        
        
