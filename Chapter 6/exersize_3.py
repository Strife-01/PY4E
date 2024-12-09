def count(string, character):
    count = 0
    for char in string:
#        if char == character:
#        if char in character:
        if char is character:
            count += 1
    return count

text = input("enter text: ")
char = input("what character to count: ")

print(count(text, char))
