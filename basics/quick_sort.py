
def quick_sort(arr, low, high):
    if low < high:
        mid = partition(arr, low, high)
        quick_sort(arr, low, mid)
        quick_sort(arr, mid+1, high)

def partition(arr, low, high):
    i = low
    j = high
    pivot = arr[low]
    while True:
        while i<=j and arr[i] <= pivot:
            i = i + 1
        while i<=j and arr[j] > pivot:
            j = j - 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

print("QuickSort started")
arr1 = [1, 3, 5, 11, 9, 2, 4, 6, 8, 10]
quick_sort(arr1, 0, len(arr1)-1)
print("Sorted array")
print(arr1)


