def comparison(model, vector):
    higher = ''
    for i in range(len(model)):
        for j in range(i, len(model)+1):
            
            sub = model[i:j]
            is_sub_valid = all(sub in word for word in vector)

            if is_sub_valid and len(higher) < len(sub) and i != j:
                higher = sub
    return higher


def main():
    size = int(input())
    model = input()
    phrase = [input() for i in range(size-1)]
    
    print(comparison(model, phrase))


if __name__ == "__main__":
    main()
