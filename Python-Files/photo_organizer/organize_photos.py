import os


def photos_list(directory):
    os.chdir(directory)  # change working directory to "Photos"
    originals = os.listdir()  # get a list of all files in Photos directory and store it in variable originals
    return originals


# Extract the place name from the file name
def extract_place(filename):
    arr = filename.split("_")
    return arr[1]


# Make a directory for each place name
def make_place_directory(place_names):
    for place in place_names:
        os.mkdir(place)


def organize_photos(directory):
    place_names = []
    files_list = photos_list(directory)

    for file in files_list:
        place = extract_place(file)  # Extract the place name from the file name
        # only append a place to the places list if it isn't already in the list.
        # to avoid error like this :
        # FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'Berlin'
        if place not in place_names:  # This is the key change
            place_names.append(place)

    make_place_directory(place_names)  # Make a directory for each place name

    # Move files with a place name in respective place name directory
    for file_name in files_list:
        place = extract_place(file_name)
        new_name = os.path.join(place, file_name)
        print(new_name)
        os.renames(file_name, new_name)


# When you import a module, the code in that module gets run automatically. ie when we import organize_photos into
# some other program, organize_photos("Photos") will be executed automatically and we don't want that
organize_photos("Photos")


# To avoid above, we use "script footer"


