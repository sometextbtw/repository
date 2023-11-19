# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
def finder(city, country):
    for country_key, city_list in country.items():
        return country_key if city in city_list else "Not found"


countries_dict = {
    "Spain": ["Madrid", "Barcelona", "Valencia"],
    "France": ["Paris", "Nice", "Lion"],
}

user_city = str(input("City: "))

print(f"Ur country: {finder(user_city,countries_dict)}")
