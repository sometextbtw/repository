# Заполнить список степенями числа 2 (от 2^1 до 2^n)
N = int(input("Enter the N: "))
res_dict = [2**i for i in range(1, N + 1)]
print(res_dict)
