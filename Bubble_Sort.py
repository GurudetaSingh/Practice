def bubble_sort(nums): 
    # Create copy to avoid changing list
    nums = list(nums)
    
    # Repeat n - 1 times
    for _ in range(len(nums) - 1):
        # Iterate over array (except last element)
        for i in range(len(nums) - 1):
            # Compare numbers
            if nums[i] > nums[i + 1]:
                # Swap numbers
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                
    return nums
