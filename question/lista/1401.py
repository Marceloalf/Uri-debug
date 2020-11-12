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


def main():
    n = int(input())

    for i in range(n):
        data = input()
        for word in sort_permutations(data):
            print(word)
        print()


if __name__ == "__main__":
    main()