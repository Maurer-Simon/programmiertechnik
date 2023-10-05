
def is_prime(x):
    prime = True

    if x >= 2:
        for i in range(2, x):
            if x % i == 0:
                prime = False
                break

        print(prime)
    else:
        print("Variable x muss eine natürliche Zahl größer als 1 sein.")

is_prime(197059)
