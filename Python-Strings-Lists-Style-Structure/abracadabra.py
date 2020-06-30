
def reverse_pattern(str):
    i = len(str)
    while i > 0:
        print(str[0:i])
        i -= 1


reverse_pattern("abracadabra")