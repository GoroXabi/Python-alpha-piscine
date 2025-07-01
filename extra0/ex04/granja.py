from animal import Animal

class Granja:
	def __init__(self):
		self.__animals = []

	def nuevoAnimal(self, animal):
		self.__animals.append(animal)
	
	def conteoAnimal(self):
		return len(self.__animals)
	
	def sonidosEnLaGranja(self):
		for animal in self.__animals:
			print(f"{animal.getName()}, {animal.getType()}: ", end='')
			animal.hacerSonido()