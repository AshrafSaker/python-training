def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

print('='*15)

def test(func, arg):
    return func(func(arg))

def mult(x):
    return x * x

print(test(mult, 2))

def pri(name):
    print('='*5 + '='*len(name)+'='*5)
    print('='*5 + name +'='*5)
    print('='*5 + '='*len(name)+'='*5)
#Pure Function
pri('Pure Function')
def pure_function(x, y):
  temp = x + 2*y
  
  return temp / (2*x + y)
print(pure_function(3,5))

#Impure function
pri('Impure function')

some_list = []

def impure(arg):
  some_list.append(arg)
  print(some_list)
impure(3)
impure(5)
impure(6)
print(impure(1))