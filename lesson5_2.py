first_number = float(input('Enter the first number: '))

action = int(input(
      '1) +\n'
      '2) -\n'
      '3) *\n'
      '4) /\n'
      'Choose an action: '))
second_number = float(input('Enter the second number: '))
match action:
    case 1:
        print('Result:', first_number+second_number)
    case 2:
        print('Result:', first_number - second_number)
    case 3:
        print('Result:', first_number * second_number)
    case 4:
        print('Result:', first_number / second_number)
    case _:
        print('Unknown operation!')

