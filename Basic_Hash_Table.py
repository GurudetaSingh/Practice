def get_index(data_list, a_string):
    # Variable to store result
    result = 0
    
    for a_character in a_string:
        # convert char to number
        a_number = ord(a_character)
        # Update result by adding number
        result += a_number
    
    # Take remainder of result with size of data list
    list_index = result % len(data_list)
    return list_index
    
class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size
     
    
    def insert(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = key, value
    
    
    def find(self, key):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # 3. Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    
    def update(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = key, value

    
    def list_all(self):
        # 1. Extract the key from each key-value pair 
        return [kv[0] for kv in self.data_list if kv is not None]
