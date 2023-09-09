print("Welcom to you in my project😊")
name = input("Please, What's your name?! ").title()
age = float(input("What's your age: "))

if 18 <= age <= 21:
    q = input("Are you still study:(Y/N) ").lower()
    if q == "y":
        school = input("What's your school name: ")
    elif q != "y":
        w = input("Are you have job? (Y/N)").lower()
        if w == "y":
            work = input("Where's your work?").title()
        else:
            print("oooh, I hope good future for you😊")
elif 5 < age < 18:
    print("That's Goood 😊 ")
    s = float(input("what your stage in school:(1:12)"))
    if 1<= s <= 6:
        p = input("Are u in primry stage:(Y/n)").lower()
        if p == "y":
            print("I hope you do well to go to perpare stage") 

            






