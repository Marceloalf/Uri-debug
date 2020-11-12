def den(a):
    if a == 0:
        return 0
    else:
        return 1/(6 + den(a-1))


def main():
    n = int(input())
    print("{:.10f}".format(3 + den(n)))


if __name__ == '__main__':
    main()
