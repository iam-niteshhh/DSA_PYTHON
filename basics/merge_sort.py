def merge(arr, low, mid, high):

    arr1 = arr[low:mid+1]
    arr2 = arr[mid+1:high+1]
    i, j, k= 0, 0, low
    while i< len(arr1) and j< len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i< len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j< len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1
    return arr

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

arr1 = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
print("Sorting started")
merge_sort(arr1, 0, len(arr1)-1)
print("Sorted array: ", arr1)
