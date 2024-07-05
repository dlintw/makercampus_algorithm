class DynamicHashTable:
    def __init__(self, initial_size=10):
        self.size = initial_size
        self.table = [[] for _ in range(self.size)]
        self.count = 0

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        if self.count / self.size > 0.7:
            self.resize(self.size * 2)
        index = self.hash_function(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])
        self.count += 1

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
                self.count -= 1
                if self.count / self.size < 0.2 and self.size > 10:
                    self.resize(self.size // 2)
                return True
        return False

    def resize(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        for bucket in old_table:
            for kvp in bucket:
                self.insert(kvp[0], kvp[1])
# 測試動態擴容的哈希表
dynamic_hash_table = DynamicHashTable()
for i in range(20):
    dynamic_hash_table.insert(f"key{i}", i)

for i in range(20):
    print(dynamic_hash_table.search(f"key{i}"))  # 輸出: 0, 1, 2, ..., 19

dynamic_hash_table.delete("key5")
print(dynamic_hash_table.search("key5"))  # 輸出: None
