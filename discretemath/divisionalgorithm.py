def positiveDivision(n, d):
    q = 0
    while n >= d:
        q = q + 1
        n = n - d

    print('Div {0} Mod {1} or {2} * {3} + {4}'.format(q, n, q,d, n))


def negativeDivision(n, d):
    q = 0
    while n <= 0:
        q = q - 1
        n = n + d
    print('Div {0} Mod {1} or {2} * {3} + {4}'.format(q, n, q, d, n))
