def comparison(not_ordered, ordered, n):
    count = 0
    for i in range(n):
        if ordered[i] != not_ordered[i]: count += 1

    return count


def main():
    size = int(input())
    
    not_ordered = input()
    ordered = sorted(set(not_ordered))

    if comparison(not_ordered, ordered, size) <= 2: print("There are the chance.")
    else: print("There aren't the chance.")


if __name__ == "__main__":
    for i in range(int(input())):
        main()
