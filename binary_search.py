def binary_search(listData, value):
    """docstring for binary_search"""
    low = 0
    high = len(listData) - 1
    while low <= high:
        mid = (low + high) / 2
        if listData[mid] == value:
            return mid
        elif listData[mid] < value:
            low = mid + 1
        elif listData[mid] > value:
            high = mid - 1
    return -1

# Testing
array1 = [x for x in range(16)]
print binary_search(array1, 0)
print binary_search(array1, 15)
print binary_search(array1, 8)
print binary_search(array1, -1)  # worst case
print binary_search(array1, 16)  # worst case
print binary_search(array1, 80)  # worst case
