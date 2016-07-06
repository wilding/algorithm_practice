def quicksort(inputArray):
    if len(inputArray) <= 1:
        return inputArray
    pivot = inputArray[-1]
    lesser = []
    greater = []
    equal = []
    for value in inputArray[:-1]:
        if value > pivot:
            greater.append(value)
        elif value < pivot:
            lesser.append(value)
        elif value == pivot:
            equal.append(value)
    lesser = quicksort(lesser)
    greater = quicksort(greater)
    # print inputArray
    return lesser + equal + [pivot] + greater


def in_place_quicksort(inputArray):
    if len(inputArray) <= 1:
        return inputArray
    pivot_index = len(inputArray) - 1
    for index in range(len(inputArray)):
        if index >= pivot_index:
            break
        while inputArray[index] > inputArray[pivot_index]:
            value = inputArray[index]
            pivot = inputArray[pivot_index]
            if index == pivot_index - 1:
                before = pivot
            else:
                before = inputArray[pivot_index - 1]
            inputArray[pivot_index] = value
            inputArray[pivot_index - 1] = pivot
            inputArray[index] = before
            pivot_index -= 1
    inputArray[:pivot_index] = in_place_quicksort(inputArray[:pivot_index])
    inputArray[pivot_index + 1:] = in_place_quicksort(inputArray[pivot_index + 1:])
    # print inputArray
    return inputArray


array1 = [1, 2, 3, 4, 5]  # worst case - quadratic
array2 = [2, 4, 1, 3, 5]  # avg case - linearithmic
array3 = [2, 2, 2, 2, 2]  # best case - linear
array4 = [2, 7, 6, 3, 5]
array5 = [2, 7, 6, 8, 5]
print quicksort(array1)
print quicksort(array2)
print quicksort(array3)
print quicksort(array4)
print quicksort(array5)
