# coding: utf-8
# n个有序数组，n个有序数据按照由大到小排列

the_first = lambda x: x[0]


def _get_max(*args):
    to_get = filter(lambda x: x, args)
    the_one = max(to_get, key=the_first)
    result = the_one[0]
    del the_one[0]
    return result


def _iter(*args):
    result = []
    while True:
        result.append(_get_max(*args))
        if not filter(None, args):
            break
    return result


if __name__ == '__main__':
    a = [3, 2, 1]
    b = [4, 3, 2, 1]
    c = [5, 4, 2, 1]
    print _iter(a, b, c)
