def main(data):
    '''
    Определяем минимальную стоимость связей
    '''
    result = 0
    size = len(data)
    for i in range(1, size):
        result += min(data[i][:i])
    return result


if __name__ == '__main__':
    n = int(input())
    data = [
        list(map(int, input().split()))
        for _ in range(n)
    ]
    print(main(data))
