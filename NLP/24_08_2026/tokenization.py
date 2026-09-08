from nltk import word_tokenize, sent_tokenize

text = "Natural Language Processing is interesting. I have 10 books, 2 pens, and a laptop. AI is used in Yangon"

sentences = sent_tokenize(text)
print("Numbers of sentences:", len(sentences))
for sentence in sentences:
    print(sentence)


words = word_tokenize(sentence)

print("Numbers of words:", len(words))
print("\nWords")

for word in words:
    print(word)
    
