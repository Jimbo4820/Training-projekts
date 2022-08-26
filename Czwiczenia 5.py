#beatles = []
#print("Krok 1:", beatles)
#beatles.append("John Lennon")
#beatles.append("Paul McCartney")
#beatles.append("George Harrison")
#print("Krok 2:", beatles)
#new_beatles = ["Stu Sutcliffe", "Pete Best"]
#for i in new_beatles:
#    beatles.append(i)
#print("Krok 3:", beatles)
#del beatles[-1]
#del beatles[-1]
#print("Krok 4:", beatles)
#beatles.insert(0,"Ringo Starr")
#print("Krok 5:", beatles)
## Sprawdzanie długości listy.
#print("The Fab", len(beatles))

lista = [17, 3, 11, 5, 1, 9, 7, 15, 13]

index = 0

lista.sort()
print(lista)
najwieksza = lista[-1]
index = lista.index(najwieksza)

print("Największa liczba na liście to:", najwieksza, "Liczba ma index:", index)


lista = []
swapped = True
zapyt = int(input("Ile elementów posortować:"))

for i in range(zapyt):
    nowa_liczba = int(input("nowa liczba: "))
    lista.append(nowa_liczba)

# Elementy zostaną posortowane
while swapped:
    swapped = False
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            swapped = True
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print("\nPosortowane:")
print(lista)