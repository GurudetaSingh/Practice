class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # all letters in word are capital
        # all letters in word are not capital
        # only first letter in word is capital
        
        return word.isupper() or word.islower() or word.istitle()
