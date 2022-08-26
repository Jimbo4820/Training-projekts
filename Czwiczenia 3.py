#import time
#
#for n in range(1,6):
#    print(n, "Mississippi")
#    time.sleep(1)
#
#print("Ready or not, here I come!")

#
#
#print("Wprowadż słowo")
#slowo_uzytkownika = input()
#slowo_uzytkownika = slowo_uzytkownika.upper()
#for litera in slowo_uzytkownika:
#    if litera == "A":
#        continue
#    elif litera == "E":
#        continue
#    elif litera == "I":
#        continue
#    elif litera == "O":
#        continue
#    elif litera == "U":
#        continue
#    else:
#        print(litera, end=" ")

#blokow = int(input("Wprowadź liczbę bloków: "))
#wysokosc = 0
#while wysokosc < blokow:
#    blokow -= wysokosc + 1
#    wysokosc += 1
#else:
#    print("nie mamy więcej elementów")
#print("Wysokość piramidy wynosi:", wysokosc)

for cyfra in "01253783402940":
    if cyfra == "0":
        cyfra = "x"
    print(cyfra, end="")

print()

liczba = int(input("Wprowadź liczbę: "))
ilosc_krokow = 0
while liczba > 1:
    if liczba % 2 == 0:
        liczba /= 2
        print(liczba)
        ilosc_krokow += 1
    else:
        liczba = 3 * liczba + 1
        print(liczba)
        ilosc_krokow += 1
print("Ilość kroków :",ilosc_krokow)