def count_unique_numbers(num: int) -> int:
    unique_numbers = set()
    
    for i in range(num):
        unique_numbers.add(int(input()))

    return len(unique_numbers)


if __name__ == '__main__':
    n = int(input())
    print(count_unique_numbers(n))
