import timeit

def M(start, end):
    summe = 0
    for i in range(start, end + 1):
        if prim(i) and mirp(i) and ones(i):
            summe += i
            print(i)
    return summe

def prim(n):
    if n < 2:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
    return True

def mirp(n):
    mirp = int(str(n)[::-1])
    
    if n != mirp and prim(mirp):
        return True
    else:
        return False
    
def ones(n):
    number = str(n)
    count = 0

    for i in number:
        if i == "1":
            count += 1
    
    if count == 2:
        return True
    else:
        return False

start = timeit.default_timer()
print(M(100, 1100))
stop = timeit.default_timer()
print('Time: ', stop - start)  



