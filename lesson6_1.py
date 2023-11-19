# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int
def numb_trans(n):
    binary_numb = bin(n)[2:]
    decimal_numb = 0
    power = 0

    for i in reversed(binary_numb):
        if i == "1":
            decimal_numb += 2**power
        power += 1

    return "0b" + binary_numb, decimal_numb


print(numb_trans(13))
