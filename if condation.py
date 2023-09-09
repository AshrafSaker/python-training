print("hello py")
name = input("what's your name: ")
name= name.title()

age = int(input("what's your age: "))

if age < 6:
    print("you are So cute 😍")
elif 6 < age < 18:
    school = input("what's you school 🏫 name: ")
else:
    job = input("Where do you work💪: ")  
print("-"*30)
print("ID")
print("Name: ",name)
print("Age: ", age)
if age < 6:
    print("Baby")
elif 6 < age < 18:
    print("School: ",school)
else:
    print("Work: ",job) 
print("-"*30)