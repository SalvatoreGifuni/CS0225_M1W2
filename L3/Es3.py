# Conteggio parole

import re

st = "Ciao, ciao! Come stai? Stai bene?"

words = re.sub(r"\W", " ", st).lower().split()

count_words = {}

for word in words:
    i = words.count(word)
    count_words[word] = i

print(count_words)

