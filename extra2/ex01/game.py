
from granja import Granja
from cerdo import Cerdo
from oveja import Oveja
from vaca import Vaca
from mercado import Mercado

class GameManager:
	def __init__(self, granja):
		self.__granja = granja
		self.__day = 0
		for n in range(0, 10):
			self.__granja.nuevoAnimal(Vaca(n))
		for n in range(0, 10):
			self.__granja.nuevoAnimal(Oveja(n))
		for n in range(0, 5):
			self.__granja.nuevoAnimal(Cerdo(n))
		self.__mercado = Mercado()

	def getGranja(self):
		return self.__granja

	def getMercado(self):
		return self.__mercado

	def getDay(self):
		return self.__day

	def passDay(self):
		self.__day += 1
		self.__granja.checkAnimals()
		for animal in self.__granja.getAnimals():
			animal.hunger()
