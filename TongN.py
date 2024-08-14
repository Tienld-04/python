n = int(input())
sum = 0
arr = []

for i in range(1,n+1):
    # arr.append(input(f"Nhập phần tử thứ {i}: "))
    if(i%2== 0):
        print(i, end=" ")
    else:
        sum += i

# for i in range(1, n+1):
#     sum1 += int(arr[i])
print(sum)