def generar_sala(filas, columnas):
    #Ciclo para generar la matriz (sala) de las medidas indicadas por el usuario.
    #La matriz se crea llena de ceros para posteriormente reemplazar por "X"
    #la posición indicada por el usuario.
    #En este punto aún no se muestra la matriz al usuario.
    sala = [['O' for _ in range(columnas)] for _ in range(filas)]
    return sala

def mostrar_sala(sala):
    #Ciclo que recorre la matriz por filas y la imprime alternando espacios
    #con las posiciones de la matriz (0 o X si la posición ya está ocupada).
    #Con el método join se inserta el "0" o la "X" alternado con los espacios,
    #para así mostrar la matriz en su estado actual.
    for fila in sala:
        print(' '.join(fila))

def asignar_posicion(sala, fila, columna):
    #Se comprueba si el asiento (fila, columna) está libre (es 0)
    #y de no estarlo se asigna al usuario (X)
    if sala[fila][columna] == 'O':
        sala[fila][columna] = 'X'
        return True
    else:
        return False

def opciones_disponibles(sala):
    #Ciclo que recorre la matriz sala (pasada como parámetro a la función "opciones disponibles")
    #y compara filas y columnas (si la posición [i][j] es igual a 0), para así generar otra vez
    #una matriz pero con los asientos disponibles (disponibles)
    disponibles = []
    for i in range(len(sala)):
        for j in range(len(sala[0])):
            if sala[i][j] == 'O':
                disponibles.append((i, j))
    return disponibles

#Medainte la linea if __name__ == "__main__": main() ubicada la final del código
#Se da la instrucción de ejecutar primero ésta función
def main():
    #Se piden las medidas que tendrá la matriz generada
    filas = int(input("Ingrese el número de filas para la sala de cine: "))
    columnas = int(input("Ingrese el número de columnas para la sala de cine: "))

    #Se emplea la función "generar_sala" para crear la matriz con las dimensiones indicadas
    sala = generar_sala(filas, columnas)
    #Se emplea la función "mostrar_sala" para mostrar la matriz
    mostrar_sala(sala)

    while True:
        #Se pregunta al usuario si desea asignar un asiento.
        #Con el método "lower" se cerciora de que así se ingresen letras minúsculas o mayúsculas
        #siempre van a ser convertidas a minúsculas para evitar error
        opcion = input("\n¿Desea asignar un asiento? (s/n): ").lower()
        if opcion == 's':
            disponibles = opciones_disponibles(sala)
            if disponibles:
                print("\nPosiciones disponibles:")
                #Ciclo para mostrar las posiciones disponibles
                for pos in disponibles:
                    print(f"Fila: {pos[0]}, Columna: {pos[1]}")

                #Se le pide al usuario que ingrese la fila del asiento que desea ocupar
                fila = int(input("\nIngrese la fila: "))

                #Se le pide al usuario que ingrese la columna del asiento que desea ocupar
                columna = int(input("Ingrese la columna: "))

                #Se comprueba que la posción indicada por el usuario sea "0" (esté libre)
                if 0 <= fila < filas and 0 <= columna < columnas:
                    #Al llamar la función "asignar_posición" se comprueba
                    #si el asiento (fila, columna) está libre (es 0).
                    #De sí estarlo, se muestra al usuario el mensaje "Asiento asignado con éxito"
                    if asignar_posicion(sala, fila, columna):
                        print("\nAsiento asignado con éxito.")
                        mostrar_sala(sala)
                    else:
                        #Si el asiento no está disponible (la posición de la matriz es "X")
                        #se muestra el siguiente mensaje al usuario
                        print("\nLo sentimos, ese asiento ya está ocupado.")
                else:
                    print("\nPosición fuera de rango. Intente de nuevo.")
            else:
                print("\nLo sentimos, no hay asientos disponibles.")
        elif opcion == 'n':
            print("\nGracias por utilizar el sistema de asignación de asientos.")
            break
        else:
            print("\nOpción no válida. Por favor, ingrese 's' o 'n'.")

#La ejecución se inicia en la función main()
if __name__ == "__main__":
    main()