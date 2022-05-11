# Ejercicio 2
# Enunciado del ejercicio:
# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, 
# lo guardaréis en un archivo y luego lo cargamos.


from copyreg import pickle
from  pickle import *

class Vehiculo():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def __str__(self):
        return f"Marca: {self.marca}\nColor: {self.color}"  

vehiculo1 = Vehiculo("Toyota", "Negro") 
print(vehiculo1)  

#Se crea el archivo pickle (Serializar)
datos_vehiculo = open("data_vehiculo", "w+b")
dump(vehiculo1, datos_vehiculo)

datos_vehiculo.seek(0)
data_vehiculo_nuevo = load(datos_vehiculo)

print(data_vehiculo_nuevo)
datos_vehiculo.close()


