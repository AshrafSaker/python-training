try:
  variable = 10
  print (10 / 2)
except ZeroDivisionError:
  print("Error")
print("Finished")

try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
    
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")


try:
  meaning = 42
  print(meaning / 0)
  print("the meaning of life")
except (ValueError, TypeError):
  print("ValueError or TypeError occurred")
except ZeroDivisionError:
  print("Divided by zero")
  
def withdraw(amount):
   print(str(amount) + " withdrawn!")

#your code goes here

try:
    a = int(input())
    withdraw(a)
except ValueError:
    print("Please enter a number")