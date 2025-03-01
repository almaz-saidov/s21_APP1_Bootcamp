def is_number_palindrome(num: int) -> bool:
    if num < 0:
        return False
    
    digits = []

    while num > 0:
        digits.append(num % 10)
        num //= 10

    for i in range(len(digits) // 2):
        if digits[i] != digits[len(digits) - i - 1]:
            return False
    
    return True


if __name__ == '__main__':
    number = int(input())
    print(is_number_palindrome(number))
