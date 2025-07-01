from game import GameManager
from granja import Granja
import os

game = GameManager(Granja())

def go_to_mercado():
	os.system('clear')
	choice = 0
	print("MERCADO")
	game.getMercado().printPrices()
	choice = input("Que quiere hacer?")
	while (choice != "0"):
		if choice == "1":
			game.getGranja().addComida(game.getMercado().getPrices()[choice][1])
def main():

	choice = 0
	while (choice != "0"):
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
		print("	0. Exit")
		print("	1. Alimentar a los animales")
		print("	2. Dormir y pasar al siguiente día")
		print("	3. Mostrar lista de animales")
		print("	4. Ir al mercado")
		choice = input("Elije una opción:")
		if (choice == "1"):
			game.getGranja().alimentarGranja()
		if (choice == "2"):
			game.passDay()
		if (choice == "3"):
			game.getGranja().showAnimals()
		if (choice == "4"):
			go_to_mercado()


if __name__ == "__main__":
    main()