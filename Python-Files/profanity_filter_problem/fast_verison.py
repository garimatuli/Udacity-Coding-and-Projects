# Profanity Filter Problem
# Finding rude words in a text
# Checking each word from text file in the rude_words list
# Takes less time on average than slow_version.py

rude_words = ["crap", "jerk", "idiot", "Devil", "butt", "heck", "darn"]

with open("random.txt") as random_file:
    rude_count = 0
    for line in random_file:  # to read from file line by line, helps in case when file is too big to fit in memory
        # print(line)
        words = line.split(" ")
        # print(words)
        for word in words:  # taking one word at a time from words in the line from text file
            if word in rude_words:  # checking if the above word is present in rude_words list
                rude_count += 1
                print(f"Found rude word: {word}")
    if rude_count == 0:
        print("Your file has no rude words which I know.")
