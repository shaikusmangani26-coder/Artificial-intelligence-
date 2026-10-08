from itertools import permutations

# Words in the crypt-arithmetic problem
word1 = "SEND"
word2 = "MORE"
result = "MONEY"

# Get all unique letters
letters = set(word1 + word2 + result)

# Try all possible digit combinations
for digits in permutations(range(10), len(letters)):
    
    # Create a dictionary mapping letters to digits
    mapping = dict(zip(letters, digits))

    # Leading letters cannot be zero
    if mapping['S'] == 0 or mapping['M'] == 0:
        continue

    # Convert words into numbers
    SEND = (mapping['S'] * 1000 +
            mapping['E'] * 100 +
            mapping['N'] * 10 +
            mapping['D'])

    MORE = (mapping['M'] * 1000 +
            mapping['O'] * 100 +
            mapping['R'] * 10 +
            mapping['E'])

    MONEY = (mapping['M'] * 10000 +
             mapping['O'] * 1000 +
             mapping['N'] * 100 +
             mapping['E'] * 10 +
             mapping['Y'])

    # Check the equation
    if SEND + MORE == MONEY:
        print("Solution found:")
        print(mapping)
        print("SEND =", SEND)
        print("MORE =", MORE)
        print("MONEY =", MONEY)
        break
