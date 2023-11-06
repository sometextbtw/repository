# Пользователь вводит Имя, Возраст и Город, сформировать
# приветственное сообщение путем форматирования 3-мя способами
name = input("Enter the name: ")
age = input("Enter the age: ")
city = input("Enter the city: ")

print("My name is %s, i am %s years old, i am from %s" % (name, age, city))
print(f"My name is {name}, i am {age} years old, i am from {city}")
print("My name is " + name + " ,i am " + age + " years old, i am from " + city)
