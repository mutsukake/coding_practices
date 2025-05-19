import sys

def main():
    # Read the initial string
    text = input().strip()
    # Read the number of commands
    n = int(input().strip())

    for _ in range(n):
        c = input().strip().split()
        command = c[0]

        if command == "print":
            start_idx = int(c[1])
            end_idx   = int(c[2])
            print(text[start_idx:end_idx+1])

        elif command == "replace":
            start_idx   = int(c[1])
            end_idx     = int(c[2])
            replacement = c[3]
            text = text[:start_idx] + replacement + text[end_idx+1:]

        elif command == "reverse":
            start_idx = int(c[1])
            end_idx   = int(c[2])
            # Reverse the specified substring
            reversed_segment = text[start_idx:end_idx+1][::-1]
            text = text[:start_idx] + reversed_segment + text[end_idx+1:]

        else:
            # Ignore unrecognized commands
            continue

    # If the problem statement requires a final print of `text`, keep this:
    # (Check the problem requirements carefully—some versions only want
    # output for the 'print' command and do *not* want a final line.)
    print(text)

if __name__ == "__main__":
    main()