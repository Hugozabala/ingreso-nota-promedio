from types import new_class
class ingreso:
    def __init__(self,nombre,carnet,carrera,nota):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.nota = nota

def menu():
  print("1. ingrese notas ")
  print("2. mostrar notas ")
  print("3. mostrar promedio")
  print("4. salir")


lista_estu =[]
menu()
op=int(input("INGRESE QUE OPCIÓN DESEA EJECUTAR"))
while op!= 4:
    match op:
        case 1:
            print("INGRESE DATOS DE ESTUDIÁNTE")
            no=input("INGRESE NOMBRE: ")
            car=input("INGRESE CARRERA: ")
            carrera=input("INGRESE CARRERA: ")
            nota=int(input("INGRESE NOTA: "))
            break
        case 2:
            print("LISTADO TOTAL DE NOTAS DE ESTUDIANTES ")
            break
        case 3:
            print("PROMEDIO DE NOTAS DE ESTUDIANTES ")
            break
        case 4:
            print("FIN DE PROGRAMA")
            break
        case _:
            print("OPCION INVALIDA")


