contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]
x = input("name: ")
for i in contacts:
    if x in i:
        print(i[1])
        break
else:
    print("not")

