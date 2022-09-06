class Solution:
    def reverseVowels(self, s: str) -> str:
        a = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        i = 0
        j = len(s) - 1
        
        while (i < j):
            if a[i] in vowels and a[j] in vowels:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
            if a[i] not in vowels:
                i += 1
            if a[j] not in vowels:
                j -= 1
            
        return "".join(a)
