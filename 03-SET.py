num = {1,2,9,3,4,5,6,7,7,7}
arr = {23,44,55}
for i in num:
    print(i, end= " ")
num.add(8)
num.remove(7)
num.update(arr)
del arr
num.pop()
num.discard(100) 
print(num)