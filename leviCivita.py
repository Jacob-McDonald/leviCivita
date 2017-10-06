def perm_parity(a, b):

    a = list(a)
    b = list(b)

    if sorted(a) != sorted(b): return 0

    inversions = 0

    while a:
        first = a.pop(0)
        inversions += b.index(first)
        b.remove(first)

    return -1 if inversions % 2 else 1

def loop_recursive(dim, n, q, s, paritycheck):

    if n < dim:

        for x in range(dim):
            q[n] = x
            loop_recursive(dim, n + 1, q, s, paritycheck)

    else:
        s.append(perm_parity(q, paritycheck))

def LeviCivitaTensor(dim):

    qinit = np.zeros(dim)
    paritycheck = range(dim)
    flattened_tensor = []
    loop_recursive(dim, 0, qinit, flattened_tensor, paritycheck)

    return np.reshape(flattened_tensor, [dim] * dim)