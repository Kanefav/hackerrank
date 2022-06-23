def breakingRecords(scores):
    max = mim = scores[0]
    ma = mi = 0
    for num in scores:
        if num > max:
            max = num
            ma += 1
        if num < mim:
            mim = num
            mi += 1
    return ma, mi
    
    
print(breakingRecords([12, 24, 10, 24]))