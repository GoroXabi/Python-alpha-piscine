from animal import Animal
from cerdo import Cerdo
from oveja import Oveja
from vaca import Vaca
from granja import Granja

def main():
	manolo = Oveja("Manolo")

	rosa = Cerdo("Rosa")

	arturo = Vaca("Arturo")

	humano = Animal("humano", "Yo", 10, 10)

	farm = Granja(100, 100)

	farm.nuevoAnimal(manolo)
	farm.nuevoAnimal(rosa)
	farm.nuevoAnimal(arturo)
	farm.nuevoAnimal(humano)

	farm.alimentarGranja()

	print(f"Agua restante: {farm.getBebida()}L")
	print(f"Comida restante: {farm.getComida()}L")

if __name__ == "__main__":
    main()