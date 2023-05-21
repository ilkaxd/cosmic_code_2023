class Astronaut:
    def __init__(self, fist_name, last_name, duration):
        self.first_name = fist_name
        self.last_name = last_name
        self.duration = int(duration)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.duration}'


def main(rows):
    '''
    Сортируем список по длительности пребывания в космосе
    '''
    astronauts = [Astronaut(*x.split()) for x in rows]
    return '\n'.join(
        str(x)
        for x in sorted(astronauts, key=lambda x: x.duration, reverse=True)
    )


if __name__ == '__main__':
    N = int(input())
    rows = [input() for _ in range(N)]
    print(main(rows))
