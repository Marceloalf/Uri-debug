class Fila:
    def __init__(self):
        self.number = int(input())
        self.ids = input().split()
        self.dropouts = int(input())
        self.dropouts_ids = input().split()
    
    def remnants(self):
        for i in self.dropouts_ids:
            self.ids.remove(i)


def main():
    soccer = Fila()
    soccer.remnants()
    print(" ".join(soccer.ids))


if __name__ == "__main__":
    main()