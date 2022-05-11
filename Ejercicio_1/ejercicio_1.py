# Ejercicio 1

# Enunciado del ejercicio:

# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. 
# Para ello, tendréis que acceder dos veces al archivo creado.

archivo = open("8-Entrada y salida datos\Ejercicios\Ejercicio_1\\archivo.txt", "w")
archivo.write("Estoy prendiendo python\n")
archivo.close()

archivo = open("8-Entrada y salida datos\Ejercicios\Ejercicio_1\\archivo.txt", "r+")
archivo.readlines()
archivo.write('Genial\n')

archivo.seek(0)
print(archivo.read())
archivo.close()