# You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
# Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. 
def count_rotations(nums):
    position = 1 
    
    while position < len(nums):
        if position > 0 and nums[position] < nums[position-1]:  
            return position
        
        position += 1
        
    return 0
