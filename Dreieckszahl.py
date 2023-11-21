#Triangle numbers are numbers which sums up from natural number from 1 to n. Example: 10 = 1+2+3+4 or 15 = 1+2+3+4+5
"""
def is_triangular(x):
    triangular = False

    #Check if number is 0 or 1, these are triangle numbers by definition.
    if x in {0, 1}:
        triangular = True
    #If other number then 0 or 1 check with mathematical induction formular if x is triangle.
    else:
        for i in range(0, x):
            if (i*(i+1))/2 == x:
                triangular = True
                break
    return triangular"""