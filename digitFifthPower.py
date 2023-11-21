def digitfifthpower(n):
    expo = n
    maxvalue = expo * 9 ** expo   #Calculate the maxValue for iteration. For 5 it cannot be more than 5*9**5 = 295245
    summe = 0
    numbers = []

    #For loop goes through every number from 1 to maxvalue
    for i in range(1, maxvalue+1):
        #Call checkexpo function if True i will be added to summe else continue
        if checkexpo(i, expo):
            summe += i
            numbers.append(i)
        else:
            continue
    return numbers, summe


def checkexpo(n, expo):
    summe = 0

    #Calculate the sum of all powers
    for i in str(n):
        summe += int(i) ** expo

    #Check if the sum of all powers is equal to the given number n, function will return True
    if summe == n and summe != 1:
        return True
    else:
        return False


print(digitfifthpower(5))
