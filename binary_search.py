def binary_search(input_array, value):
    """Same as index() but faster."""
    counter = 0
    while len(input_array) > 0:
        middle = len(input_array) / 2
        if value == input_array[middle]:
            return middle + counter
        elif value > input_array[middle]:
            if len(input_array) == 1:
                input_array = []
            else:
                counter += len(input_array[:middle])
                input_array = input_array[middle:]
        elif value < input_array[middle]:
            if len(input_array) == 1:
                input_array = []
            else:
                input_array = input_array[:middle]
    return -1




#################################   solution

def binary_search(listData, value):
    low = 0
    high = len(listData) - 1
    while low <= high:
        mid = (low + high) / 2
        if listData[mid] == value:
            return mid
        elif listData[mid] < value:
            low = mid + 1
        elif listData[mid] > value:
            high = mid + 1
    return -1




def get_fib(position):
    if position == 0 or position == 1:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)