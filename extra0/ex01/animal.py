
class Animal:
	def __init__(self, animal_type: str, animal_sound: str):
		self.__type = animal_type
		self.__sound  = animal_sound
	
	def hacerSonido(self):
		print(self.__sound)

	def getType(self):
		return (self.__type)

