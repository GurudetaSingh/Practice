# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        array1 = []
        array2 = []
        for num in nums:
            if num % 2 == 0:
                array1.append(num)
            else:
                array2.append(num)
                
        joined_list = array1 + array2
        return joined_list
