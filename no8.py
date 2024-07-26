# no.8 total_amount

total_amount = int(input("Enter the amount to be paid: "))

remain_amount = 1000 - total_amount
total_amount = remain_amount

five_hundred = total_amount // 500
total_amount %= 500
one_hundred = total_amount // 100
total_amount %= 100
fifty = total_amount // 50
total_amount %= 50
twenty = total_amount // 20
total_amount %= 20
ten = total_amount // 10
total_amount %= 10
five = total_amount // 5
total_amount %= 5
one = total_amount

print(f"จำนวนเงินทอน {remain_amount} บาท")
if five_hundred > 0:
    print(f"500 {five_hundred} ใบ")
if one_hundred > 0:
    print(f"100 {one_hundred} ใบ")
if fifty > 0:
    print(f"50 {fifty} ใบ")
if twenty > 0:
    print(f"20 {twenty} ใบ")
if ten > 0:
    print(f"10 {ten} เหรียญ")
if five > 0:
    print(f"5 {five} เหรียญ")
if one > 0:
    print(f"1 {one} เหรียญ")
