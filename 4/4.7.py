

def flatten(sequence):
    lista = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            lista.extend(flatten(item))
        else:
            lista.append(item)
    return lista
