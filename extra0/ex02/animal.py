
class Animal:
	def __init__(self, animal_type: str, animal_sound: str, animal_name: str):
		self.__type = animal_type
		self.__sound  = animal_sound
		self.__name = animal_name
	
	def hacerSonido(self):
		print(self.__sound)

	def getType(self):
		return (self.__type)

	def getName(self):
		return (self.__name)
