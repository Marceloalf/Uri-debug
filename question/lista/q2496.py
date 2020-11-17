def comparison(not_ordered, ordered, n):
    count = 0
    for i in range(n):
        if ordered[i] != not_ordered[i]: count += 1

    return count


def chance(forms, index):
    size = int(forms[index])
    not_ordered = forms[index+1]
    ordered = sorted(set(not_ordered))

    if comparison(not_ordered, ordered, size) <= 2: 
        return "There are the chance."
    else: 
        return "There aren't the chance."


def input_q2496(forms):
    Q = int(forms[0])
    forms.remove(forms[0])
    
    output = []

    for count in range(0, Q+1, 2):
        output.append(chance(forms, count))
    
    return '\n'.join(output)
