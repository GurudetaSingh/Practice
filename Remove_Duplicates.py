# method 1
def remove_duplicates(list):
    result = []
    [result.append(x) for x in list if x not in result]
    return result
   
# method 2
def remove_duplicates(array):
    return list(set(array))
    
# method 3
def remove_duplicates(array):
    result = []
    for x in array:
        if x not in result:
            result.append(x) 
