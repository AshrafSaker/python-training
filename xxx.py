txt = [
    ['a','b','c'],
    ['e','f','g'],
    ['h','i','j']
]
for row in txt:
    for ele in row:
        print(ele)
        
print(txt)
print(*txt[0],*txt[1],*txt[2])
print(*txt,sep=' ** ')

