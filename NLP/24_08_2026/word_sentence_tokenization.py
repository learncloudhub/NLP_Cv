from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

text = "Natural language Processing is a field of Artificial Intelligence. It allows computers to understand human language."

sentences = sent_tokenize(text)

print("Number of sentences:", len(sentences))
print("\nSentences:")

for sentence in sentences:
    print(sentence)

words = word_tokenize(text)

print("Number of words", len(words))
print("\nWords:")

for word in words:
    print(word)
    
