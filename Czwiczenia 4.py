liczby_z_kapelusza = [1, 2, 3, 4, 5]
liczba_uzytkownika = int(input("Podaj liczbę:"))
srodek_listy = len(liczby_z_kapelusza)%2
liczby_z_kapelusza[srodek_listy] = liczba_uzytkownika
del liczby_z_kapelusza[-1]
print(len(liczby_z_kapelusza))
print(liczby_z_kapelusza)