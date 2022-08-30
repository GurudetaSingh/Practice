# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

import numpy as np

def snail(array):
    result = []
    array = np.array(array)
    while len(array) > 0:
        result += array[0].tolist()
        array = np.rot90(array[1:])
    return result
    
