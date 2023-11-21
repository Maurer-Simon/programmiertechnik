def S(k):
    summe = 0
    for i in range(1, k+1):
        summe += f(i, i**2)
    return summe

def f(n, m):
    quer = []
    count = 0
    while len(quer) < m:
        if summe_digits(count) == n:
            quer.append(count)
        count += 1
    return quer[-1]

def summe_digits(n):
    summe = 0
    for i in str(n):
        summe += int(i)
    return summe

print(S(10))
