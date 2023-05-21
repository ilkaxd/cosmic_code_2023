class Planet:
    def __init__(self, name):
        self.name = name
        self.nearest = {}
        self.score = float('inf')
        self.visited = False

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return (
            f'{self.name} {self.visited}'
            f'(топливо: {self.score }, соседей: {len(self.nearest)})'
        )

    def __repr__(self):
        return self.__str__()


def main(data, start, end, fuel):
    '''
    Поиск наикратчайшего пути
    '''
    planets_names = set([x for x, _, _ in data] + [y for _, y, _ in data])

    planets = {
        name: Planet(name)
        for name in planets_names
    }

    for first, second, w in data:
        w = int(w)
        planets[first].nearest[second] = w
        planets[second].nearest[first] = w

    planets[start].score = 0

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

    score = planets[end].score
    if score <= fuel:
        return score
    return -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    start, end = input().split()
    fuel = int(input())
    data = [
        input().split()
        for _ in range(m)
    ]
    print(main(data, start, end, fuel))
