# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))
print("Positive: ", ((first_number < 0) + (second_number < 0) + (third_number < 0)))
print("Negative: ", ((first_number > 0) + (second_number > 0) + (third_number > 0)))
