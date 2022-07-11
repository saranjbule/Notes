array =  [12, 11, 13, 84848,0,  5, 6, 3, 0, 789]

def merge(L, R, arr):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k += 1

        else:
            arr[k] = R[j]
            j += 1
            k += 1

    while i < len(L):
        arr[k] = L[i]
        k += 1
        i += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    
def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr)//2
  
        L = arr[:mid]
        R = arr[mid:]
        
        mergeSort(L)
        mergeSort(R)

        merge(L, R, arr)

mergeSort(array)
print(array)