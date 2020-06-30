# print word triangle
word = "definitely"
length = len(word)
for n in range(length):
    print(word[:n+1])


# print * triangle pattern
for n in range(length):
    print("*" * n)


for n in range(length):
    print((" " * (length-n)) + ("*" * n))


for n in range(length):
    print((" " * (length-n)) + ("*" * n) + ("*" * (n-1)))
    

