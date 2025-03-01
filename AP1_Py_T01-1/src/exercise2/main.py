def is_number_palindrome(num: int) -> bool:
    if num < 0:
        return False


def main() -> None:
    number = int(input())
    print(is_number_palindrome(number))


if __name__ == '__main__':
    main()
