def merge_sort(nums):
    # Terminating condition
    if len(nums) <= 1:
        return nums
    
    # Midpoint
    mid = len(nums) // 2
    
    # Split list into 2 halves
    left = nums[:mid]
    right = nums[mid:]
    
    # Solve problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    
    # Combine results of two havles
    sorted_nums = merge(left_sorted, right_sorted)
    
    return sorted_nums
  
  
def merge(nums1, nums2):
    # List to store results
    merged = []
    
    # Indices for iteration
    i, j = 0, 0
    
    # Loop over the two lists, get smaller element, and move to next element
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
            
    # Get remaining list
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]
    
    # Return final merged array
    return merged + nums1_tail + nums2_tail
