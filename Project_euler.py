print('''\tProject number 1
        Сумма чисел кратные 3 и 5 от 1 до 1000 ''')
sum = 0 
for i in range(1,1000):
    i % 3
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i
print("\tсумма =", sum)
    