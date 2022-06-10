def birthdayCakeCandles(candles):
    taller = max(candles)
    return candles.count(taller)
    
    
print(birthdayCakeCandles([1, 3, 6, 6]))