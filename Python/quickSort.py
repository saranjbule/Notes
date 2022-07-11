array = [10, 87, 16, 8, 9, 5, 121, 0, 456, -3, 76]

def quickSort(arr, s, e, p):
    if s < e:
        counter = 0
        for i in arr:
            if i < arr[p]:
                counter += 1

        if counter > 0:
            arr[p], arr[counter] = arr[counter], arr[p]

        i = s
        j = e
        p = counter
        while i < j:
            while arr[i] < arr[p]:
                i += 1

            while arr[j] > arr[p]:
                j -= 1

            if i < j:
                if arr[i] > arr[p] and arr[j] < arr[p]:
                    arr[i], arr[j] = arr[j], arr[i]

        quickSort(arr, s, p-1, 0)
        quickSort(arr, p+1, e, p+1)
        


si = 0
ei = len(array) - 1
pi = 0
quickSort(array, si, ei, pi)

print(array)