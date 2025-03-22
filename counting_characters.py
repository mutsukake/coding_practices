import sys

# Initialize counts for all letters a–z to 0
char_count = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}

# Read from stdin until EOF
for line in sys.stdin:
    for char in line:
        if char.isalpha():
            char = char.lower()
            char_count[char] += 1

# Print the counts for each letter a–z
for c in range(ord('a'), ord('z') + 1):
    letter = chr(c)
    print(f"{letter} : {char_count[letter]}")