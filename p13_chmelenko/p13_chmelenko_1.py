import re
import collections, re

f = open('gadsby.txt')
d = f.read()

lines = 0
words = 0
letters = 0

def letterFrequency(txt):
    from collections import Counter
    from string import ascii_lowercase
    c=Counter(txt.lower())
    n=len(txt)/100.
    return [(x, c[x]/n) for x in ascii_lowercase]

for line in open('gadsby.txt'):
    lines += 1
    letters += len(line)

    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
print("Statistic:")
print("-" * 15)
print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)
print("-" * 15)

for k, v in collections.Counter(re.compile('[^a-z]').sub('', d)).items():
  print( k + ":", v)

print("-" * 15)
print(letterFrequency(d)) 
print("-" * 15)
