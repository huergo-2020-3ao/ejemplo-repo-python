
import random

nombre = input("Como te llamas? ")
edad = int(input("Cuantos años tenes? "))

edad_menos = random.randint(0, edad)
edad_mas = random.randint(edad, 100)

print ("Hola {}, ya cumpliste {} años no? ".format( 
	nombre, edad_menos))
print ("Pero todavia no cumpliste {}".format(
	edad_mas))
