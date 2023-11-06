# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
message = input("Enter the message: ").strip()
print(message.replace(" ", "-"))
print("-".join(message.split()))
