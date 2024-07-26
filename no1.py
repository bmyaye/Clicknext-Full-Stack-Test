# no.1 sum array

a = input("Enter the array: ").split()
a = [int(i) for i in a]

s = int(input("Enter the sum: "))

result = []

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == s:
            result.append([a[i], a[j]])

for i in result:
    print(i)
