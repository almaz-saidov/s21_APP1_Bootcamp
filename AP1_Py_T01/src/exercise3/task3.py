def count_shapes(matrix: list[list[int]]) -> tuple[int, int]:
    n = len(matrix)
    visited = [[False for _ in range(n)] for _ in range(n)]
    squares = 0
    circles = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def is_square(cells):
        min_row = min(cell[0] for cell in cells)
        max_row = max(cell[0] for cell in cells)
        min_col = min(cell[1] for cell in cells)
        max_col = max(cell[1] for cell in cells)

        for i in range(min_row, max_row + 1):
            for j in range(min_col, max_col + 1):
                if matrix[i][j] != 1:
                    return False

        return (max_row - min_row) == (max_col - min_col)

    def dfs(i: int, j: int, cells: list[tuple[int, int]]) -> None:
        if i < 0 or i >= n or j < 0 or j >= n or matrix[i][j] == 0 or visited[i][j]:
            return
        visited[i][j] = True
        cells.append((i, j))
        for dx, dy in directions:
            dfs(i + dx, j + dy, cells)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1 and not visited[i][j]:
                cells = []
                dfs(i, j, cells)
                if len(cells) > 1:
                    if is_square(cells):
                        squares += 1
                    else:
                        circles += 1

    return squares, circles


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        matrix = [list(map(int, line.split())) for line in file.readlines()]

    squares, circles = count_shapes(matrix)
    print(squares, circles)
