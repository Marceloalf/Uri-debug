def by_distance(line):
    print("oi")
    return int(line[2])

def by_region(line):
    print("bye")
    return line[1]

def path(students):
    sorted(students, key=by_region)
    sorted(students, key=by_distance)

def main():
    Q = int(input())

    students = [[input().split()]for i in range(Q)]
    path(students)

    for i in students:
        print(i)

if __name__ == "__main__":
    main()