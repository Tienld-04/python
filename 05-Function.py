def hello():
    print("helle")
def sum(a, b):
    print(a+b)
    return a+b
def array(*k):
    print(k[0], k[1])
def sum1(*arr):
    s = 0
    for i in arr:
        s+=i
    print(s)
def gcd(a, b):
    while(a!=b):
        if(a>b):
            a = a-b
        else:
            b = b-a
    return a

hello()
print(sum(2,3))
print(1,2,"kk")
sum1(1,2,3,3,4,4)
print(gcd(11,121))

