str = "This is an awesome occassion.This has never happened before"

char_occurences = {}

for char in str:
    char_occurences[char] = char_occurences.get(char,0)+1

print(char_occurences)