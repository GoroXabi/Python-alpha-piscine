from animal import Animal


class Oveja(Animal):
	def __init__(self, animal_name: str):
		Animal.__init__(self, "Oveja", animal_name)

	def hacerSonido(self):
		print("baaaa")
