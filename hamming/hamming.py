def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("uno de los strings tiene un tamaño diferente")
    contador = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            contador += 1
    return contador
