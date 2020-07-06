# This program has a collection of templates for building sentences,
# as well as collections of nouns (such as "iceberg" and "snake")
# and verbs (such as "caught" and "hacked").
# The templates for sentences look like this:The {{noun}} {{verb}} the {{noun}}.
# Then the program puts together a sentence by substituting random nouns and verbs into the template,
# creating masterpieces of modern English composition such as: The iceberg hacked the snake.

import random
from Fun_With_Strings import words  # importing words.py here


def silly_string(nouns, verbs, templates):
    template = random.choice(templates)  # Choose a random template.
    output = []  # We'll append strings into this list for output.
    index = 0  # Keep track of where in the template string we are.
    length_n = len('{{noun}}')  # length of string literal {{noun}}
    length_v = len('{{verb}}')  # length of string literal {{verb}}
    # while loop to loop over index positions of template.
    while index < len(template):
        if template[index:index + length_n] == '{{noun}}':
            output.append(random.choice(nouns))
            index = index + length_n
        elif template[index:index + length_v] == '{{verb}}':
            output.append(random.choice(verbs))
            index = index + length_v
        else:
            output.append(template[index])
            index = index + 1
    output = ''.join(output)  # After the loop has finished, join the output and return it.
    return output


# if __name__ == '__main__':
#   print(silly_string(words.nouns, words.verbs, words.templates))

# Or do python silly.py again & again to run the code
for i in range(5):
    print(silly_string(words.nouns, words.verbs, words.templates))
