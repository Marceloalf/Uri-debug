class Volei:
    def __init__(self):
        self.attempts = [0, 0, 0]
        self.points = [0, 0, 0]
        self.result = [0, 0, 0]

    def get_soma(self, att, pt):
        attempt = att
        point = pt

        for i in range(0, 3):
            self.attempts[i] += int(attempt[i])
            self.points[i] += int(point[i])

    def regra_de_3(self, a, b):
        return (b*100)/a

    def get_results(self):
        output = []
        for i in range(0, 3):
            self.result[i] = self.regra_de_3(self.attempts[i], self.points[i])
        output.append(self.get_serve())
        output.append(self.get_block())
        output.append(self.get_attack())
        
        return '\n'.join(output)

    def get_serve(self):
        return "Pontos de Saque: {:.2f} %.".format(self.result[0])
    
    def get_block(self):
        return "Pontos de Bloqueio: {:.2f} %.".format(self.result[1])
    
    def get_attack(self):
        return "Pontos de Ataque: {:.2f} %.".format(self.result[2])


def input_q2310(forms):
    n = int(forms[0])
    forms.remove(forms[0])

    game = Volei()
    for i in range(0, len(forms), 3):
        game.get_soma(forms[i+1].split(), forms[i+2].split())
    
    return game.get_results()
