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
print(spisok2)
#Проверка
#Изменение для коммита