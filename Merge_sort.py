def merge(left,right):
    result = []
    i = j = 0

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    result += left[i:]
    result += right[j:]

    return result

def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

li=[8, 3, 9, 2, 5, 1, 7, 4, 6]
print(merge_sort(li))
