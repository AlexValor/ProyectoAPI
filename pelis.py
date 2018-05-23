import requests
import json
from colorama import Back, Style, Fore, init
init(autoreset=True)

raiz= "http://www.omdbapi.com/?apikey=2cbd7158&"

print(Fore.GREEN + Style.BRIGHT + 'Tipos de busqueda: ')
print()
print(Fore.BLUE + Style.BRIGHT + '1. Peliculas')
print(Fore.BLUE + Style.BRIGHT + '2. Series')
print(Fore.BLUE + Style.BRIGHT + '3. Otro tipo')
print(Fore.BLUE + Style.BRIGHT + '4. Salir')
print()

eleccion=int(input(Fore.GREEN + Style.BRIGHT+ "Escoge una opción: "))
eleccion2=""

if eleccion == 1:
#Para hacer un request de peliculas solamente.
	buscar= input(Fore.GREEN+ Style.BRIGHT +"Dime una película: ")
	peliculas=requests.get(raiz,
									params={'s':buscar,
									'type':'movie'}).json()

	for x in range (5):
		print(Fore.YELLOW + Style.BRIGHT +"Busquedas encontradas: ")
		print(Fore.BLUE + Style.BRIGHT + peliculas['Search'][x]['Title'])
		print(Fore.BLUE + Style.BRIGHT + "ID: ",peliculas['Search'][x]['imdbID'])
		print()

	buscarID= input(Fore.GREEN + Style.BRIGHT+"Dime un id anteriormente dados para conocer mas información: ")
	iddado=requests.get(raiz,
							params={'i':buscarID}).json()
	print()
	print(Fore.GREEN + Style.BRIGHT+"¿Que quieres saber de esta película?")
	print(Fore.BLUE + Style.BRIGHT +"1.Escritor y Director")
	print(Fore.BLUE + Style.BRIGHT +"2.Género")
	print(Fore.BLUE + Style.BRIGHT +"3.Premios")
	print(Fore.BLUE + Style.BRIGHT +"4.Año de estreno")
	print(Fore.BLUE + Style.BRIGHT +"5.Productora")
	print()

	eleccion2=input(Fore.GREEN + Style.BRIGHT +"Escoge una de las opciones: ")

	while eleccion2 != "salir":
		if eleccion2 == "1":	
			print(Fore.BLUE + Style.BRIGHT +"Escritor: ", iddado['Writer'])
			print(Fore.BLUE + Style.BRIGHT +"Director: ",iddado['Director'])
			print()
		elif eleccion2 == "2":
			print(Fore.BLUE + Style.BRIGHT +"Género: ",iddado['Genre'])
			print()
		elif eleccion2 == "3":
			print(Fore.BLUE + Style.BRIGHT +"Premios:",iddado['Awards'])	
			print()
		elif eleccion2 == "4":
			print(Fore.BLUE + Style.BRIGHT +"Fecha de estreno: ",iddado['Released'])
			print()
		elif eleccion2 == "5":
			print(Fore.BLUE + Style.BRIGHT +"Productora: ",iddado['Production'])
			print()	
		else:
			print(Fore.RED + Style.BRIGHT +"Opción incorrecta")
			print()
		eleccion2=input(Fore.GREEN + Style.BRIGHT +"Escoge una de las opciones. Teclee 'salir' para finalizar: ")
			
