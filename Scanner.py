from SymbolTable import SymbolTable
import re
class Scanner:
    def __init__(self, filename):
        self.filename = filename
        self.constants = SymbolTable(100)  # Create a symbol table for constants
        self.identifiers = SymbolTable(100)  # Create a symbol table for identifiers
        self.NotCtNotId = []
        self.program = self.tokenize_program()
        self.pif = self.make_pif()

    def tokenize_program(self):
        # Regex pattern for reserved words and operators
        reserved_words = r'(let|if|else|while|write|read|bool|integer_array|char|string_array|integer|for)'
        operators = r'(\+|-|\*|/|%|==|<=|>=|<|>|=|!=|&&|\|\||{|}|\(|\)|;|,|:|\.)'

        # Regex pattern for constants (integer and string)
        integer_constant = r'-?\d+'
        string_constant = r'"[^"]*"'

        # Regex pattern for identifiers
        identifier = r'[a-zA-Z_][a-zA-Z0-9_]*'

        # Combine all patterns for tokenizing
        pattern = re.compile(f'({reserved_words}|{operators}|{integer_constant}|{string_constant}|{identifier})')

        # Initialize a list for tokens
        tokens = []

        # Read the input file
        with open(self.filename, 'r') as file:
            input_text = file.read()

        # Find all tokens in the input_text
        matches = re.finditer(pattern, input_text)

        # Extract the matched tokens from the matches
        for match in matches:
            tokens.append(match.group(0))
            if re.match(reserved_words, match.group(0)):
                self.NotCtNotId.append(match.group(0))
            elif re.match(operators, match.group(0)):
                self.NotCtNotId.append(match.group(0))
            elif re.match(identifier, match.group(0)):
                self.identifiers.add_hash(match.group(0))
            elif re.match(integer_constant, match.group(0)):
                self.constants.add_hash(int(match.group(0)))
            elif re.match(string_constant, match.group(0)):
                self.constants.add_hash(match.group(0))
            elif not re.match(f'({reserved_words}|{operators}|{integer_constant}|{string_constant}|{identifier})$', match.group(0)):
                raise ValueError(f"Invalid character found: {match.group(0)}")

        invalid_characters = re.findall(r'[^a-zA-Z0-9_+*/%<>=!&|{}();,:"\n .]', input_text)
        if invalid_characters:
            raise ValueError(f"Invalid characters found: {' '.join(set(invalid_characters))}")

        return tokens


    def make_pif(self):
        pif = []
        for token in self.program:
            if self.identifiers.check_hash(token):
                pif.append(['idi', self.identifiers.get_position_hash(token)])
            elif self.constants.check_hash(token):
                pif.append(['idc', self.constants.get_position_hash(token)])
            elif token not in self.NotCtNotId and self.constants.check_hash(int(token)):
                pif.append(['idc', self.constants.get_position_hash(int(token))])
            elif token in self.NotCtNotId:
                pif.append([token, -1])
        return pif


    def write_constants_and_identifiers(self, filename):
        with open(filename, 'w') as file:
            # Write "Constants table" before self.constants
            file.write("Constants table\n")
            for constant_list in self.constants.get_hashTable():
                if not constant_list:  # Check if the list is empty
                    file.write("[]\n")
                else:
                 file.write(' '.join(map(str, constant_list)) + '\n')

            # Write 10 empty lines
            file.write('\n' * 10)

            # Write "Identifiers table" before self.identifiers
            file.write("Identifiers table\n")
            for identifier_list in self.identifiers.get_hashTable():
                if not identifier_list:  # Check if the list is empty
                    file.write("[]\n")
                else:
                 file.write(' '.join(map(str, identifier_list)) + '\n')



    def write_pif(self, filename):
        with open(filename, 'w') as file:
            # Write "Constants table" before self.constants
            file.write("Pif table\n")
            for pif_list in self.pif:
                file.write(' '.join(map(str, pif_list)) + '\n')