class HashTable:

    def __init__(self, capacity):

        self.hashTable = [[] for i in range(capacity)]
        self.capacity = capacity

    def get_capacity(self):
        return self.capacity

    def hash(self, key):
        if type(key) is int:
            return key % self.capacity

        elif type(key) is str:
            hash_val = 5381
            for ch in key:
                #this is from the internet
                hash_val = ((hash_val << 5) + hash_val) + ord(ch)
            return abs(hash_val) % self.capacity

    def existence(self, key):
        hash_value = self.get_hash_value(key)
        for i in self.hashTable[hash_value]:
            if i == key:
                return True
        return False


    def get_hash_value(self, key):
        hash_value = -1
        if type(key) is int or type(key) is str:
            hash_value = self.hash(key)
        return hash_value


    def add_hash(self, key):
        hash_value = self.get_hash_value(key)
        self.hashTable[hash_value].append(key)


    def __str__(self):
        return str(self.hashTable)