class Fila:
    def __init__(self, ids):
        self.ids = ids
    
    def remnants(self, dropouts):
        for person in dropouts:
            self.ids.remove(person)
    
    def __str__(self):
        return " ".join(self.ids)


def input_q2460(forms):
    soccer = Fila(forms[1].split())
    soccer.remnants(forms[3].split())
    
    return soccer
