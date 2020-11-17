def verify(a, b, c):
    return a < b > c or a > b < c


def verify_hills(hills, n):
    verification = 1

    if n == 2 and hills[0] == hills[1]:
        verification = 0

    for i in range(1, n-1):
        if verify(hills[i-1], hills[i], hills[i+1]):
            continue
        else:
            verification = 0

    return verification


def input_q2162(forms):
    n = int(forms[0])
    hills = list(map(int, forms[1].split()))

    return verify_hills(hills, n)
