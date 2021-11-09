def odwracanie_iteracyjnie(L, left, right):
    while left <= right:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        left += 1
        right -= 1
    return L


def odwracanie_rekurencyjnie(L, left, right):
    if left > right:
        return L
    else:
        temp = L[left]
        L[left] = L[right]
        L[right] = temp
        return odwracanie_rekurencyjnie(L, left+1, right-1)

