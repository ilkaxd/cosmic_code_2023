from ease.A import main as ease_A
from ease.B import main as ease_B
from ease.C import main as ease_C
from ease.D import main as ease_D

from medium.A import main as medium_A
from medium.B import main as medium_B
from medium.C import main as medium_C
from medium.D import main as medium_D

from hard.A import main as hard_A
from hard.B import main as hard_B
from hard.C import main as hard_C
from hard.D import main as hard_D

from unreal.A import main as unreal_A
from unreal.B import main as unreal_B
from unreal.C import main as unreal_C


def test_ease_A():
    data = [
        'Yuri Gagarin 1',
        'Valentina Tereshkova 3',
        'Alexei Leonov 4'
    ]

    result = '\n'.join([
        'Alexei Leonov 4',
        'Valentina Tereshkova 3',
        'Yuri Gagarin 1',
    ])
    assert ease_A(data) == result


def test_ease_B():
    assert ease_B(9, 7) == '10 55'


def test_ease_C():
    M, V = 1_000, 1_000
    data = [
        (250, 250),
        (300, 300),
        (350, 350),
        (200, 200)
    ]
    assert ease_C(data, M, V) == 3


def test_ease_D():
    distanse = 500
    velocity = 50
    phase = 3
    assert (
        ease_D(distanse, velocity, phase)
        ==
        'Луноход-1 проедет 500.0 км за 18 дней.'
    )


def test_medium_A():
    rows = [
        [120, 80, 40],
        [250, 180, 80],
        [360, 480, 100],
        [400, 300, 120]
    ]
    assert medium_A(rows) == '320.00 298.82'


def test_medium_B():
    data = [
        (1, 2),
        (2, 1),
        (3, 4),
        (4, 3)
    ]
    assert medium_B(data) == 2


def test_medium_C():
    data = [
        [1, 15],
        [1, 45],
        [1, 75],
        [1, 30],
        [1, 90]
    ]
    assert medium_C(data) == (
        10,
        [
            '1 2',
            '1 3',
            '1 4',
            '1 5',
            '2 3',
            '2 4',
            '2 5',
            '3 4',
            '3 5',
            '4 5'
        ])


def test_medium_D():
    data = [
        (1961, 100),
        (1961, 50),
        (1969, 100),
        (1969, 80),
        (1971, 70)
    ]
    assert medium_D(data) == 1969


def test_hard_A():
    n = 5
    data = [
        (1, 2, 10),
        (2, 5, 100),
        (2, 3, 10),
        (4, 3, 10),
        (1, 4, 100),
        (4, 5, 10),
    ]
    assert hard_A(data, n) == 40


def test_hard_B():    
    t = 10
    v1, v2 = 5_000, 6_000
    data_1 = [
        (1, 500),
        (5, -1000),
        (9, 700),
    ]
    data_2 = [
        (3, 1000),
        (7, -1500),
    ]
    assert hard_B(v1, data_1, v2, data_2, t) == '2 - 55500.00 м'


def test_hard_C():
    start, end = 'Earth', 'Mars'
    fuel = 5000
    data = [
        ['Earth', 'Venus', 2000],
        ['Earth', 'Mars', 5000],
        ['Earth', 'Jupiter', 8000],
        ['Mars', 'Jupiter', 3000],
        ['Venus', 'Mars', 2500]
    ]
    assert hard_C(data, start, end, fuel) == 4500


def test_hard_D():
    T = 20
    data = [
        [100, 150, 5, 10],
        [200, 250, 10, 5],
        [300, 350, 15, 15],
    ]
    assert(hard_D(data, T)) == '1 2\n300'


def test_unrial_A():
    data = [
        [0, 1, 3, 4],
        [1, 0, 2, 3],
        [3, 2, 0, 5],
        [4, 3, 5, 0],
    ]
    assert unreal_A(data) == 6


def test_unreal_B():
    limitations = [
        (1, 10, 2),
        (11, 20, 1),
        (21, 30, 2)
    ]

    timestamps = [2, 10, 12, 25, 28]
    assert unreal_B(limitations, timestamps) == 5


def test_unreal_C():
    data = [
        [0, 0, 3, 3, 3, 0, 6, 3],
        [0, 0, 1, 1, 1, 0, 2, 1, 0, 1, 1, 2]
    ]
    assert unreal_C(data) == [1, 2]
