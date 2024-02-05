def unique_elems(arr):
    list = []
    for i in arr:
        if i not in list:
            list.append(i)
    return list

n = int(input())
numbers = []
for i in range(n):
    x = int(input())
    numbers.append(x)

print(unique_elems(numbers))