def splitBracket(text: str) -> list:
    indexes = []

    s = 0
    e = 0
    p = 0

    while True:
        s = text[p:].find('[')
        if s == -1: break

        s += p

        e = text[p:].find(']')
        e += p + 1

        indexes.append([s, e])

        p = e+1

    result = []
    for s, e in indexes:
        result.append(text[s+1:e-1])

    result.append(text[indexes[-1][1]+1:])

    return result
