fichero = open('pokemon.txt', 'r') 
ListaPokemon = fichero.read().split() # Convertimos lo que tenemos en fichero a lista y lo introducimos en ListaPokemon

ListaAuxiliar = [] #Lista en la cual almacenamos momentaneamente las cadenas que vamos formando
Lista = [] #Lista mas larga que encontramos hasta el momento

for elemento in ListaPokemon: #Recorremos ListaPokemon de uno en uno
	ListaAuxiliar.append(elemento) #Aniadimos a nuestra ListaAuxiliar el elemento
	i = 0
	while i < len(ListaPokemon): #Recorremos ListaPokemon de uno en uno
		if (ListaPokemon[i] not in ListaAuxiliar and ListaAuxiliar[-1][-1] == ListaPokemon[i][0]): 
		# Comprobamos que el elemento no haya sido aniadido previamente y que cumple nuestra condicion
		# de que empiece por la misma letra que acabo el anterior pokemon de la lista
			ListaAuxiliar.append(ListaPokemon[i]) #Aniadimos elementoAux a ListaAuxiliar
			i = 0; #i sera el indice primer pokemon de ListaPokemon, ya que tenemos que empezar desde el 
			# el principio buscando un pokemon que cumpla nuestra conidicion
		else: 
			i = i + 1 #incrementamos i en 1
	if (len(ListaAuxiliar)>len(Lista)): # Comprobamos si la ListaAuxiliar es mas larga que Lista
		del Lista[:] # Borramos Lista
		Lista.extend(ListaAuxiliar) # Amplimos Lista con ListaAuxiliar
	del ListaAuxiliar[:] # Borramos ListaAuxliar
print Lista # Pintamos el contenido de Lista
