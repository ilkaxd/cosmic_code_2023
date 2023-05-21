class Limit:
    def __init__(self, start, end, available_count):
        self.start = start
        self.end = end
        self.available_count = available_count


def main(limitations, timestamps):
    '''
    Определяем оптимальное распределение запусков
    '''
    limits = [Limit(*x) for x in limitations]

    result = 0
    for timestamp in timestamps:
        for i in range(len(limits)):
            limit = limits[i]
            if (
                limit.start <= timestamp <= limit.end
                and
                limit.available_count > 0
            ):
                limit.available_count -= 1
                result +=1
                break
    return result


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    limitations = [
        list(map(int, input().split()))
        for _ in range(m)
    ]
    timestamps = [int(input()) for _ in range(n)]

    print(main(limitations, timestamps))
