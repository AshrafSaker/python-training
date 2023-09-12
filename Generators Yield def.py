def pri(name):
    print('='*5 + '='*len(name)+'='*5)
    print('='*5 + name +'='*5)
    print('='*5 + '='*len(name)+'='*5)
#1st example
pri("1st Example") 
def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)
#infinti yield
#def infinite_sevens():
#  while True:
#    yield 7
        
#for i in infinite_sevens():
  #print(i)  
#exe2


#def get_primes():
#    num = 2
#    while True:
#        if is_prime(num):  #is_prime() is not defintion
#            yield num
#        num += 1

pri("exe")
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))

pri("Quiz")
def make_word():
    word = ""
    for ch in "spam":
        word +=ch
        yield word

print(list(make_word()))