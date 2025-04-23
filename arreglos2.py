playlistc=[
    "Beat.it",
    "Loba",
    "15B",
    "Diva virtual",
    "Pokemon Johtho",
    "Despacito"
]

####Toda la lista
print(playlistc)

####Elemento especifico
print(playlistc[3])

####Tamaño
print("El tamaño es: ")
size= len(playlistc)
print(size)
####print(len(playlistc))

print("El ultimo elemento es: ")
print(playlistc[size - 1])

####
print("imprimir todas las letras de una palabra")
nuevaPalabra = "GIRAFARIG"

for i in range(len(nuevaPalabra)):
    print(nuevaPalabra[i])

#########Palindromos act

print("Palindromo")
palabra=input("ingrese la palabra : ")
palabra=palabra.lower()
palabrai=palabra[::-1]

if palabra==palabrai:
    print("Tu palabra es un palindromo")
else:
    print("tu palabra no es un palindromo")

############





