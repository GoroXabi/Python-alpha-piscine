from animal import Animal
from cerdo import Cerdo
from oveja import Oveja
from vaca import Vaca
from granja import Granja

def main():
	manolo = Oveja("Manolo")

	rosa = Cerdo("Rosa")

	arturo = Vaca("Arturo")

	humano = Animal("humano", "Yo")

	farm = Granja()

	farm.nuevoAnimal(manolo)
	farm.nuevoAnimal(rosa)
	farm.nuevoAnimal(arturo)
	farm.nuevoAnimal(humano)

	print(f"La granja tiene {farm.conteoAnimal()} animales")
	farm.sonidosEnLaGranja()

if __name__ == "__main__":
    main()