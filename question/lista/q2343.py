def create_matrix(lines, columns):
    matrix = [[0 for i in range(columns)]for i in range(lines)]
    return matrix


def add_coordinates(matrix, x, y):
    matrix[x][y] += 1
    return matrix[x][y]


def input_q2343(forms):
    matrix = create_matrix(500, 500)
    verification = 0

    Q = int(forms[0])
    forms.remove(forms[0])

    for i in range(Q):
        x, y = map(int, forms[i].split())
        if add_coordinates(matrix, x, y) > 1:
            verification = 1

    return verification
