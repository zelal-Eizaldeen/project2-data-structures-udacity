
from collections import OrderedDict 

class LinkedListNode:  
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
       
       
        
class LRU_Cache(object):
    def __init__(self, capacity=object):
        self.bucket_array = [None for _ in range(capacity)]
        self.p = 37
        self.num_entries = 0
        

    def put(self, key, value):
        # If the cache is full, remove the last element                  
        bucket_index = self.get_bucket_index(key)   
        new_node = LinkedListNode(key, value)                       
        head = self.bucket_array[bucket_index]  
        if key > len(self.bucket_array):
            
            self.delete(key) 
            
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next 
        head = self.bucket_array[bucket_index]
        new_node.next = head                                         
        self.bucket_array[bucket_index] = new_node                 
        self.num_entries += 1
        
    
    def get(self, key):
        # In case of a cache hit
        bucket_index = self.get_bucket_index(key) 
        head = self.bucket_array[bucket_index]
        
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
            
        return -1                                 # In case of a cache miss
    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]
        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next
    # Returns the bucket_index
    def get_bucket_index(self, key):
        bucket_index = self.get_hash_code(key)                        
        return bucket_index 
    # Returns the hash code
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)                          
        current_coefficient = 1                                       
        hash_code = 0
        
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets                       # compress hash_code (Mod operation)
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets   # compress coefficient as well

        return hash_code % num_buckets                                # one last compression before returning
    
    
    def size(self):
        return self.num_entries
     # Helper function to see the hashmap
    def __repr__(self):
        output = "\nLet's view the hash map:"

        node = self.bucket_array
        for bucket_index, node in enumerate(self.bucket_array):
            if node is None:
                output += '\n[{}] '.format(bucket_index)
            else:
                output += '\n[{}]'.format(bucket_index)
                while node is not None:
                    output += ' ({} , {}) '.format(node.key, node.value)
                    if node.next is not None:
                        output += ' --> '
                    node = node.next
                    
        return output
    
our_cache = LRU_Cache(5)

our_cache.put(1, 1);
our_cache.put(2, 2);
our_cache.put(3, 3);
our_cache.put(4, 4);

our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.put(5, 5) 
our_cache.put(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


print("size: {}".format(our_cache.size()))

print("one: {}".format(our_cache.get(1)))
print("two: {}".format(our_cache.get(2)))
print("nine: {}".format(our_cache.get(9)))
print("three: {}".format(our_cache.get(3)))

# our_cache                          # call to the help



