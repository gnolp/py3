def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check_number(num_str):
    length = len(num_str)
    total_sum = 0
    
    for i, char in enumerate(num_str):
        digit = int(char)
        total_sum += digit
        
        if i % 2 == 0:  # 0-based index (even positions in 1-based index)
            if digit % 2 == 0:  # Check for even digit
                continue
            else:
                return "NO"
        else:  # 1-based odd positions
            if digit % 2 == 1:  # Check for odd digit
                continue
            else:
                return "NO"
    
    if is_prime(total_sum):
        return "YES"
    else:
        return "NO"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    test_cases = int(data[0])
    results = []
    
    for i in range(1, test_cases + 1):
        num_str = data[i]
        results.append(check_number(num_str))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
