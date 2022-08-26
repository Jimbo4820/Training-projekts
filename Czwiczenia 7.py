#def czy_przestepny(rok):
#    if rok % 4 == 0 and rok % 100 == 0 and rok > 1582:
#        return True
#    else:
#        return False
#
#dane_testowe = [1900, 2000, 2016, 1987]
#wyniki_testow = [False, True, True, False]
#for i in range(len(dane_testowe)):
#    r = dane_testowe[i]
#    print(r,"->",end="")
#    wynik = czy_przestepny(r)
#    if wynik == wyniki_testow[i]:
#        print("OK")
#    else:
#        print("Nie powiodło się")

# 2 3 5 7 11 13 17 19


def czy_pierwsza(liczba):
    for i in range(0,i):
        i = i % range(0,i)
        if i == 0:
            print("nie")
        else:
            print(i)
#

for i in range(1, 20):
	if czy_pierwsza(i + 1):
			print(i + 1, end=" ")
print()