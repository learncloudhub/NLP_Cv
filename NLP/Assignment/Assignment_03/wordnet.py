import re
from nltk.corpus import wordnet
import random

sentence = input("Enter a sentence: ")
word = input("Enter a word to replace: ")

synsets = wordnet.synsets(word)

synonyms = set()
for syn in synsets:
    for lemma in syn.lemmas():
        synonyms.add(lemma.name().replace("_", " "))

synonyms.discard(word.lower())

selected_synonyms = random.choice(list(synonyms))

new_sentence = sentence.replace(word, selected_synonyms)

print(f"Original sentence: {sentence}")
print(f"Selected synonym: {selected_synonyms}")
print(f"New sentence: {new_sentence}")