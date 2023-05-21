import math


def main(target, velocity, phase):
    '''
    Вычисляем время, затраченное на движение
    '''
    days = 0

    day_duration, night_duration = 7.375, 7.375
    if phase == 1:
        day_duration, night_duration = 14.75, 14.75
    elif phase == 2:
        return None

    circles = target / (day_duration * velocity)

    days += day_duration * circles
    days += night_duration * int(circles)
    return 'Луноход-1 проедет {:.1f} км за {} дней.'.format(
        target,
        math.ceil(days)
    )


if __name__ == '__main__':
    distanse = float(input())
    velocity = int(input())
    phase = int(input())

    print(main(distanse, velocity, phase))
