def selection_sort(inputArray):
    """docstring for selection_sort"""
    sort_point = 0
    while sort_point < len(inputArray) - 1:
        minval = inputArray[sort_point]
        for i in range(len(inputArray[sort_point:])):
            index = i + sort_point
            value = inputArray[index]
            if value < minval:
                minval = value
                minindex = index
        if minval != inputArray[sort_point]:
            inputArray[minindex] = inputArray[sort_point]
            inputArray[sort_point] = minval
        sort_point += 1
    return inputArray


array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
array3 = [2, 4, 1, 5, 3]
array4 = [2, 2, 2, 2, 2]
print selection_sort(array1)
print selection_sort(array2)
print selection_sort(array3)
print selection_sort(array4)
