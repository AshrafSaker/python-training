def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(a, b):
    #your code goes here
  
    for i in range(a,b):
        if isPrime(i):
            yield i
    
f = int(input("1st:"))
t = int(input("2nd:"))

print(list(primeGenerator(f, t)))