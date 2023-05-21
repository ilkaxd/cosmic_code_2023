def main(data, M, V):
    '''
    Ищем максимальное количество спутников,
    которые суммарно не превышают
    указанную массу и объём
    '''
    return DFS(data, M, V)


def DFS(available, M, V, steps=0):
    result = steps

    if len(available) == 0:
        return steps

    for i in range(len(available)):
        m, v = available[i]
        remaind_M = M - m
        remaind_V = V - v
        if remaind_M >= 0 and remaind_V >= 0:
            local = DFS(
                available[:i] + available[i + 1:],
                remaind_M, remaind_V,
                steps + 1
            )
            result = max(local, result)
    return result


if __name__ == '__main__':
    M, V = map(int, input().split())
    N = int(input())
    data = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    print(main(data, M, V))
