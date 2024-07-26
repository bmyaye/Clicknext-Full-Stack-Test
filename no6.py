# no.6 reverse int

# a = input("Enter the number: ").split()
a = input("Enter the number: ").split(", ")
a = [int(i) for i in a]

for i in range(len(a)):
    for j in range(0, len(a)-i-1):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

result = [str(i) for i in a]
print(', '.join(result))

# print(a)