elif eleccion == 2:
#Para hacer un request de series solamente.
	buscar=input(Fore.GREEN+ Style.BRIGHT +"Dime una serie: ")
	print()
	series=requests.get(raiz,
								params={'s':buscar,
								'type':'series'}).json()
	
	for x in range(5):
		print(Fore.YELLOW + Style.BRIGHT +"Busquedas encontradas: ")
		print(Fore.BLUE + Style.BRIGHT + series['Search'][x]['Title'])
		print(Fore.BLUE + Style.BRIGHT +"ID: ",series['Search'][x]['imdbID'])
		print()

	buscarID= input(Fore.GREEN + Style.BRIGHT+"Dime un id anteriormente dados: ")
	iddado=requests.get(raiz,
							params={'i':buscarID}).json()

	print()
	print(Fore.GREEN + Style.BRIGHT+"¿Que quieres saber de esta serie?")
	print(Fore.BLUE + Style.BRIGHT +"1.Escritor y Director")
	print(Fore.BLUE + Style.BRIGHT +"2.Género")
	print(Fore.BLUE + Style.BRIGHT +"3.Premios")
	print(Fore.BLUE + Style.BRIGHT +"4.Año de estreno")
	print()

	eleccion2=input(Fore.GREEN + Style.BRIGHT +"Escoge una de las opciones: ")
	while eleccion2 != "salir":
		if eleccion2 == "1":	
			print(Fore.BLUE + Style.BRIGHT +"Escritor: ", iddado['Writer'])
			print(Fore.BLUE + Style.BRIGHT +"Director: ",iddado['Director'])
			print()
		elif eleccion2 == "2":
			print(Fore.BLUE + Style.BRIGHT +"Género: ",iddado['Genre'])
			print()
		elif eleccion2 == "3":
			print(Fore.BLUE + Style.BRIGHT +"Premios:",iddado['Awards'])
			print()
		elif eleccion2 == "4":
			print(Fore.BLUE + Style.BRIGHT +"Fecha de estreno: ",iddado['Released'])
			print()
		else:
			print(Fore.RED + Style.BRIGHT +"Opción incorrecta")
			print()
		eleccion2=input(Fore.GREEN + Style.BRIGHT +"Escoge una de las opciones. Teclee 'salir' para finalizar: ")
#Para hacer un request sin tipo, ya que hay más generos a parte de las opciones dadas.
elif eleccion == 3:
	buscar=input(Fore.GREEN+ Style.BRIGHT +"Dime un juego o episodio: ")
	general=requests.get(raiz,	
							params={'s':buscar}).json()
	
	for x in range (5):
		print(Fore.YELLOW + Style.BRIGHT +"Busquedas encontradas: ")
		print(Fore.BLUE + Style.BRIGHT + general['Search'][x]['Title'])
		print(Fore.BLUE + Style.BRIGHT +"ID: ",general['Search'][x]['imdbID'])
		print()

	buscarID= input(Fore.GREEN + Style.BRIGHT+"Dime un id anteriormente dados: ")
	iddado=requests.get(raiz,
							params={'i':buscarID}).json()

	print()
	print(Fore.GREEN + Style.BRIGHT+"¿Que quieres saber de la búsqueda?")
	print(Fore.BLUE + Style.BRIGHT +"1.Escritor y Director")
	print(Fore.BLUE + Style.BRIGHT +"2.Género")
	print(Fore.BLUE + Style.BRIGHT +"3.Premios")
	print(Fore.BLUE + Style.BRIGHT +"4.Año de estreno")
	print()

	eleccion2=input(Fore.GREEN + Style.BRIGHT +"Escoge una de las opciones: ")
	while eleccion2 != "salir":
		if eleccion2 == "1":	
			print(Fore.BLUE + Style.BRIGHT +"Escritor: ", iddado['Writer'])
			print(Fore.BLUE + Style.BRIGHT +"Director: ",iddado['Director'])
			print()
		elif eleccion2 == "2":
			print(Fore.BLUE + Style.BRIGHT +"Género: ",iddado['Genre'])
			print()
		elif eleccion2 == "3":
			print(Fore.BLUE + Style.BRIGHT +"Premios:",iddado['Awards'])
			print()	
		elif eleccion2 == "4":
			print(Fore.BLUE + Style.BRIGHT +"Fecha de estreno: ",iddado['Released'])
			print()
		elif eleccion2 == "5":
			print(Fore.BLUE + Style.BRIGHT +"Productora: ",iddado['Production'])
			print()
		else:
			print(Fore.RED + Style.BRIGHT +"Opción incorrecta")
			print()
		eleccion2=input(Fore.GREEN + Style.BRIGHT +"Escoge una de las opciones. Teclee 'salir' para finalizar: ")	

elif eleccion == 4:
	print(Fore.YELLOW + Style.BRIGHT +"¡Hasta luego!")	

else:
	print(Fore.RED + Style.BRIGHT +"Opción incorrecta")				

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

