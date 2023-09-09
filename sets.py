letters = {"a", "b", "c", "d"}
if "e" not in letters:
    print(1)
else:
    print(2)

print("="*6,'mathmatical','='*6)
#-------------Mathematical---------------
first = {1,2,3,4,5,6}
second = {4,5,6,7,8,9}
print(first | second) # Merg or combnes with to sets
print(first & second) # inner - get only tems in both
print(first ^ second) # outter - get all item not in to gether
print(first - second) # get items only in first not in second
print(second - first) # get item only in second not in first

#----------------------------
print("="*18)
print("="*6,"****","="*6)
print("="*6,"Test","="*6)
print("="*6,"****","="*6)
print("="*18)
#----------------------------
skils = {'Python','HTML','SQL','C++','Java','Scala'}
job_skils = {'HTML','CSS','JS','C#','NodeJS'}
print(skils & job_skils)
print(list(skils & job_skils))
print(list(skils & job_skils)[0])
#----------------------------
print("="*18)
print("="*6,"****","="*6)
print("="*6,"End","="*6)
print("="*6,"****","="*6)
print("="*18)
#----------------------------
def eq(name=''):
    print('='*6+'='*len(name)+'='*6)
    print('='*6+'*'*len(name)+'='*6)
    print('='*6+name+'='*6)
    print('='*6+'*'*len(name)+'='*6)
    print('='*6+'='*len(name)+'='*6)
eq('math')
eq()
eq('end')