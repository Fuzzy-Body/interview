# 腾讯面试

非常不爽，感觉没有感受到应有的尊重。电话面试了我半个小时，问了做过啥，什么做的好之类的，其中问了两道题

### type函数在三个参数的时候怎么用

`type`可以作为一个类的生成器来使用

```
BClass = type('B', (AClass, ), {'format': _format})
```

其中第一个参数是类名，第二个参数的tuple是父类，第三个参数，则是想要定义或者替换的属性或方法
我比较愤怒的是，问了这么一个还算偏门的东西。

### 取出列表中的重复元素，并且保持原有的顺序

我之前都是用reduce，因为方便而且快。

```
reduce(lambda x, y: x + [y] if y not in x else x, [[], ] + the_list
```

面试官给的答案是用一个中间set，因为 `in list`的算法复杂度是O(n)， `in set`的算法复杂度是O(1)

```
tmp_set = set()
result = []
for item in the_list:
    if item not in tmp_set:
        result.append(item)
        tmp_set.add(item)
```

我写了一个[脚本](https://github.com/Fuzzy-Body/interview/blob/master/remove_duplicated.py)来比较效率，虽然reduce更快一点，但是这个考的算是算法思路，我也认了。

我还是觉得我没有不合格的地方。
