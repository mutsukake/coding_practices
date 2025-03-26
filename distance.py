import math

def main():
    try:
        x1, y1, x2, y2 = map(float, input().split())
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(distance)
    except ValueError:
        print("Invalid input")
if __name__ == "__main__":
    main()
