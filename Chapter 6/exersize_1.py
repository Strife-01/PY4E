text = input("enter your text: ")

lenght = len(text)

#for character in reversed(text):
#    print(character)

character = lenght - 1
while character > -1:
    print(text[character])
    character -= 1
