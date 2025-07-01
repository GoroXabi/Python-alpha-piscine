from animal import Animal


class Oveja(Animal):
	def __init__(self, animal_name: str):
		Animal.__init__(self, "Oveja", animal_name, 20, 30)

	def hacerSonido(self):
		print("baaaa")

	def looseHp(self):
		self.setHp(self.getHp() - 20)