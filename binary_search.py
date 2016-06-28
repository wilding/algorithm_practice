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
        sublist = inputArray[:sorted_point]
        for index, value in enumerate(sublist):
            if index < sorted_point - 1 and value > sublist[index + 1]:
                greater = value
                lesser = sublist[index + 1]
                sublist[index] = lesser
                sublist[index + 1] = greater
                swap = True
                new_point = index + 1
        inputArray[:sorted_point] = sublist
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
