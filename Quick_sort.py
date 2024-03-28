def quick_sort(arr):
    if len(arr)<=1:
        return arr
    
    pivot = arr[len(arr)//2 ]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left)+mid+quick_sort(right)

li=[8, 3, 9, 2, 5, 1, 7, 4, 6]
print(quick_sort(li))