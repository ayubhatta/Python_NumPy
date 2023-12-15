import numpy as np

s1 = 'Void is my name '
s2 = 'I am a God'

print(np.char.add(s1,s2))  # add both strings into a single line.
print("\n")

print(np.char.upper(s1)) # converts all letters into upper cases
print("\n")

print(np.char.lower(s1)) # converts all letters into lower cases
print("\n")

print(np.char.split(s1))  # breaks all the elements into different objects.
print("\n")


s3 = 'Void is my\nname'
print(np.char.splitlines(s3))  # the "\n" character breaks the string to a new line and the strings splits into 2 different objects
print("\n")

print(np.char.replace(s1, 'name', 'surname'))  # replaces the element 'name with 'surname' in string s1
print("\n")

print(np.char.center("Lord Void", 60, '*'))  # The element 'Lord Void' is kept at the center with 80 '*' at its sides keepint it at the center.