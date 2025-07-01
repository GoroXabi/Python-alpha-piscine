from animal import Animal

class Cerdo(Animal):
	def __init__(self, animal_name: str):
		Animal.__init__(self, "Cerdo", "oink", animal_name)
