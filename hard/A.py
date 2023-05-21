class Planet:
    def __init__(self, n):
        self.n = n
        self.nearest = {}
        self.score = float('inf')
        self.visited = False

    def __eq__(self, other):
        return self.n == other.n

    def __str__(self):
        return (
            f'Планета №{self.n} {self.visited}'
            f'(топливо: {self.score }, соседей: {len(self.nearest)})'
        )

    def __repr__(self):
        return self.__str__()


def main(data, n):
    '''
    Поиск наикратчайшего пути
    '''
    planets = {
        x: Planet(x)
        for x in range(1, n + 1)
    }

    for first, second, w in data:
        planets[first].nearest[second] = w
        planets[second].nearest[first] = w

    planets[1].score = 0

    while any(not x.visited for x in planets.values()):
        available_planets = [
            x
            for x in planets.values()
            if not x.visited
        ]
        planet = min(available_planets, key=lambda x: x.score)
        for key in planet.nearest.keys():
            neightbor = planets[key]
            w = planet.nearest[key]
            new_cost = planet.score + w
            neightbor.score = min(neightbor.score, new_cost)
        planet.visited = True

    return planets[n].score


if __name__ == '__main__':
    n, m = map(int, input().split())
    data = [
        list(map(int, input().split()))
        for _ in range(m)
    ]
    print(main(data, n))
