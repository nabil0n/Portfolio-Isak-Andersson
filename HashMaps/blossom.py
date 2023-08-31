from blossom_lib import flower_definitions
from linked_list import Node, LinkedList

class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for i in range(size)]
    
    def hash(self, key):
        return sum(key.encode())
    
    def compress(self, hash_c):
        return hash_c % self.array_size
    
    def assign(self, key, value):
        arrayindex = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[arrayindex]
        
        for i in list_at_array:
            if key == i[0]:
                i[1] = value
                return
        list_at_array.insert(payload)
    
    def retrieve(self, key):
        arrayindex = self.compress(self.hash(key))
        list_at_index = self.array[arrayindex]
        
        for i in list_at_index:
            if key == i[0]:
                return i[1]
        return None
        

m = HashMap(len(flower_definitions))

for flower in flower_definitions:
    m.assign(flower[0], flower[1])
    
print(m.retrieve('daisy'))