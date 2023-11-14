#is_odd function is used to check if a number is odd
def is_odd(x):
    result = None

    if x % 2 == 0:
        return False
    else:
        return True

#count_loop increases count by 1 everytime x is divided by 2
def count_loop(x):
    count = 0;

    while is_odd(x) == False:
        count += 1
        x = x/2

    print(count)

count_loop(97)