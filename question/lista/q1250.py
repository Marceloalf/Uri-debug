class KiloMan:
    def __init__(self, level, actions):
        self.level = level
        self.actions = actions
        self.damage = 0
    
    def damage_amount(self, amount):
        self.damage = 0
        for i in range(amount):
            if self.one_or_two(self.level[i],self.actions[i]):
                self.damage += 1
            elif self.three_or_higher(self.level[i], self.actions[i]):
                self.damage += 1
        return self.damage
    
    def one_or_two(self, lv, act):
        return lv in (1,2) and act == "S"

    def three_or_higher(self, lv, act):
        return lv >= 3 and act == "J"



def input_q1250(formulario):
    output = []
    count = formulario[0]   # numero de interações
    formulario.remove(count)

    # O laço será executado pelo número de interações
    for i in range(0, len(formulario), 3):
            
        # Variaveis para o calculo
        amount = int(formulario[i])
        level = list(map(int, formulario[i + 1].split()))
        actions = [action for action in formulario[i + 2]]

        # Chamada das funções
        Hero = KiloMan(level, actions)
        output.append(Hero.damage_amount(amount))
    
    return output