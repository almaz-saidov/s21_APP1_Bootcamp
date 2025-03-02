def count_coins(field: list[list[int]]) -> int:
    n, m = len(field), len(field[0])
    
    count_matrix = []
    for _ in range(n):
        count_matrix.append([0] * m)
    count_matrix[0][0] = field[0][0]
    
    for j in range(1, m):
        count_matrix[0][j] = field[0][j - 1] + field[0][j]
    
    for i in range(1, n):
        count_matrix[i][0] = field[i - 1][0] + field[i][0]
    
    for i in range(1, n):
        for j in range(1, m):
            count_matrix[i][j] = field[i][j] + max(count_matrix[i - 1][j], count_matrix[i][j - 1])
    
    return count_matrix[-1][-1]


if __name__ == '__main__':
    n, m = map(int, input().split())
    field = []

    for i in range(n):
        field.append(list(map(int, input().split())))

    print(count_coins(field))
