#This is not yet resolved.

def mergeSort(arr, ascending=True):
    #array = view.lst
    array = arr
    if len(arr) > 1:
        mid = len(arr) // 2
        left = array[:mid]
        right = array[mid:]

        mergeSort(left)
        mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                #draw_list(view, {k: constants.BLUE, i: constants.GREEN}, True)
                #yield True
                i += 1
            else:
                array[k] = right[j]
                #draw_list(view, {k: constants.BLUE, j: constants.GREEN}, True)
                #yield True
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            #draw_list(view, {k: constants.BLUE, i: constants.GREEN}, True)
            #yield True
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            #draw_list(view, {k: constants.BLUE, j: constants.GREEN}, True)
            #yield True
            j += 1
            k += 1
    return(array)