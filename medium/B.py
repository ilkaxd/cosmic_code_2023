def main(data):
    '''
    Вычисляем количество элементов которые нужно отбросить,
    чтобы обе последовательности были возрастающими
    '''
    previous_height, previous_velocity = None, None
    result = 0
    for height, velocity in data:
        if previous_height is None and previous_velocity is None:
            previous_height, previous_velocity = height, velocity
        else:
            if previous_height < height and previous_velocity < velocity:
                previous_height = height
                previous_velocity = velocity
            else:
                result += 1
    return result


if __name__ == '__main__':
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(main(data))
