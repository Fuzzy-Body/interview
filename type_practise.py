# coding: utf-8
# type的用法


class AClass(object):

    def __init__(self, name):
        self.name = name

    def format(self):
        return 'the name is %s' % self.name

    def __repr__(self):
        repr = super(AClass, self).__repr__()
        repr = repr.replace(self.__class__.__name__,
                            self.__class__.__name__ + ' name: ' + self.name)
        return repr


def _format(self):
    return 'I do not want to tell you'


BClass = type('B', (AClass, ), {'format': _format})


if __name__ == '__main__':
    a = AClass('Allen')
    b = BClass('Benny')

    print('---to print format--\n')
    print(a.format())
    print(b.format())

    print('---to print repr---\n')
    print(a)
    print(b)

    print('---end---')
