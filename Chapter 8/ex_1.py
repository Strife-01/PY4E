def chop(array):
    del array[0]
    del array[len(array) - 1]
    return None

def middle(array):
    return array[1 : len(array) - 1]


a = [1, 2, 3, 4, 5, 6]
chop(a)
print(a)

b = [10, 11, 12, 13, 14]
print(middle(b))
print(b)
