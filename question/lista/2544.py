from math import log2


def main():
    logaritmo = int(input())
    print(int(log2(logaritmo)))


if __name__ == '__main__':
    while True:
        try:
            main()
        except EOFError:
            break
