file = open("newfile.txt", "a")
file.write("This has been written to a file")
file.write("\n Hello")
file.write("\n Hello")
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()

file = open("books.txt", "a")

file.write("\nThe Da Vinci Code")
file.close()

file = open("books.txt", "r")
print(file.read())
file.close()

msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()

file = open("newfile.txt", "r")
print(file.read())
file.close()