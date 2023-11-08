def digits_factorial(n):
    sumdigits = 0

    
    for i in reversed(range(3,n+1)):
        strdigits = str(i)
        length = len(strdigits)
        digits = []
        sumfactorials = 0

        while length > 0:
            digits.append(int(strdigits[0]))
            strdigits = strdigits[1: length]
            length -= 1
        
  
        for j in digits:
            if j == 0:
                sumfactorials +=1
            elif j > 0:
                z = 1
                for k in range(1,j+1):
                    z = z * k
                sumfactorials += z

        if sumfactorials == i:
            sumdigits += i
    
    return sumdigits

    

print(digits_factorial(500000))

"""def digits_factorial(n):
    sumfactorials = 0

    for i in reversed(range(3,n+1)):
        if factorial(i) == i:
            sumfactorials += i
        
    return sumfactorials  
    

        
def factorial(n):
    digits = split(n)
    summe = 0

    for i in digits:
        if i == 0:
            summe +=1
        elif i > 0:
            y = 1
            for j in range(1,i+1):
                y = y * j
            summe += y
    return summe


def split(n):
    text = str(n)
    liste = []
    y = len(text)
    
    while text != "":
        liste.append(int(text[0]))
        text = text[1: y]
    return liste"""