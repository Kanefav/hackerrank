def kangaroo(x1, v1, x2, v2):
    j = (x2 - x1) % (v2 - v1)
    if j == 0: return True
    return False


print(kangaroo(0, 3, 4, 2))