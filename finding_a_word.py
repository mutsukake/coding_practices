import string

def main():
    # Read the target word and convert it to lowercase
    w = input().lower()
    count = 0
    
    while True:
        line = input()
        if line == "END_OF_TEXT":
            break
        
        # Split the line and strip punctuation, then compare ignoring case
        words = line.split()
        for word in words:
            # Strip punctuation if needed, then compare
            word = word.strip(string.punctuation).lower()
            if word == w:
                count += 1

    print(count)

if __name__ == '__main__':
    main()