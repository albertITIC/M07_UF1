# Author: Albert Penadés Casajús
# Demanar a l’usuari un nùmero entre 10 i 100. Posar els números a una tupla desde 1 fins al número indicat per l’usuari. 
# Exemple: usuari indica 34, es crea una tupla i es mostra per pantalla els números de l’1 al 34 (imprimint la tupla).


# Creo una variable per guardar el número (faré un cast per forçar el tipus de variable)
num = int(input("Introdueix un número entre el 10 i el 100: "))

# Crear un rang (per si es troba entre el 10 i el 100)
if num >= 10 and num <=100:
    # Crear tupla a partir del rang establert més el número que introdueix el nostre usuari
    la_meva_tupla = tuple(range(10, num+1))
    print(la_meva_tupla)
else:
    print("Error. Número introduït no es troba dins del rang")
