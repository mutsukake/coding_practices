def gcd(a, b):
    """
    Calculate the greatest common divisor of two numbers using the Euclidean algorithm.
    
    The Greatest Common Divisor (GCD) is the largest positive number that divides
    both numbers without a remainder. For example:
    - GCD of 12 and 18 is 6 (because 6 is the largest number that divides both 12 and 18)
    - GCD of 35 and 49 is 7 (because 7 is the largest number that divides both 35 and 49)
    
    The Euclidean algorithm works as follows:
    1. If b = 0, then GCD(a,b) = a (because any number divides 0)
    2. Otherwise, GCD(a,b) = GCD(b, a % b) where % is the remainder operator
    
    This algorithm keeps replacing (a,b) with (b, a%b) until b becomes 0.
    """
    while b:  # Continue until b becomes 0
        a, b = b, a % b  # This line simultaneously updates both a and b
        # First, it sets a = b
        # Then, it sets b = remainder of a divided by b (a % b)
    return a  # When b becomes 0, a is the GCD

def main():
    # Read input
    a, b = map(int, input().split())
    
    # Calculate and output the GCD
    result = gcd(a, b)
    print(result)

if __name__ == "__main__":
    main()
