import os


# Example of some methods from os Module
# os.listdir()  # by default list the content of current directory you are in
# os.listdir('.')  # by default it gives list of files in current directory
# os.listdir("Photos")  # giving path of directory will list the files in Photos directory
# os.mkdir("Documents")  # creates a new directory named Documents
# mv file oldName from current directory to Documents directory and rename it to newName
# os.rename("oldName", "/Documents/newName")


os.chdir("Photos")  # change working directory to "Photos"
originals = os.listdir()  # get a list of all files in Photos directory and store it in variable originals
print(originals)  # Just for testing the code


def extract_place_with_slicing(filename):
    first_ = filename.find('_')
    partial_result = filename[first_ + 1:]
    second_ = partial_result.find('_')
    result = partial_result[:second_]
    return result


# Here are some calls you can use for testing:
print(extract_place_with_slicing("2016-11-04_Berlin_09/42/22.jpg"))
print(extract_place_with_slicing("2018-01-03_Oahu_21/51/57.jpg"))
print(extract_place_with_slicing("2018-01_Scottland_11/51/27.jpg"))


def extract_place_with_split(filename):
    arr = filename.split("_")
    return arr[1]


# Here are some calls you can test it with:
print(extract_place_with_split("2016-11-04_Berlin_09/42/22.jpg"))
print(extract_place_with_split("2018-01-03_Oahu_21/51/57.jpg"))
print(extract_place_with_split("2018-01_Scottland_11/51/27.jpg"))



# Actual Program

