for ano in range (1800,2200):
    if ano%4==0 and ano%100 !=0 or ano%400==0:
        print(ano, "es bisiesto")