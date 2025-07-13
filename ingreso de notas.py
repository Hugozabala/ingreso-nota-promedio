class ingreso:
    def __init__(self, nombre, carnet, carrera, nota):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.nota = nota


def menu():
    print("1. ingrese notas ")
    print("2. mostrar notas ")
    print("3. mostrar promedio")
    print("4. salir")


lista_estu = []
suma = 0
promedio = 0
cont = 0
menu()
op = int(input("INGRESE QUE OPCIÓN DESEA EJECUTAR"))
while op != 4:
    match op:
        case 1:
            while True:
                respuesta = input("deseas ingresar otro estudiante(s/n)")
                if respuesta == "n":
                    print("Programa finalizado")
                    break
                else:

                    print("INGRESE DATOS DE ESTUDIÁNTE")
                    no = input("INGRESE NOMBRE: ")
                    car = input("INGRESE CARRERA: ")
                    carrera = input("INGRESE CARRERA: ")
                    nota = int(input("INGRESE NOTA: "))
                    suma += nota
                    cont += 1
                    promedio = (suma / cont)
                    estudiante = ingreso(no, car, carrera, nota)
                    lista_estu.append(estudiante)

        case 2:
            if len(lista_estu) == 0:
                print("no hay estudiantes ingresados ")

            else:
                print("LISTADO TOTAL DE NOTAS DE ESTUDIANTES ")
                for estudiante in lista_estu:
                    print(estudiante)
        case 3:
            print("PROMEDIO DE NOTAS DE ESTUDIANTES ")
            print(promedio)
            break
        case 4:
            print("FIN DE PROGRAMA")
            break
        case _:
            print("OPCIÓN INVALIDA")


