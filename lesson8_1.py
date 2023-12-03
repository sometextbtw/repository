with open("text.txt", "r") as file:
    with open("newtxt.txt", "w") as new_file:
        for counter, line in enumerate(file, start=1):
            new_file.write(
                f"{counter} Строка - {sum(1 for letter in line if letter.isalpha())}\n"
            )
