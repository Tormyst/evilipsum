import sys
import random

importFile = 'wordList.txt'

if sys.argv.count < 1:
    maxLines = 20
else:
    maxLines = int(sys.argv[1])

minPerLine = 20
maxPerLine = 25

f = open(importFile, 'r')

words = []

for line in f:
    words.append(line[:-1])

punctuation = ['. ', ',', '! ', '? ']

result = True


def write_word(cap):
    toreturn = False
    word = random.choice(words)
    if cap:
        word = word.capitalize()
    elif random.random() > 0.9:
        word = word + random.choice(punctuation)
        toreturn = True
    sys.stdout.write(word + ' ')
    return toreturn


for _ in range(maxLines):
    for _ in range(random.randrange(minPerLine, maxPerLine)):
        result = write_word(result)
    sys.stdout.write("\n")


