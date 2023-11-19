#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

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


print(dividableBy(20))
#Result = 232792560
