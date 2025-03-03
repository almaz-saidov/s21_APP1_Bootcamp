def get_scalar_composition(v1: list[float], v2: list[float]) -> float:
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]


if __name__ == '__main__':
    vector1 = list(map(float, input().split()))
    vector2 = list(map(float, input().split()))
    print(get_scalar_composition(vector1, vector2))
