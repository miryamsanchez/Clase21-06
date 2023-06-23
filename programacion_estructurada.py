alumnos=["Juan", "Maria", "Luis"]
notas=[[3.8, 4.7 , 7.3],[6.5, 7.1, 8.4],[1.9, 9.5 , 6.3]]
def media_alumno(notas):
    return sum(notas)/len(notas)

if __name__=="__main__":
    for i in range(len(alumnos)):
        print("La nota media de ", alumnos[i], "es", media_alumno(notas[i]))
