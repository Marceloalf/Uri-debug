from math import log2


def kagebushin(term):
    logaritmo = int(term)
    return (int(log2(logaritmo)))

def input_q2544(forms):
    output = []
    for term in forms:
        output.append(str(kagebushin(term)))
    return '\n'.join(output)