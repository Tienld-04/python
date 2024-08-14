
n = int(input())
arr = [9,8,7,1,2,3,4,5]
# arr.append(6) // thêm ptu
# arr.remove(3) // xóa ptu 
# arr.sort()  //sắp xếp tăng dần
# arr.reverse() //đảo ngược mảng
# for i in arr:
    # print(i)

arr2 = list()
for i in range(n):
    b = int(input())
    arr2.append(b)

arr2.insert(0, 12)
arr2.pop()
print("count: ", arr2.count(2))
arr2.extend(arr)
for j in arr2:
    print(j)



