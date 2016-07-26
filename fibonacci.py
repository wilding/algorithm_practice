def get_fib(position):
    """docstring for get_fib"""
    if position == 0 or position == 1:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)


fibarray = [get_fib(x) for x in range(21)]
print fibarray
