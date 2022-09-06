class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Sort array
        strs.sort()
        result = ''
        # Compare first and last string char by character
        for i in range(len(strs[0])):
            # If characters match append char to result
            if strs[0][i] == strs[-1][i]:
                result += strs[0][i]
            # Else, stop comparison
            else:
                break
        return result
        
