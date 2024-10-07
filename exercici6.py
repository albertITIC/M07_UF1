# Fet per: Albert Penadés Casajús

# Cal buscar la informació que es demana de la següent list:
# areas_pis = [“Menjador”, 10.15, “Rebedor”, 9.56, “Habitació1”, 12.34, “Terrassa”, 15.55, “Lavabo”, 7.98, “Cuina”, 12, “Habitació2”, 12.23]
# (Cal utilitzar els “:” per a que siguin vàlids els prints següents)

areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

# Imprimir el segon element
print("Segon element:")
print(areas_pis[1])
print("##############################################################################################################################################################\n")


# Imprimir l’últim element
print("Últim element:")
print(areas_pis[-1])
print("##############################################################################################################################################################\n")

# Imprimir l’àrea de la terrassa
print("Area terrassa:")
print(areas_pis[7])
print("##############################################################################################################################################################\n")

# Imprimir del primer element al tercer element
print("Del primer al tercer:")
print(areas_pis[0:3])
print("##############################################################################################################################################################\n")


# Imprimir del tercer element a l’últim
print("Del tercer al últim:")
print(areas_pis[2:])
print("##############################################################################################################################################################\n")


# Imprimir el total de l'àrea de les dues habitacions
print("Suma de les dues habitacions:")
print(areas_pis[5]+areas_pis[-1])
print("##############################################################################################################################################################\n")


# Modificar l’àrea del lavabo i imprimir la nova list area
print("Modificar l'area del lavabo:")
areas_pis[9]=10.5 # Primer assignem i després imprimim (no dexia fer-ho en una sola línia)
print(areas_pis)
print("##############################################################################################################################################################\n")


# Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions. Imprimir la nova list area.
print("Afegir pati interior i 2.78 a les ultimes posicions")
areas_pis.append("Pati interior")
areas_pis.append(2.78)
areas_pis.append(2.78)
print(areas_pis)
print("##############################################################################################################################################################\n")

# Imprimir el total de l’àrea del pis.
print("Total d'àrea del pis: ")
print(areas_pis[1] + areas_pis[3] + areas_pis[5] + areas_pis[7] + areas_pis[9] + areas_pis[11] + areas_pis[13])
print("##############################################################################################################################################################\n")
