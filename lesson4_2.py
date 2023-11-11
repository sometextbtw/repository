# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры
text = str(input('Enter the text: '))
res_dict = {i:text.count(i) for i in text}
print(res_dict)