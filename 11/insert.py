def cmp(a, b):
    return (a > b) - (a < b)


def insertsort(L, left, right, cmpfunc=cmp):
    for i in range(left+1, right+1):
        for j in range(i, left, -1):
            if cmpfunc(L[j-1], L[j]):
                L[j-1], L[j] = L[j], L[j-1]
