import math


def main(data):
    result = 0
    pairs = []

    N = len(data)
    for i in range(N):
        for j in range(i + 1, N):
            first = data[i]
            second = data[j]

            if first[0] == second[0] or math.gcd(first[1], second[1]) != 1:
                result += 1
                pairs.append(f'{i + 1} {j + 1}')
    return result, pairs


if __name__ == '__main__':
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result, pairs = main(data)
    print(result)
    print('\n'.join(pairs))
