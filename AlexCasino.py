import os
from math import ceil
import random
import time
import pickle


with open('donnees', 'rb') as fichier:
	myDepickler = pickle.Unpickler(fichier)
	wallet = myDepickler.load()
continuer = True

while continuer == True:
	print("Bienvenue au \"Casino\" !")
	time.sleep(1)
	print("Vous êtes actuellement en possession de", wallet, "€ !")
	time.sleep(2)
	print("Vous pouvez continuer la partie en cours, ou vous pouvez réinitialiser votre porte-monnaie afin de revenir à zéro")
	resetWallet = str(input("Souhaitez-vous continuer la partie en cours ? (o/n) : "))
	if resetWallet.lower() == "n":
		wallet = 1000
		with open('donnees', 'wb') as fichier:
			myPickler = pickle.Pickler(fichier)
			myPickler.dump(wallet)
		continuer = False
	else:
		nombreChoisi = -1
		while nombreChoisi < 0 or nombreChoisi > 49:
			try:
				nombreChoisi = int(input("Veuillez sélectionner un nombre entre 0 et 49 : "))
			except:
				print("Une erreur est survenue, veuillez taper un nombre entre 0 et 49 !")
				continue

		mise = -1
		while mise <= 0 or mise > wallet:
			try:
				mise = int(input("Veuillez choisir une mise inférieure ou égale à la somme de votre porte-monnaie : "))
			except:
				print("Une erreur est survenue, veuillez recommencer !")
				continue

		nombreGagnant = random.randrange(50)
		time.sleep(1)
		print("Bien, la roue tourne...")
		time.sleep(2.3)
		if nombreChoisi == nombreGagnant:
			print("Bravo ! Vous avez choisi le bon numéro ! Vous récupérez votre mise et gagnez", mise * 3, "€")
			wallet = wallet + mise + mise * 3
		elif nombreChoisi % 2 == nombreGagnant % 2:
			print("Bravo ! Vous êtes tombé(e) sur la bonne couleur, vous récupérez votre mise et gagnez", ceil(mise * 0.5), "€")
			wallet = wallet + mise + ceil(mise * 0.5)
		else:
			print("Dommage, vous n'avez rien gagné...")
			wallet = wallet - mise
		print("Vous avez désormais", wallet, "€ dans votre porte-monnaie")
		if wallet == 0:
			print("Vous n'avez plus d'argent, la partie est terminée pour vous mon vieux !")
			continuer = False
		else:
			inputContinuer = input("Souhaitez-vous continuer ? (o/n) : ")
			if inputContinuer.lower() == "n":
				continuer = False
				with open('donnees', 'wb') as fichier:
					myPickler = pickle.Pickler(fichier)
					myPickler.dump(wallet)
			elif inputContinuer == "backdoor":
				ajoutWallet = int(input("Bravo, tu as trouvé la backdoor (pas difficile hein ?), combien veux-tu ajouter à ton wallet ? : "))
				wallet = wallet + ajoutWallet
				print("Bien, tu as ajouté", ajoutWallet, "dans ton porte-monnaie, tu as à présent", wallet, "€")
				continue
			else:
				continue

					
os.system("pause")