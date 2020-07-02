# Some built-in methods
# Check substring in string -> in , not in
# Locate substring in a string -> find
# Count substring in a string -> count
# join a substring in string -> join

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
