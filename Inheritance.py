class Animal: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")
        
        
class Dog(Animal):
    def bark(self):
        print("Woof!")
        print("the sound Dog!!!")
        print("*"*20)

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
print(fido.name)
fido.bark()
print("-"*30)
class Wolf: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof")

husky = Dog("Max", "grey")
husky.bark()

print("-"*30)
class A:
  def method(self):
    print(1)

class B(A):
  def method(self):
    print(2)

B().method()

print("-"*30)

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()
print("-"*30)

class Shape: 
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width*self.height)

class Rectangle(Shape):
    def perimeter(self):
      print((self.width + self.height) *2)  
    #your code goes here
    

w = int(input())
h = int(input())

r = Rectangle(w, h)
r.area()
r.perimeter()