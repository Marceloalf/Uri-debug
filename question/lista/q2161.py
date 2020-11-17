def den(a):
    if a == 0:
        return 0
    else:
        return 1/(6 + den(a-1))


def input_q2161(forms):
    n = int(forms[0])
    return "{:.10f}".format(3 + den(n))
