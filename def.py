def name(first= "",last=""):
    if first != "":
        print("Welcom",first,last,"!")
    else:
        print("First name is empty. Please enter your first name.")
        first = input("What's ur 1st name: ").title()
        name(first,1)
    
    

f = input("What's ur 1st name: ").title()
l = input("What's ur Last name: ").title()
name(f,l)