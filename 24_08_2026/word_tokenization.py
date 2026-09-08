import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

nltk.download('punkt_tab')

text = "I am studying Artificial Intelligence at U.S.A."

tokens = word_tokenize(text)

print("Original text:")
print(text)
print("\nTokenized Text:")
print(tokens)