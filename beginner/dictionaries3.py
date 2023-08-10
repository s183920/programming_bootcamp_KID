"""
1. Create a dictionary to store word frequencies. 
2. Ask the user to input a sentence. 
3. Split the sentence into words and count how many times each word appears. 
4. Display the word frequencies.
"""

word_frequencies = {}
sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    word = word.lower()
    word = word.replace(".", "").replace(",", "")
    if word in word_frequencies:
        word_frequencies[word] += 1
    else:
        word_frequencies[word] = 1

print(word_frequencies)
