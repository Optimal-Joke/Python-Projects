sentence = "This is a common interview question"

letters = {}
for letter in sentence.lower():
    if not letter in letters.keys():
        letters[letter] = sentence.count(letter)

highest_count = 0
for letter, count in letters.items():
    if count > highest_count:
        highest_count = count
        most_common_letter = letter

print(f"{most_common_letter}, {highest_count}")
