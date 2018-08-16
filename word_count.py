str = "This is an awesome occasion. This has never happened before"

char_occurences = {}

for char in str:
    char_occurences[char] = char_occurences.get(char, 0)+1

print(char_occurences)

word_occurences = {}

for word in str.split():
    word_occurences[word] = word_occurences.get(word, 0) + 1

print(word_occurences)