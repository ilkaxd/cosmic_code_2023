from collections import defaultdict


def main(data):
    '''
    Вычисляем год с максимальным количеством запусков ракет
    '''
    years = defaultdict(int)
    for year, starts in data:
        years[year] += starts
    return max_starts(years)


def max_starts(years):
    max_starts = max(years.values())
    keys = sorted(years.keys())
    for key in keys:
        if years[key] == max_starts:
            return key


if __name__ == '__main__':
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(main(data))
