import timeit

def dividableBy(n):
    dividable = False
    x = 1

    #While dividable is False the for loop will continue
    while dividable == False:
        #The for loop checks in the range from 1-20 if x is dividable by x.
        #If one statement is false the loop will break and 1 will be added to x
        for i in range(1, n+1):
            if x % i == 0:
                dividable = True
            else:
                dividable = False
                x += 1
                break
    return x


def ggt(x, y):
    if x == 0:
        return y
    else:
        return ggt(y % x, x)


def smallest_multiple_solution():
    sm_sum = 1

    for i in range(1, 21):
        sm_sum *= i // ggt(i, sm_sum)
    return sm_sum


def ggT(a, b):
    while b:
        a, b = b, a % b
    return a


def kgV(a, b):
    return a * b // ggT(a, b)


def kleinstes_gemeinsames_vielfache(start, end):
    if start == end:
        return start
    else:
        mid = (start + end) // 2
        left_lcm = kleinstes_gemeinsames_vielfache(start, mid)
        right_lcm = kleinstes_gemeinsames_vielfache(mid + 1, end)
        return kgV(left_lcm, right_lcm)

#----------------------------------------------

def flattenList(nestedList):
    if not(bool(nestedList)):
        return nestedList

    if isinstance(nestedList[0], list):
        return flattenList(*nestedList[:1]) + flattenList(nestedList[1:])

    return nestedList[:1] + flattenList(nestedList[1:])


def nested_sum(nested):
    sumList = 0
    x = flattenList(nested)
    for i in x:
        if type(i) == int:
            sumList += i
    return sumList

#----------------------------------------------

def S(m, d):
    sumNumbers = 0

    for i in range(1, m + 1):
        if sigma(i) % d == 0:
            sumNumbers += i
    return sumNumbers


def sigma(n):
    sumDivisor = 0
    for i in range(1, n+1):
        if n % i == 0:
            sumDivisor += i
    return sumDivisor

#----------------------------------------------

def M(n, m):
    mirpNums = []
    mirpSum = 0

    for i in range(n, m+1):
        if is_prim(i) and is_mirp(i) and two_zeros(i):
            mirpSum += i
            mirpNums.append(i)
    return mirpNums, mirpSum


def is_prim(n):
    if n == 2: return True
    elif n == 1 or n == 0: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def is_mirp(n):
    mirp = int(str(n)[::-1])
    if mirp == n:
        return False
    else:
        return is_prim(mirp)


def two_zeros(n):
    return str(n).count("1") == 2


print(M(100, 1100))

