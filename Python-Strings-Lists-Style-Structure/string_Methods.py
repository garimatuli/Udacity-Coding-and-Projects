# Some built-in methods
# Check substring in string -> in , not in
# Locate substring in a string -> find
# Count substring in a string -> count
# join a substring in string -> join
# split a string with any character ch -> str.split("ch")

print('cad' in 'abracadabra')  # True
print('gar' in 'abracadabra')  # False

print('code, code, code, all you need is code'.count('code'))  # 4
print('AAAA'.count('AA'))  # 2

print('cookbook'.find('ook'))  # 1
print('codbook'.find('code'))  # -1

print(' '.join(['Hello', 'all', 'Good', 'Morning']))  # Hello all Good Morning
print(' silly '.join(['My', 'dog', 'has', 'fleas']))  # My silly dog silly has silly fleas
print('-'.join('cat'))  # c-a-t

lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

print('<br>'.join(lines))
print("\n")


def extract_place_with_split(filename):
    arr = filename.split("_")
    return arr[1]


# Here are some calls you can test it with:
print(extract_place_with_split("2016-11-04_Berlin_09/42/22.jpg"))
print(extract_place_with_split("2018-01-03_Oahu_21/51/57.jpg"))
print(extract_place_with_split("2018-01_Scottland_11/51/27.jpg"))


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