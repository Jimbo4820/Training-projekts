#ГЛАВА 4 Сортировка
# Задание 1
#Пользователь вводит массив чисел

#Метод рекурсии
def sum(numbers):
    if not numbers:
        return 0
    else:
        return numbers.pop() + sum(numbers[0:-1])
print(sum([1,2,3]))
#
#Факториал с помощью метода рекурсии
def fact(x):
    if x == 1:
        return 1 
    else:
        return x * fact(x-1)
print(fact(3))

#Быстрая сортировка на основе рекурсии
def quicksort(array):
    if len(array)<2:
        return array
    else:
        pivot = array[0]

        less = [i for i in array[1:] if i <= pivot]

        greater = [ i for i  in  array[1:] if  i > pivot]

        return quicksort(less) + [pivot] + quicksort (greater)
print(quicksort([10, 5,  2, 3])) 
