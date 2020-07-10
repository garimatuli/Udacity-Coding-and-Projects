# Profanity Filter Problem
# Finding rude words in a text
# Takes more time on average than fast_version.py
# Checking presence of each rude word in the text file

rude_words = ["crap", "jerk", "idiot", "Devil", "butt", "heckK", "darn"]

random_file = open("random.txt")
rude_count = 0
file_contents = random_file.read()
# print(file_contents)
for rude_word in rude_words:
    if rude_word in file_contents:
        rude_count += 1
        print(f"Found rude word: {rude_word}")
# print(rude_count)

if rude_count == 0:
    print("Your file has no rude words which I know.")

random_file.close()
