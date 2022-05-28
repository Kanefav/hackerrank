def diagonalDifference(arr):
    firstd = 0
    secondd = 0
    for line in range(0, len(arr)):
        firstd += arr[line][line]
    for line_inverse in range(len(arr)-1, -1, -1):
        secondd += arr[line-line_inverse][line_inverse]
    output = firstd - secondd
    if output >= 0: return output
    else: return output * -1


print(diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]))