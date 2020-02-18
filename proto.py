# JS style functions


def _checkIter(list_):
    try:
        _ = (e for e in list_)
    except TypeError:
        raise Exception(list_, 'is not iterable')
        return None


# JS array.prototype.every equivalent (ES6)
def every(list_, pred):
    _checkIter(list_)
    return all(pred(x) for x in list_)


# JS array.prototype.some equivalent (ES6)
def some(list_, pred):
    _checkIter(list_)
    return any(pred(x) for x in list_)


# JS array.prototype.filter equivalent (ES6)
def filter(list_, pred):
    _checkIter(list_)
    return [x for x in list_ if pred(x)]


# JS array.prototype.find equivalent (ES6)
def find(list_, pred):
    _checkIter(list_)
    for x in list:
        if pred(x):
            return x
            break
        else:
            x = None


# JS array.prototype.findIndex equivalent (ES6)
def findIndex(list_, pred):
    _checkIter(list_)
    for x, i in enumerate(list):
        if pred(x):
            return i
            break
        else:
            i = None


# returns indexes
def findIndexes(list_, pred):
    _checkIter(list_)
    return [i for i in range(len(list_)) if pred(list_[i])]
