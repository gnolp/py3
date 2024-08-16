def is_interleaved_number(num):
    num_str = str(num)
    length = len(num_str)

    # 1. Check if the number of digits is odd
    if length % 2 == 0:
        return False

    # 2. Check if the first digit is different from the second digit
    if num_str[0] == num_str[1]:
        return False

    # 3. Check if digits at odd positions and the last digit are the same
    first_digit = num_str[0]
    for i in range(0, length, 2):
        if num_str[i] != first_digit:
            return False

    return True
def main():
    for _ in range(int(input())):
        number = int(input())
        if is_interleaved_number(number):
            print('YES')
        else:
            print("NO")
if __name__ == "__main__":
    main()