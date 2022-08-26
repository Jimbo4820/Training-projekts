def bmi():

    bmi = masa_w_kg/wzrost_w_m
    if bmi >= 25:
        print("nadwaga")
    elif bmi < 18.5:
        print("niedowaga")
    else:
        print("pożądana masa ciała")

while True:
    masa_w_kg = int(input("masa twojego ciała w kg: "))#>20 kg <200
    wzrost_w_m = int(input("wzrost twojego ciała w metrach: "))#>1metr <2.5
    if masa_w_kg < 20 or masa_w_kg > 200 or wzrost_w_m < 1 or wzrost_w_m > 2.5:
        print("sprawdż swoje dane")
    else:
        bmi()
        break

a = []
for i in range(3):
    kąt = int(input("podaj kąt każdego z boków:"))
    a.append(kąt)

def czyToTrójkąt():
    b = (a[0] + a[1]) > a[2]
    c = (a[2] + a[1]) > a[0]
    d = (a[2] + a[0]) > a[1]
    if b and c and d:
        print("To jest trójkąt)")

def czy_to_trojkat_prostokatny(a):
    if a[2]**2 == a[1]**2 + a[0]**2:
        print("Tak")
    else:
        print("Nie")

def pole_trojkata(a):
    p = (a[0]+a[1]+a[2])/2
    pole = (p*(p - a[0])*(p - a[1])*(p - a[2]))**0.5
    print("Pole =", pole)

czyToTrójkąt() 
czy_to_trojkat_prostokatny(a)
pole_trojkata(a)




