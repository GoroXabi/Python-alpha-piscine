
class Animal:
	def __init__(self, animal_type: str, animal_name: str, animal_hambre: int, animal_sed: int):
		self.__type = animal_type
		self.__name = animal_name
		self.__hambre = animal_hambre
		self.__sed = animal_sed
		self.__hp = 100
		self.__eaten = False
	
	def hacerSonido(self):
		print("AAAAAAAAA")

	def getType(self):
		return (self.__type)

	def getName(self):
		return (self.__name)

	def comer(self):
		print(f"{self.__name} ha comido {self.__hambre}kg de comida.")

	def beber(self):
		print(f"{self.__name} ha bebido {self.__sed}L de agua.")

	def getConsumoComida(self):
		return self.__hambre
	
	def getConsumoBebida(self):
		return self.__sed

	def getHp(self):
		return self.__hp

	def getEaten(self):
		return self.__eaten

	def eat(self):
		self.__eaten = True
		self.__hp = 100

	def hunger(self):
		self.__eaten = False

	def setHp(self, value):
		self.__hp = value

	def looseHp(self):
		self.__hp -= (self.__hp / 10)

