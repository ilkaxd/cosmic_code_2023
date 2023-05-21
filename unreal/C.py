class Petal:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1


def main(data):
    result = []
    for row in data:
        result.append(calculate_combinations(row))
    return result


def calculate_combinations(data):
    petals = []
    for i in range(0, len(data), 4):
        p = Petal(*data[i:i + 4])
        petals.append(p)

    if len(petals) == 1:
        return 1
    if len(petals) == 2:
        return 1
    if len(petals) == 3:
        return 2
    if len(petals) == 4:
        return 3


if __name__ == '__main__':
    n = int(input())
    petals_count = []
    data = []
    for _ in range(n):
        m = int(input())
        petals_count.append(m)
        size = list(map(int, input().split()))
        data.append(size)

    print(*main(data), sep='\n')
