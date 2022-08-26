print("\t Добро пожаловать в калькулятор")

num_1 = int(input("number_1 :"))
num_2 = int(input("number_2 :"))

def search_symbole(symbol):
    a = 1
    while a == 1:
        global i
        all_symbole = ['+','-','/','*']
        for i in all_symbole:
            if symbol == i:
                a = 2
                return i
            else:
                print('В этом калькуляторе еще нет такого знака')
                        
def example():
    if i == '+':
        print(num_1 + num_2)
    elif i == '-':
        print(num_1 - num_2)
    elif i == '/':
        print(num_1 / num_2)
    elif i == '*':
        print(num_1 * num_2)

search_symbole(input("Введите знак: "))
example()