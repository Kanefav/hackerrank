n = int(input())
arr = map(int, input().split())
arr = sorted(arr)
number = arr[-1]
for num in range(len(arr)-1, -1, -1):
    if arr[num] != number:
        print(arr[num])
        break
