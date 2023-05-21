class Satellite:
    def __init__(self, w, w_max, t_start, duration, i):
        self.w = w
        self.w_max = w_max
        self.t_start = t_start
        self.duration = duration
        self.i = i


def main(data, T):
    sattelites = []
    for i, (w, w_max, t_start, duration) in enumerate(data):
        sattelites.append(Satellite(w, w_max, t_start, duration, i + 1))

    sattelites.sort(key=lambda x: x.t_start)

    dp = [0] * (T + 1)

    result_mass = 0
    result_order = []

    for s in sattelites:
        for t in range(T - s.duration, s.t_start - 1, -1):
            if dp[t] + s.w > dp[t + s.duration] and s.w < s.w_max:
                dp[t + s.duration] = dp[t] + s.w

                if dp[t + s.duration] > result_mass:
                    result_mass = dp[t + s.duration]
                    result_order.append(str(s.i))
    return ' '.join(result_order) + '\n' + str(result_mass)


if __name__ == '__main__':
    # n, T = map(int, input().split())
    # data = [list(map(int, input().split())) for _ in range(n)]
    
    T = 20
    data = [
        [100, 150, 5, 10],
        [200, 250, 10, 5],
        [300, 350, 15, 15],
    ]
    print(main(data, T))
