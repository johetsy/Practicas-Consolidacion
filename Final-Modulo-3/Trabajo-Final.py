# Dada la siguiente lista de nombres:
# Harry Houdini, Newton, David Blaine, Hawking,  Messi,  Teller, Einstein, Pele, Juanes
# Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton,
# Hawking y Einstein son científicos. Debemos separar los nombres en tres grupos: magos,
# científicos y otros; y escribir una función llamada hacer_grandioso(), que modifique la
# lista de magos añadiendo la frase ‘El gran‘ antes del nombre de cada mago. Crear una función
# llamada imprimir_nombres(), que imprime el nombre de cada persona de la lista.
# Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados
# luego imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes.

lista_nombres = ['Harry Houdini', 'Newton', 'David Blaine',
                 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']
lista_magos = []
lista_cientificos = []
lista_otros = []
lista_magos2 = []

for nombre in lista_nombres:
    if (nombre == 'Newton' or nombre == 'Hawking' or nombre == 'Einstein'):
        lista_cientificos.append(nombre)
    elif (nombre == 'Harry Houdini' or nombre == 'David Blaine' or nombre == 'Teller'):
        lista_magos.append(nombre)
    else:
        lista_otros.append(nombre)


def hacer_grandioso():
    for nombre in lista_magos:
        lista_magos2.append('El Gran' + ' ' + nombre)
    print(lista_magos2)


def imprimir_nombres():
    for nombre1 in lista_nombres:
        print(nombre1)


print('\n ***Lista Completa de Nombres***')
imprimir_nombres()
print('\n ***Magos Grandiosos***')
hacer_grandioso()
print('\n ***Cientificos***')
print(lista_cientificos)
print('\n***Otros***')
print(lista_otros, '\n')
