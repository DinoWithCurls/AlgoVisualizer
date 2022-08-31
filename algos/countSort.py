def countSort(arr, *args):
    size = len(arr)
    A = arr.copy()
    C = [0]*(max(A)+1)
    for i in range(size):
        C[A[i]] += 1
    for i in range(1, len(C)):
        C[i] += C[i-1]
    for i in range(0, size):
        yield arr, C[A[size-i-1]]-1, -1, size-i-1, -1
        arr[C[A[size-i-1]]-1] = A[size-i-1]
        C[A[size-i-1]] -= 1