a=float(input("Introducir a: "))
b=float(input("Introducir b: "))
c=float(input("Introducir c: "))
a=0
b=1
while a<100:
    c=a+b
    a=b
    b=c
print(a)