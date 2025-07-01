from animal import Animal

class Vaca(Animal):
	def __init__(self, animal_name: str):
		Animal.__init__(self, "Vaca", "muuuuuu", animal_name)