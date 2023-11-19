# Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
# четные, потом нечётныe
def numb_sort(numbers):
    return numbers % 2, numbers


numb_list = [1, 23, 44, 41, 25, 15, 1, 26, 3, 115, 21, 52]
print(sorted(numb_list, key=numb_sort))
