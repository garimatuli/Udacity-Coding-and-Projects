def remove_substring(string, substring):
    output = []
    length = len(substring)
    i = 0
    while i < len(string):
        if string[i:i + length] == substring:
            i += length
        else:
            output.append(string[i])
            i += 1
    return ''.join(output)


def replace_substring(string, substring, replacement):
    output = []
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            output.append(replacement)
            index += len(substring)
        else:
            output.append(string[index])
            index += 1
    return "".join(output)


print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!'))  # Hello world!
print(remove_substring("Whoever<br> wrote this<br> loves break<br> tags!",
                       "<br>"))  # Whoever wrote this loves break tags!
print(remove_substring('I am NOT learning to code.', 'NOT '))  # I am learning to code.

print('\n')

print(replace_substring('Hot SPAM!drop soup, and curry with SPAM!plant.', 'SPAM!', 'egg'))
print(replace_substring("The word 'definately' is definately often misspelled.", 'definately', 'definitely'))