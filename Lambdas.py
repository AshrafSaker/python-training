print("-"*30)

#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))
print("-"*30)
price = int(input("write price: "))
perc = int(input("Enter perc%: "))

res = (lambda x,y:x-y)(price, perc)

print(res)

