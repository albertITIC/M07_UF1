# Author: Albert Penadés Casajús 

# Demanar a l’usuari que introdueixi 10 números separats per un espai. 
# Al acabar, el programa els introduirà en una tupla i els ordenarà (major o menor, com volgueu), 
# mostrant per pantalla el contingut de la tupla.

# Demano al usuari que introdueixi els números
nums = input("Introdueix una série de 10 números: ") # És un String que després li passaré un mètode que separi per ' ' (espais en blanc)

cadNums = nums.split() # Funció que ens separarà tots els números per subcadenes

# Itero per cada separació de números (en format cadena) i els passo a int (conversió de str a int)
cadNums = [int(num) for num in cadNums] 

# Crearé tupla a partir del la conversió de Strings a int
myTupla = tuple(cadNums) 

# Crearé una nova tulpa pero aquest cop ordenada passant-li la antigua com a paràmetre 
myTuplaOrdenada = tuple(sorted(myTupla))

# Imprimir resultats
print("Tupla ordenada: ")
print("-----------------")
print(myTuplaOrdenada)