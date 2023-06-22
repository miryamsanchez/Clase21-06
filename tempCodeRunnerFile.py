a=float(input("Introducir a: "))
b=float(input("Introducir b: "))
a=0
b=1
while a<100:
    c=a+b
    a=b
    b=c
print(a)