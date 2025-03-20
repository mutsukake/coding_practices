while True:
    x = input().strip()
    if x == '0':
        break
    # Compute sum of digits in x
    digit_sum = sum(int(d) for d in x)
    print(digit_sum)