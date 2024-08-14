import math
x = float(input("Nhap vao x = "))

print("|x| = ", math.fabs(x))
print("ceil x = ", math.ceil(x))
print("floor x = ", math.floor(x))
print("pi = ", math.pi)
print("e = ", math.e)
print("exp 3 = ", math.exp(3))
print("log 3 = ", math.log(3))
print("pow(3,3) = ", math.pow(3, 3))

# round: lấy các số sau dấu phẩy
print("sqrt 3 = ", round(math.sqrt(3), 3))
y = round(x, 2); # lấy sau dấu phẩy 2 chữ số
print(y)