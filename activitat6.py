# Author: Albert Penadés Casajús

# LOOPS: Mostrar els números de l’1 al 100 amb un while. Fer el mateix exercici amb for.
print("Apartat 6: ")
# Crear variable per recórrer el bucle
i=0
# WHILE: Mentres que i sigui més petit que 101 faré:
print("BUCLE WHILE:")
while i<101:
    print(i) # Imprimir i
    i+=1     # Per cada iteració sumo 1 al valor anterior.

#FOR
print("\nBUCLE FOR:")
for num in range (101):
    print(num)
