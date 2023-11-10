from HashTable import HashTable


# 1b(2 symbol tables for lab 3)
class SymbolTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = HashTable(size)

    def add_hash(self, key):
        return self.hash_table.add_hash(key)

    def get_hashTable(self):
        return self.hash_table.hashTable


    def check_hash(self, key):
        return self.hash_table.contains_hash(key)

    def get_position_hash(self, key):
        return self.hash_table.get_hash_value(key)

    def __str__(self):
        return "Symbol Table = " + str(self.hash_table)
