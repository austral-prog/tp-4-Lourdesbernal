def leap_year():
        years=int(input("Ingrese un año: "))
        if years%400 == 0:
         print("El año"+" "+str(years)+" es bisiesto")
        elif years%4==0 and years%100!=0:
                print("El año"+" "+str(years)+" es bisiesto")
        else:
                print("El año"+" "+str(years)+" no es bisiesto")
