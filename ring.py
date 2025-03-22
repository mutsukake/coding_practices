import sys

def main():
    s = input().strip()
    p = input().strip()

    # Check if each character in p appears in s with sufficient frequency
    for char in set(p):
        if s.count(char) < p.count(char):
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    main()