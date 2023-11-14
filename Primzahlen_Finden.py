#is_prime function is used to check if a number is a prime. i.e. only dividable by 1 or itself
def is_prime(x):
    prime = True

    for i in range(2, x): #if x can be divided by a number from 2 to x(counts till x-1, x itself is not included) without remainder x is not a prime
        if x % i == 0:
            prime = False
            break

    return prime


# search_prime counts up to a given number and stores every prime in a list
def search_prime(z):
    primes = []
    for i in range(2, z):
        if is_prime(i) == True:
            primes.append(i)
    return primes

print(search_prime(100))