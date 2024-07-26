# no.3 range of number

a = input("Enter the array: ").split()
a = [int(i) for i in a]

result = []
i = 0

while i < len(a):
    start = a[i]
    while ( i < (len(a)-1) ) and ( (a[i]+1) == a[i+1] ):
        i += 1
    end = a[i]
    if start == end:
        result.append(f'{start}')
    else:
        result.append(f'{start}-{end}')
    i += 1

print(', '.join(result))
