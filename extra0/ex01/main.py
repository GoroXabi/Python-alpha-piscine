from animal import Animal

def main():
	perro = Animal("dogi", "wofi")
	print(f"El {perro.getType()} hace ", end='')
	perro.hacerSonido()

	gato = Animal("chusta", "mau")
	print(f"El {gato.getType()} hace ", end='')
	gato.hacerSonido()

if __name__ == "__main__":
    main()