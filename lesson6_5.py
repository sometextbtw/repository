# Дан список чисел, необходимо его развернуть без использования метода revese и
# функции reversed, а так же дополнительного списка и среза
def reverse_list(numb):
    i = 0
    lenght = len(numb)
    while i < lenght:
        numb.insert(i, numb.pop())
        i += 1
    return numb


numb_list = [1, 215, 55, 41, 25, 151, 61]
print(reverse_list(numb_list))
