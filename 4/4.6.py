def sum_seq(sequence):
    total = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            total += sum_seq(i)
        else:
            total += i
    return total


