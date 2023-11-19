#Task is from codewars.com You should find the element which occurs odd number of times.
def find_it(seq):
    count = 0
    element = 0

    for i in seq:
        if seq.count(i) > count and seq.count(i) % 2 != 0:
            element = i
            count = seq.count(i)
    return element

print(find_it([1,1,1,1,1,1,10,1,1,1,1]))