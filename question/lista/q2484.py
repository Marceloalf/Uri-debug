def outer_spaces(number, str2):
    return (number * " ") + str2


def inner_spaces(word):
    return " ".join(word)


def remove_last(number, word):
    return word[:-number]


def word_pyramid(word):
    count = 0
    pyramid = []
    while len(word) >= 1:
        pyramid.append(outer_spaces(count, word))
        word = remove_last(2, word)
        count += 1
    return '\n'.join(pyramid)


def input_q2484(form):

    palavras = []
    for i in form:
        word = inner_spaces(i)
        palavras.append(word_pyramid(word))
        palavras.append('\n\n')
    return ''.join(palavras)
