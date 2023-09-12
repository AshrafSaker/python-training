def pri(name):
    print('='*5 + '='*len(name)+'='*5)
    print('='*5 + name +'='*5)
    print('='*5 + '='*len(name)+'='*5)
#Lambdas
pri('Lambdas')

def my_func(f, arg):
  return f(arg)

print(my_func(lambda x: 2*x*x, 5))

#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

#practice 
pri('practice Lambdas')

price = int(input("Write The price! :"))
perc = int(input("Write Percent% :"))

res = (lambda x,y:x*(y/100))(price, perc)

print(res)



