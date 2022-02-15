arr = [4, 2, 7, 1, 3, 9, 20, 13, 8]
n = len(arr)

for i in range(1, n):
    k = arr[i]
    j = i - 1
    while j >= 0 and k < arr[j]:
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j+1] = k
print(arr)

