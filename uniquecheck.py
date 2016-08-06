importFile = 'wordList.txt'

f = open(importFile, 'r')

words = set()

none = True

for line in f:
    if line in words:
        print "Non unique fount: {0}".format(line[:-1])
        none = False
    else:
        words.add(line)

if none:
    print "Everything is unique."