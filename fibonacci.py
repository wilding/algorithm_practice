def get_fib(position):
    """docstring for get_fib"""
    if position < 0:
        return -1
    if position == 0 or position == 1:
        return position
    else:
        return get_fib(position - 1) + get_fib(position - 2)


def get_fib_list(position):
    """docstring for get_fib_list"""
    if position < 0:
        return -1
    if position == 0 or position == 1:
        return [x for x in range(position + 1)]
    else:
        fiblist = get_fib_list(position - 1)
        fiblist.append(fiblist[-1] + fiblist[-2])
        return fiblist


print get_fib(-1)
print [get_fib(x) for x in range(31)]
print get_fib_list(-1)
print get_fib_list(30)
