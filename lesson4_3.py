# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
N = int(input("Enter the N: "))
res_dict = {i:{'name':str(input('Name: ')),'mail': str(input('Mail: '))}  for i in range(1, N+1)}
print(res_dict)