def quicksort(inputArray):
    if len(inputArray) <= 1:
        return inputArray
    pivot = inputArray[-1]
    lesser = []
    greater = []
    for value in inputArray[:-1]:
        if value > pivot:
            greater.append(value)
        else:
            lesser.append(value)
    lesser = quicksort(lesser)
    greater = quicksort(greater)
    return lesser + [pivot] + greater


array1 = [1, 2, 3, 4, 5]  # worst case
array2 = [2, 4, 1, 3, 5]
array3 = [23, 44, 55, 2, 44, 30, 35, 11, -23, 40]
print quicksort(array1)
print quicksort(array2)
print quicksort(array3)
