# list : append, len, del, insert, enumarate, remove
# Split and join

def affichage_floattant(nombre:float):

	if type(nombre) is not float:
		raise TypeError("Le nombre que vous avez entré n'est pas un float ni un double")

	nombre_str = str(nombre)
	entier, decimal = nombre_str.split(".")
	return ",".join([entier, decimal[:2]])


if __name__ == '__main__':
	print("Veuillez donner un nombre double svp")
	print(affichage_floattant(float(input())))

