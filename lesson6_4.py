# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно
def list_sort(list):
    index = 0
    while index < len(list):
        if not isinstance(list[index], str):
            list.pop(index)
        else:
            index += 1
    return list


data_list = [1, 23, "hello", True, "World"]
print(list_sort(data_list))
