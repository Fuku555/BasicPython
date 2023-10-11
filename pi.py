import re

text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""
words=re.findall(r'\b\w+\b',text)
print(words)

charnumber=list(map(len,words))
print(charnumber)

charnumberconnect=''.join(map(str,charnumber))
print(charnumberconnect)