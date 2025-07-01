from animal import Animal

class Cerdo(Animal):
	def __init__(self, animal_name: str):
		Animal.__init__(self, "Cerdo", animal_name)

	def hacerSonido(self):
		print("oink")
