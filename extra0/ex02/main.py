from animal import Animal
from cerdo import Cerdo
from oveja import Oveja
from vaca import Vaca

def main():
	manolo = Oveja("Manolo")
	print(f"{manolo.getName()} es una {manolo.getType()} y hace ", end='')
	manolo.hacerSonido()

	rosa = Cerdo("Rosa")
	print(f"{rosa.getName()} es una {rosa.getType()} y hace ", end='')
	rosa.hacerSonido()


	arturo = Vaca("Arturo")
	print(f"{arturo.getName()} es una {arturo.getType()} y hace ", end='')
	arturo.hacerSonido()


if __name__ == "__main__":
    main()