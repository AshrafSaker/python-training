text = input("text: ")
word = input("word: ")
def search(text, word):
    if word in text:
        print("Word found")
    else:
        print("Word not found")
    return
print(search(text, word))