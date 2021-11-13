# Il s'agit ici de créer une fonction d'affichage avec des paramètres que
# l'on ne connait pas d'avance le nombre

def affichage(*chaine_caracters, sep = " ", fin = "\n"):
	"""
		Fonction chargée de reproduire le comportement de print.

		Elle doit finir par faire appel à print pour afficher le résultat.
		Mais les paramètres devront déjà avoir été formatés.
		On doit passer à print une unique chaîne, en lui spécifiant de ne
		rien mettre à la fin :
		print(chaine, end='')
	"""
	parameters = list(chaine_caracters)

	for i, item in enumerate(parameters):
		parameters[i] = str(item)

	chaine = sep.join(parameters)
	chaine += fin

	print('Voici votre chaine de caractère :')
	print(chaine, sep='')
	print('fin affichage')


if __name__ == '__main__':
	print("Veuillez donner un parametre à notre fonction affichage svp ")
	affichage('aaaaaa', 2, 3, "zazazazaza")
	my_list = [2, 3, 4, "zazaza", 'ezezeze']
	affichage(my_list)