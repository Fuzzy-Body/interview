# coding: utf-8
# 给定一个严格升序的列表li和num，使用二分法来找出num在li中的索引值，如果没有，就返回比这个刚刚好小的值，如果仍然没有，则返回None

def bin_find(li, num):
    def _iter(sub_li, index):
        if len(sub_li) == 1:
            if sub_li[0] >= num:
                return index
            else:
                return index - 1

        middle_index = len(sub_li) / 2
        middle_value = sub_li[middle_index]
        if middle_value == num:
            return index + middle_index
        elif middle_value < num:
            return _iter(sub_li[:middle_index])
        elif middle_value > num:
            return _iter(sub_li[middle_index:], index + middle_index)

    result = _iter(li, 0)
    return result if result >=0 else None


def assert_equal(value, expected):
    if value == expected:
        print('result is %s, right' % value)
    else:
        raise ValueError('found: %s, expected: %s, wrong' % (value, expected))


def test_bin_find():
    list1 = range(100)
    result = bin_find(list1, 50)
    assert_equal(result, list1.index(50))

    list2 = range(0, 100, 2)
    result = bin_find(list2, 32)
    assert_equal(result, list2.index(32))


    list3 = range(0, 100, 3)
    result = bin_find(list2, 32)
    assert_equal(result, list2.index(32))


if __name__ == '__main__':
    test_bin_find()
