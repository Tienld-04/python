class Animal:  
    def speak(self):  
        print("Animal Speaking")
 
# lớp con Dog kế thừa lớp Animal
class Dog(Animal):
    def bark(self):
        print("Gou gou!")
 
# lớp con Dogchild kế thừa lớp Dog
class DogChild(Dog):
    def eat(self):
        print("Eating milk...")
 
d = DogChild()
d.bark()
d.speak()
d.eat()
d.speak()