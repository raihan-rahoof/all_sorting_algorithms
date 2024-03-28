def bubble_sort(arr):
    for x in range(len(arr)-1,0,-1):
        for y in range(x):
            if arr[y] > arr[y+1]:
                arr[y],arr[y+1] = arr[y+1],arr[y]
    
    return arr


li=[8, 3, 9, 2, 5, 1, 7, 4, 6]
print(bubble_sort(li))