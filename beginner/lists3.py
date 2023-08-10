words = input().split()

small = 0
long = 100000

new_words = ["", ""]

for word in words:
    if len(word) > long:
        new_words[0] = word
    if len(word) < small:
        new_words[1] = word
        
print(new_words)