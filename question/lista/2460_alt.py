class Fila:
    def __init__(self, ids):
        self.ids = ids
    
    def remnants(self, dropouts):
        for person in dropouts:
            self.ids.remove(person)
    
    def __str__(self):
        return " ".join(self.ids)


def main():
    int(input())
    soccer = Fila(input().split())
    
    int(input())
    soccer.remnants(input().split())
    
    print(soccer)
    
if __name__ == "__main__":
    main()
