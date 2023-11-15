N = int(input("Enter the N: "))
counter = 0
for i in range(2, N + 1, 2):
    print(i, end=" ")
    counter += 1
    if counter >= 5:
        print("")
        counter = 0
