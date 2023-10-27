from HashTable import HashTable


# 1b(2 symbol tables for lab 3)
class SymbolTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = HashTable(size)

    def add_hash(self, name):
        return self.hash_table.add_hash(name)

    def check_hash(self, name):
        return self.hash_table.existence(name)

    def get_position_hash(self, name):
        return self.hash_table.get_hash_value(name)

    def __str__(self):
        return "Symbol Table = " + "Hash table=" + str(self.hash_table)
