from collections import OrderedDict 

class LRU_Cache(object):
  def __init__(self, capacity):
      # Initialize class variables
      self.capacity = capacity
      self.cache = OrderedDict()

  def get(self, key):
    if len(self.cache) ==  0:
      return "No Value to get"
    if key not in self.cache:
      return -1
    else:
      self.cache.move_to_end(key)
      return self.cache[key]

    

  def set(self, key, value):
    self.cache[key] = value
    self.cache.move_to_end(key)
    if len(self.cache) > self.capacity:
      self.cache.popitem(last = False)
    


#Test 
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

cache2 = our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

print(f"Removed the Least Used so return -1 -> {cache2}")

#  Test Empty Cach
empty_cache = LRU_Cache(0)
empty = empty_cache.get(1)
print(f"Empty Cache -> {empty}")



