#1.	Используя стандартные арифметические операции представьте
# самое большое целое число из цифр 4, 4, 4 и приведите его значение.

print(4 ** 4 ** 4)

#2.	Написать программу для вычисления значения выражений.
# Проверить правильность выполнения задания с помощью тестовых значений.
#A
a = int(input("Введите значение"))
y = ((1+a+a**2)/(2*a+a**2))+2-((1-a+a**2)/(2*a-a**2))**-1*(5-2*a**2)
print(y)

#B
import math
a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
y = int(input("Введите значение y: "))
c = 0.25*(math.sin(a+b-y)+math.sin(b+y-a)+math.sin(y+a-b)+math.sin(a+b+y))
print(c)
#3.	Создать пустую переменную. Проверить ее на истинность и ложность.
# Объясните полученный результат.
a = ""
print(bool(a))

#4.	Даны два целых числа m и n (m≤n). Н
# апишите программу, которая выводит все числа от m до n включительно.

m = 2
n = 8
for i in range(2, 9):
    print(i)

#5  Даны два целых числа m и n. Напишите программу,
# которая выводит все числа от m до n включительно в порядке возрастания,
# если m<n, или в порядке убывания в противном случае.

m = 5
n = 10
if m < n:
    for i in range(m, n + 1):
        print(i)
elif m > n:
    for i in reversed(range(n, m + 1)):
        print(i)

#6.	В строке “Иван Иванов” поменяйте местами слова.
# Может быть предоставлена любая строка с именем и фамилией.
#например
#“Петр Иванов” => “Иванов Петр”

a = "Джесика Шпак"
a = a.split(' ')
print(a)
a.reverse()
print(a)

#7.	Создать список с числами от 1 до 50 используя генератор списков.
v = []
for i in range(1, 51):
    v.append(i)
print(v)

#8.	Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5

a = [1, 5, 2, 9, 2, 9, 1]
f = a.count(5)
print(f)

#9.	Дан список [student1, student2, student3] с помощью цикла for добавить к каждому
# элементу списка слово “_good”. Вывести на экран.

s = ['student1', 'student2', 'student3']
d = []
for i in s:
    d.append(i + '_good')
s = d
print(d)

#10.	Вывести на экран числа от 0 до 50, кроме 35

for i in range(0, 51):
    if i == 35:
        continue
    print(i)

#11.	Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”].
# В новый список добавить элементы, которые содержат пробел.

a = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
b = [a[0], a[1]]
print(b)
