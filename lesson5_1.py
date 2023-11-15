N = int(input("Enter the N: "))
M = int(input("Enter the M: "))
K = int(input("Enter the K: "))
i = K + 1
counter = 0

while counter < N:
    if i % M == 0:
        print(i)
        counter += 1
    i = i + 1
