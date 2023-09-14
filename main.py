#Ruslan = input('Введите камень, ножницы или бумага: ').lower()
#Timur = input('Введите камень, ножницы или бумага: ').lower()
#komment
stroka = list(input('Напишите строкой количество разыгранных орлов и решек(ОРОРРОРРРРОРРРР):'))
print(stroka)

counterer = 0
spisok = []

for i in range(len(stroka)):
    if stroka[i] == 'Р':
        counterer += 1

    if stroka[i] != len(stroka):
        if stroka[i] == 'О':
            spisok.append(counterer)
            counterer = 0
print(spisok)