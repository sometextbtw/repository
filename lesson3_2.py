# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))
print(round((first_number + second_number + third_number) / 3, 3))
