def ggT(m, n):  #Größter gemeinsamer Teiler
    while m > 0:
        if m < n:
            m, n = n, m
            m = m - n
            ggT(m, n)
        else:
            m = m - n
            ggT(m, n)
    return n



def sum_digits(n):
    my_sum = 0
    for digit in str(n):
        my_sum += int(digit)
    return my_sum



def is_prime(num):
    if num < 2:  # Zahlen kleiner als 2 sind keine Primzahlen.
        return False
    for i in range(2, int(num ** 0.5) + 1):  # Durchlaufe potenzielle Teiler von 2 bis zur Wurzel der Zahl.
        if num % i == 0:  # Keine Primzahl, wenn durch i teilbar. Drum: False.
            return False
    return True



def reverse_number(num):
    int_str = str(num)  # Wir casten die Zahl in einen String und kehren ihn um.
    reversed_str = int_str[::-1]
    reversed_num = int(reversed_str)  # Wir casten den String wieder in eine Zahl.
    return reversed_num

def is_mirp(n):
    mirp = int(str(n)[::-1])
    return mirp

