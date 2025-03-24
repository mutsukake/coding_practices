def main():
    while True:
        s = input().strip()
        if s == '-':  # a single dash indicates no more datasets
            break

        m = int(input().strip())
        for _ in range(m):
            h = int(input().strip())
            # Shuffle: take the first h chars and move them to the end
            s = s[h:] + s[:h]

        print(s)

if __name__ == '__main__':
    main()