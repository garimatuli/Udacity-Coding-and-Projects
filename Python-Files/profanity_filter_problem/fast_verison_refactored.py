# Profanity Filter Problem
# Finding rude words in a text
# Checking each word from text file in the rude_words list
# Takes less time on average than slow_version.py
# Refactored

rude_words = ["crap", "jerk", "idiot", "Devil", "butt", "heck", "darn"]


def check_line(line):
    count = 0
    words = line.split(" ")
    # print(words)
    for word in words:  # taking one word at a time from words in the line from text file
        if word in rude_words:  # checking if the above word is present in rude_words list
            count += 1
            print(f"Found rude word: {word}")
    return count


def check_file(filename):
    with open(filename) as random_file:
        rude_count = 0
        for line in random_file:  # to read from file line by line, helps in case when file is too big to fit in memory
            # print(line)
            rude_count = rude_count + check_line(line)
        print(f'There are {rude_count} rude words in this file!!')
        if rude_count == 0:
            print("Your file has no rude words which I know.")


if __name__ == '__main__':
    check_file("random.txt")
