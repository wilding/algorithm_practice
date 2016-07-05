def merge_sort(inputArray):
    if len(inputArray) <= 1:
        return inputArray

    mid = len(inputArray) / 2
    left = merge_sort(inputArray[:mid])
    right = merge_sort(inputArray[mid:])

    if left[-1] <= right[0]:
        return left + right
    if right[-1] <= left[0]:
        return right + left
    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    while left:
        result.append(left[0])
        left = left[1:]
    while right:
        result.append(right[0])
        right = right[1:]
    return result


array1 = [2, 4, 3, 5, 1]
array2 = [6, 8, 9, 3, 12, 999, 32, 498, 901]
array3 = [x for x in range(100)]
array4 = [4, 73, 23, 41, 97, 444, 75, 0, -34, 88, 88, 90, 345, 79]
print merge_sort(array1)
print merge_sort(array2)
print merge_sort(array3)
print merge_sort(array4)
