def countingValleys(steps, path):
    v = 0
    under = False
    sealevel = 0
    for step in range(0, steps):
        if path[step] == 'U': sealevel += 1
        else: 
            sealevel -= 1
            
        if sealevel <= -1:
            under = True
        else:
            if under == True:
                v += 1
                under = False
    return v

            
            


print(countingValleys(8, ['U','D','D','D','U','D','U','U']))