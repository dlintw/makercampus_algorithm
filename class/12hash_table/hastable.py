class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])
    
    def search(self, key):
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None
    
    def delete(self, key):
        index = self.hash_function(key)
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]
                return True
        return False

# 測試哈希表
hash_table = HashTable(10)
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("grape", 30)

print(hash_table.search("apple"))  # 輸出: 10
print(hash_table.search("banana"))  # 輸出: 20
print(hash_table.search("grape"))  # 輸出: 30

hash_table.delete("banana")
print(hash_table.search("banana"))  # 輸出: None
