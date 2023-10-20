# Open the text file for reading using 'with' statement
with open('data.txt', 'r') as file:
    text = file.read()

# Convert the text to lowercase and split it into words
words = text.lower().split()

# Remove punctuation and possessive "'s" from each word
cleaned_words = [word.strip('.,!?()[]{}"\'') for word in words]

# Count word occurrences using a dictionary
word_count = {}
for word in cleaned_words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print unique words and their occurrences
for word, count in word_count.items():
    print(f"{word}: {count}")
