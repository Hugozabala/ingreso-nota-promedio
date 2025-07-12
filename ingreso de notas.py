from types import new_class


class ingreso:
    def __init__(self,nombre,carnet,carrera,nota):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.nota = nota

lista_estu =[]

nombre =input(f" ingrese nombre")
carnet=input("ingrese carnet")
carrera=input("ingrese carrera")
nota=input("ingrese nota")
cliente =new_class(nombre,carnet,carrera,nota)

lista_estu.append(cliente)
