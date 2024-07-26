# no.10 triangle star up

n = int(input("Enter the number of rows: "))

for i in range(n):
    print(" " * (n-i-1) + "*" * (2*i+1))