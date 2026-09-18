def linear_search(L, x):
    n = len(L)

    for i in range(n):
        if L[i] == x:
            return i
    return -1
