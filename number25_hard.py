import re

rightBorder = int("gggggg", 17)     # для обозначения правой границы в 10 системе счисления

def to17ss(a):
    numbersIn17 = "0123456789abcdefg"
    result = ""
    while a:
        result += numbersIn17[a % 17]
        a //= 17
    return result[::-1]

def toFactss(a):
    divideBy = 2
    result = ""
    while a:
        result += str(a % divideBy)
        a //= divideBy
        divideBy += 1
    return result[::-1]

for i in range(235, rightBorder + 1, 235):
    if (re.fullmatch(r"1[a-g]\d\d{,2}[a-g]", to17ss(i))) and (i % 71 == 0):
        print(i // 235, toFactss(i))
