# no.7 time

time = int(input("Enter the time in seconds: "))
hour = time // 60 // 60
min = time // 60 % 60
sec = time % 60 % 60
print(f"{hour:02d}:{min:02d}:{sec:02d}")