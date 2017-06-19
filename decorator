# coding: utf-8
# 实现一个装饰器，对函数重试，支持一个重试次数参数


class RetryExceedTimesError(Exception):
    pass


def retry(retry_time):
    def wrapper(_func):
        def wrapper2(*args, **kwargs):
            retry = 0
            while retry < retry_time:
                try:
                    _func(*args, **kwargs)
                    return
                except Exception as e:
                    error = e
                    print 'retry time %s' % retry
                    retry += 1
            raise RetryExceedTimesError(e)
        return wrapper2
    return wrapper


@retry(3)
def raise_error(x, y):
    raise ValueError('error')


@retry(3)
def normal(x, y):
    print 'here we are'


if __name__ == '__main__':
    normal(1, 2)
    raise_error(1, 2)
