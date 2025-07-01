from animal import Animal

class Granja:
	def __init__(self):
		self.__animals = []
		self.__total_water = 1000
		self.__total_food = 500

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
				animal.eat()
			else:
				print(f"No hay suficientes recursos para alimentar a {animal.getName()} ({animal.getType()})")

	def checkAnimals(self):
		for animal in self.__animals:
			if animal.getEaten() == False:
				animal.looseHp()
		self.__animals = [animal for animal in self.__animals if animal.getHp() > 0]

	def showAnimals(self):
		for animal in self.__animals:
			print(f"|{animal.getName()} {animal.getType()} : {animal.getHp()}hp", end='')
		print('')

	def getAgua(self):
		return self.__total_water

	def getComida(self):
		return self.__total_food

	def addAgua(self, to_add):
		self.__total_water += to_add
	
	def addComida(self, to_add):
		self.__total_food += to_add

	def getVacas(self):
		return len([animal for animal in self.__animals if animal.getType() == "Vaca"])

	def getOvejas(self):
		return len([animal for animal in self.__animals if animal.getType() == "Oveja"])
	
	def getCerdos(self):
		return len([animal for animal in self.__animals if animal.getType() == "Cerdo"])

	def getAnimals(self):
		return self.__animals