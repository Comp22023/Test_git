chislo = int(input('Введите натуральное число больше нуля: '))
stroka = str(input('Введите строку: '))

spisok=[]

for i in range(1,chislo + 1):
    spisok.append(i)
spisok2 = []

for g in spisok:
    if (g % 2 == 0):
        spisok2.append(stroka)
    else:
        spisok2.append(g)
print(spisok2)#Этот принт выводит результат в терминале

#Проверка
#Изменение для коммита
a = '\nВсем '
b = 'ку'
print(a + b)