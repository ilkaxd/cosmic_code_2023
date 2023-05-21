import datetime as dt


def main(h, m, duration=108):
    '''
    Вычисляем время полёта Гагарина
    '''
    start = dt.datetime(
        year=1961, month=4, day=12,
        hour=h, minute=m, second=0
    )
    end = start + dt.timedelta(minutes=108)
    return f'{end.hour} {end.minute}'


if __name__ == '__main__':
    h, m = map(int, input().split())
    print(main(h, m))
