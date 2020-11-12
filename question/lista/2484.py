def outer_spaces(number, str2):
    return (number * " ") + str2


def inner_spaces(word):
    return " ".join(word)


def remove_last(number, word):
    return word[:-number]


def word_pyramid(word):
    count = 0
    while len(word) >= 1:
        print(outer_spaces(count, word))
        word = remove_last(2, word)
        count += 1


def main():
    word = list(input())
    word = inner_spaces(word)

    word_pyramid(word)
    print()


if __name__ == '__main__':
    while True:
        try:
            main()
        except EOFError:
            break
