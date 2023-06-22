from math import sqrt
def raiz_cuadrada_inversa(x):
    if x<=0:
        raise ValueError("Debe ser positivo")
    return 1/sqrt(x)
    