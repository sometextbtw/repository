with open('table.csv', 'r') as file:
    lines = file.readlines()

titles = lines[0].split(',')
new_dict = []

for line in lines[1:]:
    values = line.split(',')
    new_dict.append(dict(zip(titles, values)))

print(new_dict)
