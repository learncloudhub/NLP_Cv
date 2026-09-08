from nltk.tokenize import sent_tokenize

text = "I am studying NLP. NLP is interesting. I want to learn more."

sentences = sent_tokenize(text)

print("Sentences:")
for sentence in sentences:
    print(sentence)