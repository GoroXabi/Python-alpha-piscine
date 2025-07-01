from animal import Animal

class Cerdo(Animal):
	def __init__(self, animal_name: str):
		Animal.__init__(self, "Cerdo", animal_name, 30, 50)

	def hacerSonido(self):
		print("oink")

	def looseHp(self):
		self.setHp(self.getHp() - 35)