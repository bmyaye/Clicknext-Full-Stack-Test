# no.9 reverse the string

a = input("Enter the string: ").split()

for i in range(len(a)):
    a[i] = a[i][::-1]

print(" ".join(a))