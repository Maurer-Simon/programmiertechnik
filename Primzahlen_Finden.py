
def is_prime(x):
    prime = True

    for i in range(2, x):
        if x % i == 0:
            prime = False
            break

    return prime


def search_prime(z):
    for i in range(2, z):
        if is_prime(i) == True:
            print(i)

search_prime(197070)