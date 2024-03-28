def selection_sort(arr):
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            if arr[x]>arr[y]:
                arr[x] , arr[y] = arr[y],arr[x]
    
    return arr


li=[8, 3, 9, 2, 5, 1, 7, 4, 6]
print(selection_sort(li))
