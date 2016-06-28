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

#######   Sorting   #######

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


#def merge_sort():
#def quick_sort():



#def timsort():
#def heap_sort():
#def insertion_sort():
#def selection_sort():
#def shell_sort():
#def bucket_sort():
#def radix_sort():
