x = int(1)
y = int(1)
z = int(2)          # new_list = [expression for member in iterable]
n = int(3)          
output = [[ax, by, cz] for ax in (x+1) for by in (y+1) for cz in (z+1) if (ax + by + cz) != 3]
print(output)