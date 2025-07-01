
class Mercado:
	def __init__(self):
		self.__precios = {"1" : ["Comida", 10, "Kg", 100],
					"2" : ["Agua", 10, "L", 55]}
	def printPrices(self):
		for item, info in self.__precios.items():
			print(f"{item} {info[0]}: {info[1]}{info[2]} - {info[3]} monedas")
	
	def getPrices(self):
		return self.__precios