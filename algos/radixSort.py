def counting_Sort(arr, exp1):
    n = len(arr)
    output = []
    for i in range(0,n):
        output.append(arr[i])
    count = [0] * (10)
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int(index % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        yield output, count[int(index % 10)]-1, -1, int(index % 10), -1
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1
    i = 0
    if(arr != output):
        pass
    else:
        return 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
    del(output)


def radixSort(arr, *args):

    max1 = max(arr)
    g = 1
    exp = 1
    while max1 / exp > 0:
        g = yield from counting_Sort(arr, exp)
        if g==0:
            break
        exp *= 10