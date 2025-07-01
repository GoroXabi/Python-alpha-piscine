from animal import Animal


class Vaca(Animal):
	def __init__(self, animal_name: str):
		Animal.__init__(self, "Vaca", animal_name, 50, 80)

	def hacerSonido(self):
		print("muuuuuu")
