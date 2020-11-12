from itertools import permutations


def sort_permutations(data):
    word = sorted(set(permute(data)))
    return word


def join_strings(string):
    return ''.join(char for char in string)


def permute(vector):
    words = []
    for combination in permutations(vector):
        words.append((join_strings(combination)))
    return words


def input_1401(formulario):
    n = formulario[0]
    formulario.remove(n)

    perms = []
    for i in range(int(n)):
        data = formulario[i]
        for word in sort_permutations(data):
            perms.append(word)
        perms.append('---')
    
    return perms
