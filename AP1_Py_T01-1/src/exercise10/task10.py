def get_input_data(n: int) -> list[list[int]]:
    try:
        data = [list(map(int, input().split())) for _ in range(n)]
    except Exception as e:
        print(e)
        exit(1)

    for item in data:
        for num in item:
            if num <= 0:
                print('Incorrect input data')
                exit(1)

    return data


def solution(data: list[list[int]]) -> int:
    sorted_by_year = dict()
    for item in data:
        if item[0] not in sorted_by_year.keys():
            sorted_by_year[item[0]] = [[item[1], item[2]]]
        else:
            sorted_by_year[item[0]].append([item[1], item[2]])

    sorted_by_year = dict(sorted(sorted_by_year.items()))

    for key, value in sorted_by_year.items():
        sorted_by_year[key] = sorted(value, key=lambda item: item[0])
    
    totals = []
    for value in sorted_by_year.values():
        if len(value) > 1:
            totals.append(value[0][0] + value[1][0])
    
    return sorted(totals)[-1]


if __name__ == '__main__':
    try:
        available_devices, required_time = map(int, input().split())
    except Exception as e:
        print(e)
        exit(1)

    if available_devices <= 0 or required_time <= 0:
        print('Incorrect input data')
        exit(1)

    print(solution(get_input_data(available_devices)))
