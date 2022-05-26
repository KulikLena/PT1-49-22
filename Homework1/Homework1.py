string= "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"

#1.Посчитать количество символов
n=len(string)
print("Шаг1: Количество символов в строке составляет: "+str(n))

#2.Развернуть строку
reverse_str =  string[::-1]
#мой редактор такой формат подчеркивает, почему-то, но работает 
print(f'{"Шаг2:Развернутая строка выглядит следующим образом: "}{reverse_str}')

#3.Сделать каждое слово с большой буквы
title_str=string.title()
print(f'{"Шаг3: Слова с большой буквы выглядят так: "}{title_str}')

#4.Сделать весь текст прописными буквами
caps_lock=string.upper()
print(f'{"Шаг4: Весь текст прописными буквами: "}{caps_lock}')

#5.Найти число вхождений "нд", "ам", "о" в строку
count_1=string.count("нд")
count_2=string.count("ам")
count_3= string.count("o")
print("Шаг5: НД встерачается {} раз, AM встречается {} раз, О встречается {} раз".format(count_1, count_2, count_3))

#6. Собственные упражнения

#подстановка значение format()
localized_str="Не знаю, как там в {}{}, я не была. Может, там {} — друг человека. А у нас управдом — друг человека!"
city="Париж"
postfix="е"
animal="лось"
print("В других городах говорят по-другому: "+localized_str.format(city,postfix,animal))

# замена символов
trans_table = string.maketrans({'о': 'и', 'л': 'к', '—': ':'})
translated_str=string.translate(trans_table)
print("Замена символов: "+translated_str)

# разбивка на слова и знаки препинания
splited_list=string.split()
print(f'{"Из длинной строки можно сделать список из отделльных слов: "}{splited_list}')

#Вывести в консоль исходную строку
print("Шаг7: Исходня строка хранилась в переменной string и не изменялась: "+string)