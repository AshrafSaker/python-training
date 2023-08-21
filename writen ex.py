n = int(input("n: "))

file = open("numbers.txt", "w+")
for i in range(n):
    i += 1
    print(i)
#your code goes here
file.write(i)
file.close()

f = open("numbers.txt", "r")
print(f.read())
f.close()