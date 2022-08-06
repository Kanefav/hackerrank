nestedList = []
for time in range(0, 3):
    name = input('name: ')
    score = float(input('score: '))
    nestedList.append([name, score])
nestedList = sorted(nestedList, key= lambda x: x[1])
lowest = nestedList[0][1]
n = 0
output = []
for number in range(0, len(nestedList)):
    if nestedList[number][1] == lowest: continue 
    elif n == 1:
        if secondlowest == nestedList[number][1]: output.append(nestedList[number][0])
    else:
        n = 1
        secondlowest = nestedList[number][1]
        output.append(nestedList[number][0])
for name in range(0, len(output)):
    print(sorted(output)[name])