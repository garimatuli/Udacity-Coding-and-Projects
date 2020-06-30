def count_character(string, target):
    count = 0
    for ch in string:
        if ch == target:
            count = count + 1
    return count


def count_char(string, target):
    i = 0
    count = 0
    while i < len(string):
        if target == string[i]:
            count += 1
        i += 1
    return count


def count_words(str):
    count = 0
    i = 0
    j = 0
    while i < len(str):
        if str[i] == " ":
            print(str[j:i])
            count += 1
            j = i + 1
        i = i + 1
    print(str[j:i])
    return count+1


# Should print a count of 3
print(count_character("oxen and foxen all live in boxen", "x"))
print(count_char("oxen and foxen all live in boxen", "x"))

# This should return 3, since there are three "o"s:
print(count_character("bonobo", "o"))
print(count_char("bonobo", "o"))

# word count in strings
print("\n")
print(count_words("oxen and foxen all live in boxen"))
print("\n")
print(count_words("Mind the gap!"))
