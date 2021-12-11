def count_leafs(top):
    if top is None:
        return 0
    if (top.left is None and top.right is None):
        return 1
    else:
        return count_leafs(top.left) + count_leafs(top.right)

def count_total(top):
    if top is None:
        return 0
    if (top.left is None and top.right is None):
        return top.data
    else:
        return top.data + count_total(top.left) + count_total(top.right)