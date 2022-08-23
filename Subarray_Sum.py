# Subarray with given sum
# You are given an array of numbers(non-negative). Find a 
# Continuous subarray of list that adds up to given sum
def subarray_sum3(arr, target):
    n = len(arr)
    i, j, s = 0, 0, 0
    while i < n and j < n + 1:
        if s == target:
            return i, j
        elif s < target:
            if j < n:
                s += arr[j]
            j += 1
        elif s > target:
            s -= arr[i]
            i += 1
            
    return None, None        
