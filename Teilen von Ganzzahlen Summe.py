def is_odd(x):
    result = None

    if x % 2 == 0:
        return False
    else:
        return True


def count_loop(x):
    count = 0;

    while is_odd(x) == False:
        count += 1
        x = x/2

    print(count)

count_loop(96)