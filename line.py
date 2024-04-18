def line():
        import math
        a=float(input("Ingrese el coeficiente A: "))
        b=float(input("Ingrese el coeficiente B: "))
        x1=float(input("Ingre el coeficiente x1: "))
        x2=float(input("Ingre el coeficiente x2: "))

        y1=a*x1+b
        y2=a*x2+b

        print(f"""El coeficiente A de su ecuacion de la recta es: {a}
    El coeficiente B de su ecuacion de la recta es: {b}
    El coeficiente X1 de su ecuacion de la recta es: {x1}
    El coeficiente X2 de su ecuacion de la recta es: {x2}""")
        print(f"""\nPara la siguiente ecuacion:
        Y = {a}x + {b}""")
        print(f"""\nDados los siguientes puntos:
        P1 ({x1}, {y1})
        P2 ({x2}, {y2})""")

        d= math.sqrt((x2-x1)**2 + (y2-y1)**2)

        print(f"\nLa distancia entre ellos es: {d}")
