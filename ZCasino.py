# -*-coding:Latin-1 -*

# import random as rm
# import math as mt
from random import randrange
from math import ceil
import os

# Ici on recupere la somme misée du joueur et en meme temps le numero sur
# lequel il mise

somme_limit = 2500
continue_partie = True

# Tant que la personne dit qu'elle continue la partie, on recomence le processuce
while continue_partie:

	init_mise_nb = -1

	while init_mise_nb < 0 or init_mise_nb > 49:

		print("SVP veuillez entrer le nombre sur lequel vous voulez miser ")
		init_mise_nb = input()

		try:
			init_mise_nb = int(init_mise_nb)
		except ValueError:
			print("Vous n'avez pas entré un nombre")
			init_mise_nb = - 1
			continue

		if init_mise_nb < 0:
			print("Vous n'avez pas entré une valeur positive")
		elif init_mise_nb > 49:
			print("Vous devez entrer un nombre inférieur à 49 svp")


	init_mise_sm = -1
	while init_mise_sm < 0 or init_mise_sm > somme_limit:

		print("SVP veuillez entrer la somme sur laquel vous voulez miser ")
		init_mise_sm = input()

		try:
			init_mise_sm = int(init_mise_sm)
		except ValueError:
			print("Vous n'avez pas entré un nombre")
			init_mise_sm = - 1
			continue

		if init_mise_sm < 0:
			print("Vous n'avez pas entré une valeur positive")
		elif init_mise_sm > somme_limit:
			print("Vous devez entrer un nombre inférieur à {} svp".format(somme_limit))


	numero_alea = rm.randrange(50)

	if numero_alea == init_mise_nb:
		init_mise_sm += init_mise_sm*3
		print("Binnnnngooo, vous avez gagnez la partie à présent votre solde est de {} ".format(init_mise_sm))
	elif numero_alea%2 == init_mise_nb%2 or (numero_alea - 1)%2 == (init_mise_nb - 1)%2:
		init_mise_sm += mt.ceil(init_mise_sm*0.5)
		print("Vous n'avez pas gagner mais vous avez misé sur le bon numero. Pour cela vous gagnez {} $".format(init_mise_sm))
	else:
		print("Je suis navré de vous annoncer que vous avez perdu toute votre mise. Vous avez à présent 0 $")
		init_mise_sm -= init_mise_sm

	if init_mise_sm <= 0:
		print("Désolé la partie est fini, vous n'avez pas assez de sous pour continuer")
		continue_partie = False
	else:
		print("Vous avez à prsent {} à votre solde. Voulez vous continer ?".format(init_mise_sm))
		print("Tapez 'O' pour continuer et 'Q' pour quitter")
		quit_game = input()
		if quit_game.lower()=='q':
			print("Au revoir, au plaisir de vous revoir.")
			continue_partie  = False

os.system('pause')
