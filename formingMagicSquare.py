def formingMagicSquare(s):
    output = 0
    for line in s:
        x = sum(line)     #struggling to make it work in all directions, currently working for the three horizontal 
        if x > 15:        #                                              lines.. (need to work to the diagonals and vertical lines)
            output += x - 15
        else:
            output += 15 - x
    return output
    
    
print(formingMagicSquare([[4, 4, 7], [1, 1, 5], [1, 7, 9]]))