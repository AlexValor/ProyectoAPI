import requests
import json

raiz= "http://www.omdbapi.com/?apikey=2cbd7158&"

print('Tipos de busqueda: ')
print()
print('1. Peliculas')
print('2. Series')
print('3. Otro tipo')
print('4. Salir')
print()

eleccion=int(input("Escoge una opción: "))
eleccion2=""

if eleccion == 1:
#Para hacer un request de peliculas solamente.
	buscar= input("Dime una película: ")
	peliculas=requests.get(raiz,
									params={'s':buscar,
									'type':'movie'}).json()

	for x in range (10):
		print(peliculas['Search'][x]['Title'])
		print("ID: ",peliculas['Search'][x]['imdbID'])
		print()

	buscarID= input("Dime un id anteriormente dados para conocer mas información: ")
	iddado=requests.get(raiz,
							params={'i':buscarID}).json()
	print()
	print("¿Que quieres saber de esta película?")
	print("1.Escritor y Director")
	print("2.Género")
	print("3.Premios")
	print("4.Año de estreno")
	print("5.Productora")
	print()

	eleccion2=int(input("Escoge una de las opciones: "))

	while eleccion2 != "salir":
		if eleccion2 == 1:	
			print("Escritor: ", iddado['Writer'])
			print("Director: ",iddado['Director'])
			break	
		elif eleccion2 == 2:
			print("Género: ",iddado['Genre'])
		elif eleccion2 == 3:
			print("Premios:",iddado['Awards'])	
		elif eleccion2 == 4:
			print("Fecha de estreno: ",iddado['Released'])
		elif eleccion2 == 5:
			print("Productora: ",iddado['Production'])	

elif eleccion == 2:
#Para hacer un request de series solamente.
	buscar=input("Dime una serie: ")
	print()
	series=requests.get(raiz,
								params={'s':buscar,
								'type':'series'}).json()
	
	for x in range (10):
		print(series['Search'][x]['Title'])
		print("ID: ",series['Search'][x]['imdbID'])
		print()

	buscarID= input("Dime un id anteriormente dados: ")
	iddado=requests.get(raiz,
							params={'i':buscarID}).json()

	print()
	print("¿Que quieres saber de esta serie?")
	print("1.Escritor y Director")
	print("2.Género")
	print("3.Premios")
	print("4.Año de estreno")
	print()

	eleccion2=int(input("Escoge una de las opciones: "))

	if eleccion2 == 1:	
		print("Escritor: ", iddado['Writer'])
		print("Director: ",iddado['Director'])
	elif eleccion2 == 2:
		print("Género: ",iddado['Genre'])
	elif eleccion2 == 3:
		print("Premios:",iddado['Awards'])	
	elif eleccion2 == 4:
		print("Fecha de estreno: ",iddado['Released'])
	else:
		print("Opción incorrecta")
#Para hacer un request sin tipo, ya que hay más generos a parte de las opciones dadas.
elif eleccion == 3:
	buscar=input("Dime un juego o episodio: ")
	general=requests.get(raiz,	
							params={'s':buscar}).json()
	
	for x in range (10):
		print(general['Search'][x]['Title'])
		print("ID: ",general['Search'][x]['imdbID'])
		print()

	buscarID= input("Dime un id anteriormente dados: ")
	iddado=requests.get(raiz,
							params={'i':buscarID}).json()

	print()
	print("¿Que quieres saber de la búsqueda?")
	print("1.Escritor y Director")
	print("2.Género")
	print("3.Premios")
	print("4.Año de estreno")
	print()
	eleccion2=int(input("Escoge una de las opciones: "))

	if eleccion2 == 1:	
		print("Escritor: ", iddado['Writer'])
		print("Director: ",iddado['Director'])
	elif eleccion2 == 2:
		print("Género: ",iddado['Genre'])
	elif eleccion2 == 3:
		print("Premios:",iddado['Awards'])	
	elif eleccion2 == 4:
		print("Fecha de estreno: ",iddado['Released'])
	elif eleccion2 == 5:
		print("Productora: ",iddado['Production'])
	else:
		print("Opción incorrecta")

elif eleccion == 4:
	print("¡Hasta luego!")	

else:
	print("Opción incorrecta")				

#PROBANDO EL FORMATO DEL JSON PELICULAS
#with open("peliculas.json", "w") as archivo: 
    #json.dump(peliculas,archivo,indent=4)

#for x in range (10):
	#if general['Search'][x]['Type'] == 'game':
		#print(general['Search'][x]['Title'],general['Search'][x]['Type'])


#buscarID= input("Dime un id anteriormente dados: ")
#idraro=requests.get(raiz,
							#params={'i':buscarID}).json()
#print(idraro['Genre'],idraro['Title'])

#PROBANDO EL FORMATO DEL JSON POR ID (CONTIENE MAS ESTADISTICAS)
#with open("peliculas.json", "w") as archivo: 
    #json.dump(idraro,archivo,indent=4)

