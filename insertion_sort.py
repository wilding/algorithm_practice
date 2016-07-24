def insertion_sort(inputArray):
    """docstring for insertion_sort"""
    for index in range(len(inputArray)):
        value = inputArray[index]
        position = index
        while position > 0 and inputArray[position-1] > value:
            inputArray[position] = inputArray[position-1]
            position = position - 1
        inputArray[position] = value
    return inputArray


array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
array3 = [2, 4, 1, 5, 3]
array4 = [2, 2, 2, 2, 2]
print insertion_sort(array1)
print insertion_sort(array2)
print insertion_sort(array3)
print insertion_sort(array4)
