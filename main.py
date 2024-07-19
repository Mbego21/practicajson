import json

def datos_guardados(contenido):
    with open("alumnos.json", "r") as file:
        json.dump(contenido,file)

def buscar_alumnos(cedula):
    with open("alumnos.json","r") as file:
        contenido = json.load(file)
        alumnos = contenido["data"]

        for estudiantes in alumnos:
            if estudiantes["cedula"] == cedula:
                return estudiantes
        return None
    
def eleccion_alumno(cedula, nombre, apellido, nota1, nota2, nota3):
    with open("alumnos.json", "r+") as file:
        contenido= json.load(file)
        alumnos = contenido["data"]
        l=len(file)
        for i in range(l):
            for estudiantes in enumerate(alumnos):
                if estudiantes["cedula"] == cedula:
                    alumnos[i]["nombre"]== nombre
                    alumnos[i]["apellido"]== apellido
                    alumnos[i]["nota1"]== nota1
                    alumnos[i]["nota2"]== nota2
                    alumnos[i]["nota3"]== nota3

                    file.seek(0)
                    json.dump(contenido, file, indent=5)
                    print(f"alumno con cedula {cedula} corregido correctamente")
                    return
                print(f"no se encontro con alumno con cedula {cedula} ")

def correcion_alumno():
    cedula = input("ingrese la cedula del alumno que desea encontrar: ")
    estudiante = buscar_alumnos(cedula)

    if estudiante:
        print(f"alumno encontrado: {estudiante["nombre"]} + {estudiante["apellido"]}")

        correccion_nombre = input("ingrese el nombre corregido:")
        correcion_apellido = input("ingrese el apellido corregido:")

        nuevas_notas = []
        while True:
            nueva_nota = float(input("ingrese la nueva nota:"))
            nuevas_notas.append({"nota": nueva_nota})

     