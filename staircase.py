def staircase(n):
    output = ''
    for line in range(1, n+1):
        for spaces in range(1, (n-line)+1):
            output += ' '
        output += '#'*line
        if line != n:    
            output += '\n'
    print(output)

staircase(8)