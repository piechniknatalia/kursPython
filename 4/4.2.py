def make_ruler(n):
    s = ''
    for i in range(n):
        s += ("|....")
    s += ("|\n")
    for i in range(n + 1):
        if i < 9:
            s += (str(i) + "    ")
        else:
            s += (str(i) + "   ")
    return(s)

def make_grid(rows, cols):
    s = ''
    for i in range(rows):
        for j in range(cols):
            s += "+---"
        s += "+\n"
        for j in range(cols):
            s += "|   "
        s += "|\n"
    for k in range(cols):
        s += "+---"
    s += "+"
    return(s)

