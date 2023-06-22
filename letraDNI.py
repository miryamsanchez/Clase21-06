def letra_DNI(num):
    resto = num % 23
    letras ="TRWAGMYFPDXBNJZSQVVHLCKE"
    return letras [resto]
num = int(input("Escriba su DNI sin letra: "))
print(letra_DNI(num))