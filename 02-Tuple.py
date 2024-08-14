fruits1 = ("apple", "banana", "guava", "kiwi", "cherry")
tupl2 = ("kiwi", "cherry")
fruits = fruits1+tupl2*2
print (fruits[1])
for i in fruits:
    print(i)
print(fruits.count("apple"))
print(len(fruits))

# chuyển về list
print("---------")
listfr = sorted(fruits)
print(listfr)
