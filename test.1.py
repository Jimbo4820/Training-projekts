from colorama import init
from colorama import Fore, Back, Style

init()

print( Back.GREEN )
print ( Fore.WHITE )

num_1 = int(input('Number 1 : '))

print( Back.CYAN )
print ( Fore.WHITE )
num_2 = int(input('Number 2 : '))
while True:
    act = input('''wybierz akcję z liczbami
    (+,-,*,/,n^n): ''')


    print( Back.YELLOW )
    print ( Fore.BLACK )
    if act == '+':
        res = num_1 + num_2
        print('Wynik : ', num_1 , '+' , num_2 , '=' , res)
        break

    elif act == '-':
        res = num_1 - num_2
        print('Wynik : ' , num_1 , '-' , num_2 , '=' , res)
        break

    elif act == '*':
        res = num_1 * num_2
        print('Wynik : ' , num_1 , '*' , num_2 , '=' , res)
        break

    elif act == '/':
        res = num_1 / num_2
        print('Wynik : ' , num_1 , '/' , num_2 , '=' , res)
        break

    elif act == 'n^n':
        res = num_1 ** num_2
        print('Wynik : ' , num_1 , '**' , num_2 , '=' , res)
        break    

    else:
        print('Blęd, niema takiego znaku')
print('Operacja wykonana)')
k = input("kliknij ENTER aby kontynuować ")
input(k)
