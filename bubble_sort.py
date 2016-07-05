def bubble_sort(inputArray):
    swap = True
    sorted_point = len(inputArray)
    new_point = None
    while swap and sorted_point > 1:
        swap = False
        for index in range(sorted_point):
            value = inputArray[index]
            if index == sorted_point - 1:
                next_value = None
            else:
                next_value = inputArray[index + 1]
            if next_value and value > next_value:
                inputArray[index] = next_value
                inputArray[index + 1] = value
                swap = True
                new_point = index + 1
        sorted_point = new_point
    return inputArray
