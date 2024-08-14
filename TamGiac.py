import math
a, b, c = map(float, input().split())
if a + b > c and a + c > b and b + c > a:
    cv = a + b + c
    print("{:.2f}".format(cv))
    p = cv / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("{:.2f}".format(s))
else:
    print("khong la tam giac")
    