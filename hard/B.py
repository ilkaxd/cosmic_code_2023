class Rocket:
    def __init__(self, n, v, data):
        self.n = n
        self.velocity = v
        self.actions = data
        self.t = 0
        self.distance = 0

    def __str__(self) -> str:
        return (
            f'Корабль №{self.n} '
            f'({self.t}-'
            f'{self.velocity}-'
            f'{self.distance})'
        )

    def __repr__(self):
        return self.__str__()


def main(v1, data_1, v2, data_2, t):
    first = Rocket(1, v1, data_1)
    second = Rocket(2, v2, data_2)
    calculate_distance(first, t)
    calculate_distance(second, t)
    if first.distance > second.distance:
        return '1 - {:.2f} м'.format(first.distance)
    return '2 - {:.2f} м'.format(second.distance)


def calculate_distance(rocket, target):
    for t, accelerate in rocket.actions:
        delta_t = t - rocket.t
        rocket.distance += (
            rocket.velocity * delta_t +
            accelerate * delta_t ** 2 / 2
        )
        new_velocity = rocket.velocity + delta_t * accelerate
        rocket.t = t
        rocket.velocity = new_velocity

    rocket.distance += rocket.velocity * (target - rocket.t)


if __name__ == '__main__':
    t = int(input())
    v1, v2 = map(int, input().split())
    n1, n2 = map(int, input().split())
    data_1 = [
        list(map(int, input().split()))
        for _ in range(n1)
    ]
    data_2 = [
        list(map(int, input().split()))
        for _ in range(n2)
    ]
    print(main(v1, data_1, v2, data_2, t))
