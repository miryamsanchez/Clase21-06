class Alumno:
    def __init__(self, nombre, ñotas=[]):
        self.nombre = nombre
        self.notas = ñotas[::]

    def añadir_nota(self,nota):
        if nota<0:
            return
        self.notas.append(nota)
    
    @property 
    def media(self):
        return sum(self.notas)/len(self.notas)
    
    def __str__(self):
        return self.nombre
    

if __name__=="__main__":
    a1 = Alumno("Juan")
    a2 = Alumno("Maria")
    a3 = Alumno("Luis")
    a1.añadir_nota(3.8)
    a1.añadir_nota(4.7)
    a1.añadir_nota(7.3)
    a2.añadir_nota(6.5)
    a2.añadir_nota(7.1)
    a2.añadir_nota(8.4)
    a3.añadir_nota(1.9)
    a3.añadir_nota(9.5)
    a3.añadir_nota(6.3)
    for alumno in [a1,a2, a3]:
        print("El alumno", alumno.nombre, "tiene nota media", alumno.media)
        print(f"El alumno {alumno} tiene nota media {alumno.media:.2f}")

