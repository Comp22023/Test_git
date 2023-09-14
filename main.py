#Ruslan = input('Введите камень, ножницы или бумага: ').lower()
#Timur = input('Введите камень, ножницы или бумага: ').lower()
#komment
stroka = list(input('Напишите строкой количество разыгранных орлов и решек(ОРОРРОРРРРОРРРР):'))


counterer = 0

for i in range(len(stroka)):
    if stroka[i] == 'Р':
        counterer += 1
    elif stroka[i] == 'О':
        counterer += 0
print(counterer)