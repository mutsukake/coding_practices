import math

def solve():
    # Read n
    n = int(input().strip())
    # Read x vector
    x = list(map(int, input().split()))
    # Read y vector
    y = list(map(int, input().split()))
    
    # p = 1 (Manhattan distance)
    dist1 = sum(abs(a - b) for a, b in zip(x, y))
    
    # p = 2 (Euclidean distance)
    dist2 = math.sqrt(sum((a - b) ** 2 for a, b in zip(x, y)))
    
    # p = 3
    dist3 = sum(abs(a - b) ** 3 for a, b in zip(x, y)) ** (1.0 / 3.0)
    
    # p = infinity (Chebyshev distance)
    dist_inf = max(abs(a - b) for a, b in zip(x, y))
    
    # Print with 6 decimal places. Using format() to avoid f-string issues on older Python.
    print("{:.6f}".format(dist1))
    print("{:.6f}".format(dist2))
    print("{:.6f}".format(dist3))
    print("{:.6f}".format(dist_inf))

if __name__ == "__main__":
    solve()