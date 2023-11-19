# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4
def list_shift(numb, n):
    for i in range(n):
        temporary_numb = numb.pop(0)
        numb.append(temporary_numb)
    return numb


numb_list = [1, 2, 3, 4, 5, 6, 7]
N = 3

print(list_shift(numb_list, N))
