from game import GameManager
from granja import Granja
import os

def main():

	choice = 0
	game = GameManager(Granja())
	while (choice != "3"):
		#os.system('clear')
		print("LOCURAS EN LA GRANJA")
		print("Día", game.getDay())
		print("RECURSOS ACTUALES")
		print("- Animales")
		print(f""" - Vacas: {game.getGranja().getVacas()} 
 - Ovejas: {game.getGranja().getOvejas()} 
 - Cerdos: {game.getGranja().getCerdos()}""")
		print("- Alimento")
		print(f""" - Comida: {game.getGranja().getComida()}Kg
 - Agua: {game.getGranja().getAgua()}L""")

		print("¿Qué quieres hacer?")
		print("	1. Alimentar a los animales")
		print("	2. Dormir y pasar al siguiente día")
		print("	3. Exit")
		choice = input("Elije una opción:")
		if (choice == "1"):
			game.getGranja().alimentarGranja()
		if (choice == "2"):
			game.passDay()


if __name__ == "__main__":
    main()