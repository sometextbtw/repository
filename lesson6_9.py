# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)


def checkout(dict):
    pure_emails = []
    for user_id, user_data in users_dict.items():
        email_value = user_data.get("email", "")
        if email_value == " " or not email_value:
            pure_emails.append(user_data["name"])
    return pure_emails


users_dict = {
    1: {
        "name": "ivan",
        "surname": "ivanov",
        "numbers:": "1234567",
        "email": "ivan@gmail.com",
    },
    2: {"name": "petr", "surname": "petrov", "numbers:": "7654321", "email": " "},
}


print(checkout(users_dict))
