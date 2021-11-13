import os
import pickle as pk

global scores_recupere
scores = {
	'jean': 1,
	'Joachim': 3,
	'otrance': 190,
}

with open('score_data', 'wb') as fichier:
	scores_pickled = pk.Pickler(fichier)
	scores_pickled.dump(scores)

with open('score_data.txt', 'w') as fichier:
	fichier.write("je ne suis pas en train de m'amuser")

with open('score_data.txt', 'r') as fichier:
	contenu = fichier.read()
	print(contenu)

if __name__ == '__main__':
	print(os.chdir("K:\\Projects\\Python"))
	print(os.getcwd())

	with open('score_data', 'rb') as fichier:
		scores_unpickled = pk.Unpickler(fichier)
		scores_recupere = scores_unpickled.load()
	
	print(scores_recupere)
	print(scores_recupere['jean'])





