#Algorithm to search for lowest and highest number from input
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


#Calculate how often x can be divided by y and return result plus remainder from division
def division_mit_rest(x, y):
    count = 0
    remainder = 0

    while y <= x:
        count += 1
        x = x - y

    remainder = x
    return count, remainder


print(division_mit_rest(21, 4))
print(get_min_max(25, 12, 7, 90, 146, 2))