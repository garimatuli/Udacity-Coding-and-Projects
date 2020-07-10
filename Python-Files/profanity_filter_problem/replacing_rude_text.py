# Profanity Filter Problem
# Replacing rude words in a text file and create a new file


import string

rude_words = ["crap", "jerk", "idiot", "devil", "butt", "heck", "darn"]


def check_line(line):
    replaced_str = line
    words = line.split(" ")
    rude_list = []
    for word in words:  # taking one word at a time from words in the line from text file
        word = word.lower()  # lower() to solve the capitalization bug!!
        word = word.strip(string.punctuation)
        if word in rude_words:  # checking if the above word is present in rude_words list
            rude_list.append(word)
            # print("rude word = " + word)
    for rude in rude_list:
        replaced_str = replaced_str.lower().replace(rude, "****")
    return replaced_str


def write_file(filename):
    created_file = open("rude_replaced.txt", "w")
    with open(filename) as random_file:
        for line in random_file:
            # print("\n line = " + line)
            new_line = check_line(line.strip('\n'))
            # print("new_line = " + new_line)
            created_file.write(new_line+"\n")
    created_file.close()


if __name__ == '__main__':
    write_file("random_with_punctuations.txt")

    print("Original File Contents:-")
    original_file = open("random_with_punctuations.txt")
    print(original_file.read())
    original_file.close()
    print("Replaced File Contents:-")
    with open("rude_replaced.txt") as replaced_file:
        print(replaced_file.read())

