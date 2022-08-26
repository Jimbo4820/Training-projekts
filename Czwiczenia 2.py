#CZWICZENIA 2 ZADANIE 1
#h = int(input("Czas rozpoczęcia (godziny): "))
#m = int(input("Czas rozpoczęcia (minuty): "))
#d = int(input("Czas trwania wydarzenia (minuty): "))
#m = m + d # oblicz ogólną liczbę minut
#h = h + m // 60 # znajdź liczbę godzin ukrytych w minutach i zaktualizuj godzinę
#m = m % 60 # prawidłowe minuty w zakresie (0..59)
#h = h % 24 # prawidłowe godziny w zakresie (0..23)
#print(h, ":", m, sep='')

#/////////

#print("+" + 10 * "-" + "+")
#print(("|" + " " * 10 + "|\n") * 5, end="")
#print("+" + 10 * "-" + "+")

#/////////////////
#CZWICZENIA 2 ZADANIE 2
#rok = int(input("Wprowadź rok: "))
#przez_4 = rok % 4
#przez_100 = rok % 100
#przez_400 = rok % 400
#if rok <= 1581:
#    print(rok, "Nie w kalendarzu gregoriańskim")
#elif przez_100 != 0:
#    print(rok, "jest to rok przestępny")
#elif przez_400 != 0:
#    print(rok, "jest to rok zwykły")
#elif przez_4 != 0:
#    print(rok, "jest to zwykły rok")
#else:
#    print(rok, "jest to rok przestępny")


import random
tajnyNumer = random.randrange(1, 100)       # zwraca liczbę z zakresu 1 do 100
# tajnyNumer = random.randint(1,100)        # druga wersja   
print(tajnyNumer)

print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")

while True:
    numer_użytkownika = int(input("Wprowadż swój numer:"))
    if numer_użytkownika > 100 or numer_użytkownika < 1:
        print("Nie, musisz wybrać liczbę od 1 do 100! Sprobuj ponownie")
    elif numer_użytkownika > tajnyNumer:
        print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Ona jest mniejsza. Spróbuj ponownie!")
    elif numer_użytkownika < tajnyNumer:
        print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Ona jest większa. Spróbuj ponownie!")
    else:
        print(numer_użytkownika,"\nDobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.")
        break