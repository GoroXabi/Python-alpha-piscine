from animal import Animal

class Granja:
	def __init__(self, total_water:int, total_food:int):
		self.__animals = []
		self.__total_water = total_water
		self.__total_food = total_food

	def nuevoAnimal(self, animal):
		self.__animals.append(animal)
	
	def conteoAnimal(self):
		return len(self.__animals)
	
	def sonidosEnLaGranja(self):
		for animal in self.__animals:
			print(f"{animal.getName()}, {animal.getType()}: ", end='')
			hacerSonido()

	def alimentarGranja(self):
		for animal in self.__animals:
			if animal.getConsumoBebida() < self.__total_water and animal.getConsumoComida() < self.__total_food:
				print(f"{animal.getName()} ({animal.getType()}) esta comiendo y bebiendo...")
				self.__total_food -= animal.getConsumoComida()
				animal.comer()				
				self.__total_water -= animal.getConsumoBebida()
				animal.beber()
			else:
				print(f"No hay suficientes recursos para alimentar a {animal.getName()} ({animal.getType()})")

	def getBebida(self):
		return self.__total_water

	def getComida(self):
		return self.__total_food
