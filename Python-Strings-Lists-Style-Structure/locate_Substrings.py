# Locating 1st occurrence of a substring in a string


def locate_first_substring(substring, string):
    length = len(substring)
    i = 0
    while i < len(string):
        if string[i:i + length] == substring:
            return i
        i += 1
    return -1


print(locate_first_substring('ook', 'cookbook'))  # 1
print(locate_first_substring('code', 'codbook'))  # -1


# Locating all occurrences of a substring in a string


def locate_first_substring(substring, string):
    match = []
    length = len(substring)
    i = 0
    while i < len(string):
        if string[i:i + length] == substring:
            match.append(i)
        i += 1
    if match:
        return match
    else:
        return -1


print(locate_first_substring('ook', 'cookbook'))  # [1, 5]
print(locate_first_substring('code', 'codbook'))  # -1


# using built-in Functions

# Locating 1st occurrence of a substring in a string
print('cookbook'.find('ook'))  # 1
print('codbook'.find('code'))  # -1
