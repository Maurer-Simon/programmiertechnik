def is_prime(x):
    prime = True

    for i in range(2, x):
        if x % i == 0:
            prime = False
            break

    print(prime)

is_prime(2)