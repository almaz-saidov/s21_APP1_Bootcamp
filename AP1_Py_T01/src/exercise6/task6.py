import json


def file_is_valid(file_path: str) -> bool:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        if not isinstance(data.get('list1'), list) or not isinstance(data.get('list2'), list):
            raise ValueError("File must contain lists 'list1' and 'list2'")

        for key in ['list1', 'list2']:
            for item in data[key]:
                if not all(k in item for k in ('title', 'year')):
                    raise ValueError(f"There is not keys 'title' or 'year' in list {key}")

                if not isinstance(item['title'], str) or not isinstance(item['year'], int):
                    raise ValueError(f"The value with the key 'title' must be a string, and with the key 'year' it must be an integer in list {key}")
    
        return True

    except Exception as e:
        print(e)
        return False


def merge(file_path: str) -> str:
    with open(file_path, 'r') as file:
        data = json.load(file)

    merged_data = {'list0': []}

    for key in ['list1', 'list2']:
        for item in data[key]:
            merged_data['list0'].append(item)

    merged_data['list0'] = sorted(merged_data['list0'], key=lambda item: item['year'])
    
    return json.dumps(merged_data, indent=4)


if __name__ == '__main__':
    file_path = 'input.txt'

    if file_is_valid(file_path):
        print(merge(file_path))
    else:
        print('Incorrect input data')
        exit(1)
