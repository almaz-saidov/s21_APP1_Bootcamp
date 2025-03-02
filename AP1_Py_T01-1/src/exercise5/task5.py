def check_input(string_to_check: str) -> bool:
    for i in range(len(string_to_check)):
        if string_to_check[i].isalpha() or \
            string_to_check[i] == '-' and i != 0 or \
            not string_to_check[i].isdigit() and string_to_check[i] != '.' and string_to_check[i] != '-' or \
            string_to_check.count('.') > 1:
            return False

    return True


def convert_to_float(string_to_convert: str) -> float:
    parts = list(map(int, string_to_convert.split('.')))
    converted = int(parts[0])
    fraction = int(parts[1])

    while fraction > 1:
        fraction /= 10

    if converted < 0:
        return converted - fraction

    return converted + fraction


if __name__ == '__main__':
    string = input()
    
    if not check_input(string):
        print('Incorrect input data')
        exit(1)
    
    print(f'{2 * convert_to_float(string):.3f}')
