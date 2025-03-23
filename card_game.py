import sys



def main():
    n = int(input())

    T = 0
    H = 0


    text = []
    for i in range(n):
        text.append(input().split)
        if range(text[i][0]) > range(text[i][1]):
            T += 3
        elif range(text[i][0]) < range(text[i][1]):
            H += 3
        else:
            T += 1
            H += 1
    print(T, H)


if __name__ == "__main__":
    main()

