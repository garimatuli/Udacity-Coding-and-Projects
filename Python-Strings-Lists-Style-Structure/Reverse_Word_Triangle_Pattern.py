def word_triangle(word):
    length = len(word)
    for n in range(length):
        print(word[:length - n])
# The slice expression above is word[:length - n].
# Since length stays the same while n grows, this means that on each pass through the loop,
# length - n gets smaller and smaller, from length down to 1.
# And that means that on each pass, the string that gets printed will be a shorter and shorter piece of word.


def reverse_word_triangle(word):
    n = len(word)
    for i in range(n):
        print((" " * i) + (word[:n - i]))


def reverse_triangle(word):
    n = len(word)
    for i in range(n):
        print((" " * i) + (word[i:n - i]))


inputWord = "ABRACADABRA"
word_triangle(inputWord)
reverse_word_triangle(inputWord)
reverse_triangle(inputWord)
