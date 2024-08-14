n = int(input())
arr = []
sum1 = 0
sum2 = 0
i1 = 0
i2 = 0
for i in range(n):
    a = int(input())
    arr.append(a)
if n == 0:
    print(0)
    print(0)
elif n == 1:
    if(arr[0]%2!=0):
        print(int(arr[0]))
        print(0)

    else:
        print(0)
        print(int(arr[0]))
else:
    for i in arr:
        if i%2 != 0:
            sum1 += i
            i1 += 1
        else:
            sum2 += i
            i2 += 1
    if i1 == 0:
        print(0)
    else:
        print(sum1//i1)
    if i2 == 0:
        print(0)
    else:
        print(sum2//i2)