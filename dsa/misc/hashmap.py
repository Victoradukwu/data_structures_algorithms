from typing import List, Optional


class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class HashMap:
    """
    Insert, Remove and Search each has a time complexity of O(1), but Inorder traversing is O(nlogn)
    """
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map: List[Optional[Pair]] = [None, None]
        
    def hash(self, key):
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity
    
    def get(self, key):
        index = self.hash(key)
        
        while self.map[index] is not None:
            if self.map[index].key == key:  # type: ignore
                return self.map[index].val  # type: ignore
            index += 1
            index = index % self.capacity # To ensure we do not go out of bounds
        return None
    
    def put(self, key, val):
        index = self.hash(key)

        while True:
            if self.map[index] is None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            #if key is already at this index, we overwrite it
            elif self.map[index].key == key:  # type: ignore
                self.map[index].val = val  # type: ignore
                return
            
            index += 1
            index = index % self.capacity
            
    def remove(self, key):
        if not self.get(key):
            return
        
        index = self.hash(key)
        while True:
            if self.map[index].key == key: # type: ignore
                # Removing an element using open-addressing actually causes a bug,
                # because we may create a hole in the list, and our get() may 
                # stop searching early when it reaches this hole.
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity
            
    def rehash(self):
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)
                
    def print(self):
        for pair in self.map:
            if pair:
                print(pair.key, pair.val)