# Complete the function/method to return True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

def same_structure_as(original, other):
    if type(original) != type(other):
        return False
    if len(original) == len(other) == 0:
        return True
    if len(original) != len(other):
        return False
    for i in range(len(original)):
        if bool(type(original[i]) == list) != bool(type(other[i]) == list):
            return False
        elif type(original[i]) == type(other[i]) == list:
            return same_structure_as(original[i], other[i])
    return True
