# Write a function called starts_with that takes two strings as arguments,
# and returns True if the first string starts with the second string,
# and False otherwise.


def starts_with(long_str, short_str):
    for i in range(len(short_str)):
        if long_str[i] != short_str[i]:
            return False
    return True


#  use string slicing
def starts_with_slicing(long_str, short_str):
    n = len(short_str)
    return long_str[0:n] == short_str


# A call like this should return True:
print(starts_with("apple", "app"))
print(starts_with_slicing("apple", "app"))

# And one like this should return False:
print(starts_with("manatee", "mango"))
print(starts_with_slicing("manatee", "mango"))


# using built-in method startswith
print("apple".startswith("app"))
print("manatee".startswith("mango"))
