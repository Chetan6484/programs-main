class ChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def search(self, key):
        index = self.hash_function(key)
        return key in self.table[index]
    
ht = ChainingHashTable(5)
ht.insert(10)
ht.insert(15)  
ht.insert(22)  
ht.insert(7)

print("Hash Table:", ht.table)
print("Is 15 in table?", ht.search(15))
print("Is 99 in table?", ht.search(99))

