import requests
import json

raiz= "http://www.omdbapi.com/?apikey=2cbd7158&"

print('Tipos de busqueda: ')
print('1. Peliculas')
print('2. Series')
print('3. Otro tipo')
eleccion=int(input("Escoge una opción: "))

if eleccion == 1:
#Para hacer un request de peliculas solamente.
	peliculas=requests.get(raiz,
								params={'s':buscar,
								'type':'movie'}).json()

	buscar= input("Dime una película: ")
	for x in range (10):
		print(peliculas['Search'][x]['Title'],peliculas['Search'][x]['imdbID'])

		buscarID= input("Dime un id anteriormente dados: ")
		iddado=requests.get(raiz,
								params={'i':buscarID}).json()
		print(iddado['Genre'],iddado['Title'])

elif eleccion == 2:
#Para hacer un request de series solamente.
	series=requests.get(raiz,
								params={'s':buscar,
								'type':'series'}).json()
	buscar=input("Dime una serie: ")
	for x in range (10):
		print(series['Search'][x]['Title'],series['Search'][x]['imdbID'])

		buscarID= input("Dime un id anteriormente dados: ")
		iddado=requests.get(raiz,
									params={'i':buscarID}).json()
		print(iddado['Genre'],iddado['Title'])

#Para hacer un request sin tipo, ya que hay más generos a parte de las opciones dadas.
elif eleccion == 3:
	general=requests.get(raiz,	
								params={'s':buscar}).json()
	buscar=input("Dime un juego o episodio: ")
	for x in range (10):
		print(general['Search'][x]['Title'],general['Search'][x]['imdbID'])

		buscarID= input("Dime un id anteriormente dados: ")
		iddado=requests.get(raiz,
									params={'i':buscarID}).json()
		print(iddado['Genre'],iddado['Title'])

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

