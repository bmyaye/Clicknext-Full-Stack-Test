# no.5 triangle int

n = int(input("Enter the number of rows: "))

if n >= 1 and n <= 4:
    current_num = 1
    for i in range(1, n+1):
        result = ''.join(str((current_num + j) % 10) for j in range(i))
        print(result)
        current_num = (current_num + i) % 10
else:
    print("Please enter number between 1 and 4")