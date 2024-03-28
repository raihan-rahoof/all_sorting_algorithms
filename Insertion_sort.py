def insertion_sort(arr):
    for x in range(1, len(arr)):
        key = arr[x]
        j = x-1
        while j>=0 and key<arr[j]:
            arr[j+1]= arr[j]
            j-=1
        arr[j+1] = key
    
    return arr

li=[8, 3, 9, 2, 5, 1, 7, 4, 6]
print(insertion_sort(li))