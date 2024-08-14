check = lambda a: (a%2==0)

print(check(5))
print(check(2))

sum = lambda a,b: (a+b)
print(sum(1,2))

def x(n):
    return lambda a : a**n

x2  = lambda a : a**2
print(x2(2))

x3 = x(3)
print(x3(2)) # 2^3
