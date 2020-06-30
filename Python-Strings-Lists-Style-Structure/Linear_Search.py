# These functions takes a string argument and returns the portion of that string before the first dot character .

# Both functions are linear search
# we start at the beginning of a sequence & look at each item until we find one that matches what we're looking for.
# When we either find it, or run out of items, we stop.


def until_dot_while(s):
    index = 0
    while index < len(s) and s[index] != '.':
        # No dots yet, keep going.
        index += 1
    # We either found a dot or ran out of string.
    return s[:index]


def until_dot_for(s):
    for index in range(len(s)):
        if s[index] == '.':
            # A dot! Return everything up to here.
            return s[:index]
    # We ran out of string without seeing any dots.
    # Return the whole string.
    return s


print(until_dot_while("This is a sentence. This is another."))
print(until_dot_while("192.168.200.2"))
print(until_dot_while("No dots here"))
print("\n\n")
print(until_dot_for("This is a sentence. This is another."))
print(until_dot_for("192.168.200.2"))
print(until_dot_for("No dots here"))
