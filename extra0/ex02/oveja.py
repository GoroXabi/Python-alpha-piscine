from animal import Animal


class Oveja(Animal):
	def __init__(self, animal_name: str):
		Animal.__init__(self, "Oveja", "baaaa", animal_name)
