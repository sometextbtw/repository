# Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры
res_dict = {}
N = int(input("Enter the N: "))
for i in range(1, N + 1):
    nestery_dict = {
        "name": str(input(f"Name of the {i} person: ")),
        "email": str(input(f"Mail of the {i} person: ")),
    }
    res_dict[i] = nestery_dict

print(res_dict)
