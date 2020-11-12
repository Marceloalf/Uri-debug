class Volei:
    def __init__(self):
        self.attempts = [0, 0, 0]
        self.points = [0, 0, 0]
        self.result = [0, 0, 0]

    def get_soma(self):
        attempt = input().split()
        point = input().split()

        for i in range(0, 3):
            self.attempts[i] += int(attempt[i])
            self.points[i] += int(point[i])

    def get_results(self):
        for i in range(0, 3):
            self.result[i] = regra_de_3(self.attempts[i], self.points[i])
        print("Pontos de Saque: {:.2f} %.".format(self.result[0]))
        print("Pontos de Bloqueio: {:.2f} %.".format(self.result[1]))
        print("Pontos de Ataque: {:.2f} %.".format(self.result[2]))


def regra_de_3(a, b):
    return (b*100)/a


def main():
    n = int(input())
    game = Volei()
    for i in range(0, n):
        name = input()
        game.get_soma()
    game.get_results()


if __name__ == '__main__':
    main()
