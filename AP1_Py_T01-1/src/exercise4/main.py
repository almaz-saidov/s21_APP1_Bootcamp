def pascal_triangle(num: int):
    rows = [[1], [1, 1]]

    if num == 1:
        print(*rows[0])
    elif num == 2:
        print(*rows[0])
        print(*rows[1])
    else:
        for _ in range(2, num):
            new_row = [1]
            for j in range(len(rows[-1]) - 1):
                new_row.append(rows[-1][j] + rows[-1][j + 1])
            new_row.append(1)
            rows.append(new_row)
            
        for row in rows:
            print(*row)


if __name__ == '__main__':
    try:
        number = int(input())
        pascal_triangle(number)
    except ValueError:
        print(f'Natural number was expected')
        exit(1)
