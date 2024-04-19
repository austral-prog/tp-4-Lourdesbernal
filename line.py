import math
def line():
        
        a=float(input("Ingrese el coeficiente A:"))
        b=float(input("Ingrese el coeficiente B:"))
        X1=float(input("Ingre el coeficiente X1:"))
        X2=float(input("Ingre el coeficiente X2:"))
        Y1=float(a*X1+b)
        Y2=float(a*X2+b)
        P1=[X1 , Y1]
        P2=[X2 , Y2]

        print(f"El coeficiente A de su ecuacion de la recta es: {a}")
        print(f"El coeficiente B de su ecuacion de la recta es: {b}")
        print(f"El coeficiente X1 de su ecuacion de la recta es: {X1}")
        print(f"El coeficiente X2 de su ecuacion de la recta es: {X2}")
        print()
        print("Para la siguiente ecuacion:")
        print(f"\tY = {a}x + {b}")
        print()
        print(Dados los siguientes puntos:")
        print(f"\tP1 ({X1}, {Y1})")
        print(f"\tP2 ({X2}, {Y2})")
        print()
        print("La distancia entre ellos es: " + str(math.dist(P1, P2)))
