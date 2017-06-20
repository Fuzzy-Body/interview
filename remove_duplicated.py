# coding: utf-8
# 给出一个列表，去掉重复的元素，并且保持原来的顺序
import timeit
from functools import partial


def merge(x, y):
    # print(x, y)
    if y not in x:
        return x + [y]
    else:
        return x


def use_reduce(the_list):
    # print(reduce(merge, [[], ] + the_list))
    print(reduce(lambda x, y: x + [y] if y not in x else x, [[], ] + the_list))


def use_set(the_list):
    tmp_set = set()
    result = []
    for item in the_list:
        if item not in tmp_set:
            result.append(item)
            tmp_set.add(item)
    print(result)


def analyse():
    result1 = timeit.timeit('_use_reduce', setup='from __main__ import _use_reduce')
    result2 = timeit.timeit('_use_set', setup='from __main__ import _use_set')
    print('use reduce: %s' % result1)
    print('use set: %s' % result2)


if __name__ == '__main__':
    print('----check func----\n')
    use_reduce([1, 2, 3, 1, 6, 10, 9, 4, 4, 3])
    use_set([1, 2, 3, 1, 6, 10, 9, 4, 4, 3])

    print('----compare efficiency----\n')
    the_list = range(10000) * 3
    _use_reduce = partial(use_reduce, the_list=the_list)
    _use_set = partial(use_set, the_list=the_list)
    analyse()
    print('---done----')
