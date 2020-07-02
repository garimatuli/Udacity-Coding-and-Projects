# Finds if substring present in a string or not


def is_substring(string, substring):
    length = len(substring)

    for i in range(len(string)):
        if string[i:i + length] == substring:
            return True
    return False


print(is_substring('abracadabra', 'cad'))  # True
print(is_substring('abracadabra', 'gar'))  # False
print(is_substring('abracadabra', 'd'))  # True


# Counting occurrence of a substring in a string

def count_substrings(substring, string):
    count = 0
    length = len(substring)
    i = 0
    while i < len(string):
        if string[i:i + length] == substring:
            count += 1
        i += 1
    return count


print(count_substrings('code', 'code, code, code, all you need is code'))  # 4

print(count_substrings('AA', 'AAAA'))  # 3
# There's one sense in which the answer above is 2, and another sense in which it's 3.
# It depends on whether matches are allowed to overlap!
# With the solution above, the function counts overlapping matches—so it will count 3 instances of AA.
# If that's the behavior we want, great! But if not, below is the function to fix it in case of Overlapping Matches


# Counting occurrence of a substring in a string  (IN CASE OF OVERLAPPING MATCHES)

def count_overlapping_substrings(substring, string):
    count = 0
    length = len(substring)
    i = 0
    while i < len(string):
        if string[i:i + length] == substring:
            count += 1
            i += length     # <- Key line in case of a match; i + length so that it skips over rest of the characters
        else:
            i += 1          # <- This is the key line in case when no match
    return count


print(count_overlapping_substrings('code', 'code, code, code, all you need is code'))  # 4
print(count_overlapping_substrings('AA', 'AAAA'))  # 2


# using built-in Functions

# Finds if substring present in a string or not
print('cad' in 'abracadabra')  # True
print('gar' in 'abracadabra')  # False
print('d' in 'abracadabra')  # True

# Counting occurrence of a substring in a string (it always does that as a Non-OVERLAPPING case.)
print('code, code, code, all you need is code'.count('code'))  # 4
print('AAAA'.count('AA'))  # 2


