import re
class FiniteAutomaton:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def display_states(self):
        print("Set of States:", self.states)

    def display_alphabet(self):
        print("Alphabet:", self.alphabet)

    def display_transitions(self):
        print("Transitions:")
        for transition, destination_state in self.transitions.items():
            source_state, symbol = transition
            print(f"({source_state}, {symbol}) -> {destination_state}")


    def display_initial_state(self):
        print("Initial State:", self.initial_state)

    def display_final_states(self):
        print("Set of Final States:", self.final_states)

    def is_sequence_accepted(self, sequence):
        current_state = self.initial_state
        for symbol in sequence:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return False
        return current_state in self.final_states


# Read FA from file
def read_fa_from_file(file_path):
    # Populate states, alphabet, transitions, initial_state, and final_states
    # States
    #states = ['Q0', 'Q1', 'Q2']

    # Alphabet
    #alphabet = ['a', 'b']

    # Transitions
    #transitions = {
     #   ('Q0', 'a'): 'Q1',
      #  ('Q0', 'b'): 'Q0',
       # ('Q1', 'a'): 'Q2',
        #('Q1', 'b'): 'Q0',
        #('Q2', 'a'): 'Q2',
        #('Q2', 'b'): 'Q1',
    #}

    # Initial State
    #initial_state = 'Q0'

    # Final States
    #final_states = ['Q2']
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize variables
    states = []
    alphabet = []
    transitions = {}
    initial_state = None
    final_states = []

    # Parse lines to extract information
    current_section = None
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespaces
        if line.startswith("#"):
            # Switch to a new section based on the comment in the line
            current_section = line[1:].strip().lower()
        elif current_section == 'states':
            states.append(line)
        elif current_section == 'alphabet':
            alphabet.extend(line.split())
        elif current_section == 'transitions':
            # Use regular expression to extract information
            match = re.match(r'\((.*),\s*(\w+)\)\s*->\s*(\w+)', line)
            if match:
                from_state, symbol, to_state = match.groups()
                transitions[(from_state, symbol)] = to_state
        elif current_section == 'initial state':
            initial_state = line
        elif current_section == 'final states':
            final_states.extend(line.split())

    #print(transitions)
    return FiniteAutomaton(states, alphabet, transitions, initial_state, final_states)



# Main menu
def main():
    fa = read_fa_from_file("FA.in")

    while True:
        print("\nMenu:")
        print("1. Display Set of States")
        print("2. Display Alphabet")
        print("3. Display Transitions")
        print("4. Display Initial State")
        print("5. Display Set of Final States")
        print("6. Verify Sequence for DFA")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            fa.display_states()
        elif choice == "2":
            fa.display_alphabet()
        elif choice == "3":
            fa.display_transitions()
        elif choice == "4":
            fa.display_initial_state()
        elif choice == "5":
            fa.display_final_states()
        elif choice == "6":
            sequence = input("Enter the sequence to verify: ")
            result = fa.is_sequence_accepted(sequence)
            print("Sequence accepted" if result else "Sequence not accepted")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
