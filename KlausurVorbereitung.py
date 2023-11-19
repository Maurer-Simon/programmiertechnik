"""
Implementieren Sie ein Programm das die Summe aller positiven Ganzzahlen berechnet, welche nicht die Ziffer 0 enthalten
und deren Quersumme exakt 5 ergibt. Überlegen Sie sich dazu zuerst wie groß die größte gesuchte Zahl maximal sein kann,
um eine Obergrenze für die Anzahl der zu untersuchenden Zahlen zu finden.
Zur Erinnerung: Die Quersumme einer Zahl ist die Summe ihrer Ziffern (z.B. Quersumme von 123 ist 1 + 2 + 3 = 6).
Achten Sie darauf Ihren Code möglichst vollständig zu kommentieren, um die Auswertung zu erleichtern.
Wenden Sie bei der Lösung dieser Aufgabe das Teile-und-Herrsche Prinzip an und zerlegen sie das Problem in leicht zu
lösende Teilprobleme, die sie getrennt voneinander lösen und am Ende für die Lösung des Gesamtproblems wieder zusammenfügen.
"""

def find_it(l, m):
    summe = 0

    for i in range(l, m+1):
        if checkEqual(i) == True:
            summe += i
    return summe


def toList(n):
    digits = []

    for digit in str(n):
        if digit == "0" or digit == "6" or digit == "7" or digit == "8" or digit == "9":
            digits = []
            return digits
        else:
            digits.append(int(digit))
    return digits

def checkEqual(n):
    sum = 0

    for j in toList(n):
        sum += j

    if sum == 5:
        return True
    else:
        return False




print(find_it(1, 11111))

"""
def is_zero(n):
    for num in str(n):  # Wir iterieren durch eine Zahl, die wir mit str() zu einem String casten
        if num == "0":  # und prüfen, ob der Character "0" enthalten ist.
            return True  # Wenn das zutrifft, geben wir True zurück.
    return False


# Als Nächstes widmen wir uns der Quersumme. Wieder casten wir die gegebene Zahl in einen String.
# An der Stelle achten wir aber noch nicht darauf, ob die Quersumme = 5 ist!
# Wir möchten einfach eine Funktion schreiben, die uns die Summe der Quersumme zurückgibt :)

def sum_digits(n):  # sum_of_digits hat eine Zahl n als Parameter.
    my_sum = 0  # In my_sum speichern wir die Summe unserer Quersummenberechnung.
    for digit in str(n):  # In der For-Loop wird zB die Zahl 542 in 5, 4 und 2 zerlegt.
        my_sum += int(digit)  # Die Zahl i wird wieder in ein Integer umgewandelt und zu my_sum hinzuaddiert.
    return my_sum  # Am Ende geben wir die Summe von z.B. 5 + 4 + 2 = 11 zurück.


# Nun können wir unsere letzte Funktion schreiben, in der wir is_zero und sum_digits einbauen und uns die Summe
# aller positiven Ganzzahlen ausgeben lassen können, die die Bedingungen erfüllen.
# Wir werden hier auch überprüfen, ob die Quersumme der jeweiligen Zahlen = 5 ist.

def calculate_solution():
    n = 11111  # 11111 = unsere Obergrenze
    m = 5  # 5 = unsere Bedingung für die Quersumme
    total = 0  # total wird am Ende ausgegeben; hier summieren wir alle Werte auf
    for nums in range(1, n + 1):
        if not is_zero(nums) and (sum_digits(nums) == m):
            total += nums
    return total


print(calculate_solution())"""