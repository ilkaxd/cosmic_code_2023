def main(rows):
    '''
    Определяем центр масс
    '''
    sum_weighted_x = sum(x * w for x, y, w in rows)
    sum_weighted_y = sum(y * w for x, y, w in rows)
    sum_weights = sum(w for x, y, w in rows)
    optimal_x = round(sum_weighted_x / sum_weights, 2)
    optimal_y = round(sum_weighted_y / sum_weights, 2)
    return '{:.2f} {:.2f}'.format(optimal_x, optimal_y)


if __name__ == '__main__':
    N = int(input())
    rows = [
        list(map(int, input().split()))
        for _ in range(N)
    ]
    print(main(rows))
