def count_derivative(n: int, coefficients: list[float], x: float) -> float:
    new_coefficients = []
    tmp_n = n

    for coeff in coefficients:
        new_coefficients.append(coeff * tmp_n)
        tmp_n -= 1

    return sum([x ** (n - 1 - i) * new_coefficients[i] for i in range(n)])


if __name__ == '__main__':
    n, x = map(float, input().split())
    coefficients = [float(input()) for _ in range(int(n) + 1)]

    print(f'{count_derivative(int(n), coefficients, x):.3f}')
