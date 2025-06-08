import sys

def main():
    stack = []
    operators = {"+", "-", "*"}
    
    for line in sys.stdin:
        token = line.strip()
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
        else:
            stack.append(int(token))
    
    print(stack.pop())

if __name__ == "__main__":
    main()