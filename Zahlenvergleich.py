def get_min_max(a, b, c, d, e, f):
    _max_ = None
    _min_ = None
    values = [a, b, c, d, e, f]

    for i in values:
        if _max_ is None or i > _max_:
            _max_ = i

    for i in values:
        if _min_ is None or i < _min_:
            _min_ = i

    return _min_, _max_


def division_mit_rest(x, y):
    result = 0
    remainder = 0

    while y <= x:
        result += 1
        x = x - y

    remainder = x

    return result, remainder

division_mit_rest(21, 4)