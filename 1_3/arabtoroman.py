num = int(input())
s = ""

if (num // 1000) > 0:
    s = s + (num // 1000) * "M"
    num = num % 1000
if (num // 500) > 0:
    if (num // 100) == 9:
        s = s + "CM"
        num = num - 900
    else:
        s = s + "D"
        num = num % 500
if (num // 100) > 0:
    if (num // 100) == 4:
        s = s + "CD"
        num = num - 400
    else:
        s = s + (num // 100) * "C"
        num = num % 100
if (num // 50) > 0:
    if (num // 10) == 9:
        s = s + "XC"
        num = num - 90
    else:
        s = s + "L"
        num = num - 50
if (num // 10) > 0:
    if (num // 10) == 4:
        s = s + "XL"
        num = num - 40
    else:
        s = s + (num // 10) * "X"
        num = num % 10
if (num // 5) > 0:
    if (num % 5) == 4:
        s = s + "IX"
        num = num - 9
    else:
        s = s + "V"
        num = num - 5
if num == 4:
    s = s + "IV"
else:
    s = s + num * "I"

print(s)