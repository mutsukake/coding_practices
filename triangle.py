import math

def main():
    try:
        # Read multiple lines of input until EOF or empty line
        while True:
            try:
                input_line = input()
                if not input_line:  # Exit on empty line
                    break
                
                a, b, c = map(float, input_line.split())
                
                # Input validation
                if a <= 0 or b <= 0 or c <= 0 or c >= 180:
                    print("Invalid triangle measurements")
                    continue
                
                # Calculate triangle properties
                c_rad = math.radians(c)
                area = 0.5 * a * b * math.sin(c_rad)
                side3 = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(c_rad))
                
                # Avoid division by zero
                if a == 0:
                    print("Height calculation impossible: side 'a' is zero")
                else:
                    height = (2 * area) / a
                    print(f"Area: {area:.2f}, Third side: {side3:.2f}, Height: {height:.2f}")
            
            except EOFError:
                break  # Exit on EOF
                
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
