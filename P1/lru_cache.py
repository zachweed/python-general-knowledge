import time

class LRU_Cache(object):

  def __init__(self, capacity):
    # Initialize class variables
    self.capacity = capacity
    self.cache = dict()

  def get(self, key):
    # Retrieve item from provided key. Return -1 if nonexistent.
    if key not in self.cache:
      return -1
    else:
      self.cache[key][1] = time.time()
      return self.cache[key][0]

  def set(self, key, value):
    # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
    if key not in self.cache:
      if len(self.cache) + 1 >= self.capacity:
        del self.cache[self.lru()]
      self.cache[key] = [value, time.time()]

  def lru(self):
    # Find the Least Recently Used Key-Value pair and return the Key
    lru_key = next(iter(self.cache))
    for key in self.cache:
      if self.cache[key][1] < self.cache[lru_key][1]:
        lru_key = key
    return lru_key



our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1) == 1)
print(our_cache.get(2) == 2)
print(our_cache.get(9) == -1)

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3) == -1)
