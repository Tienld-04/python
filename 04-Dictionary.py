dictCar = {
    "brand": "Honda",
    "model": "Honda Civic",
    "year": 1972
}
dictCar["year"] = 2020
dictCar["color"] = "yellow"
print(dictCar)

for x in dictCar:
    print(x, ": ", dictCar.get(x))

for x in dictCar.values():
    print(x)

print(len(dictCar))
if "model" in dictCar:
    print("Khoa \"model\" co ton tai.")
else:
    print("Khoa \"model\" khong ton tai.")

dictCar.pop("model")
print(dictCar)
dictCar.popitem()

print(dictCar)
dict1 = dictCar # su dung toan tu =
dict2 = dictCar.copy() # su dung ham copy()
dictCar["color"] = "yellow" # thay doi dictCar
print("dict1: ", dict1)
print("dict2: ", dict2)



