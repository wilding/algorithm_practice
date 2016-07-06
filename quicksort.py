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
