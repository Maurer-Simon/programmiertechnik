# Mit dieser Funktion wird berechnet, ob eine Zahl eine Dreieckszahl ist.

def is_triangular(x):
    triangular = False

    if x in {0, 1}:
        triangular = True
    else:
        for i in range(0, x):
            if (i*(i+1))/2 == x:
                triangular = True

    print(triangular)


is_triangular(14)