def get_fib(position):
    """docstring for get_fib"""
    if position < 0:
        return -1
    if position == 0 or position == 1:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)


def get_fib_list(position):
    if position < 0:
        return -1
    else:
        return [get_fib(x) for x in range(position + 1)]


print get_fib(0)
print get_fib(1)
print get_fib(-1)
print get_fib(2)
print get_fib(5)
print get_fib_list(0)
print get_fib_list(1)
print get_fib_list(-1)
print get_fib_list(10)
print get_fib_list(20)
