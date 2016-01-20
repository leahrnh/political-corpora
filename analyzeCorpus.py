import os
import glob
import re

def process_line(line, sentLengths, wordOccurrences, numWords):
    for sentence in re.split('(\.|\?|!)', line):
        # remove any words in parenthesis (tends to be (APPLAUSE) etc.)
        p = re.compile(r'\([A-Za-z]+\)', re.DOTALL)
        sentence = p.sub(' ', sentence)

        # remove anything at the beginning of a sentence with all caps and colon. Ex. TRUMP:
        p = re.compile(r'^[A-Z]+:', re.DOTALL)
        sentence = p.sub(' ', sentence)

        # remove all punctuation
        p = re.compile(r'[^A-Za-z0-9 ]', re.DOTALL)
        sentence = p.sub(' ', sentence)

        # lowercase everything
        sentence = sentence.lower()

        # split into words
        words = sentence.split()

        # record occurrence of a sentence with this number of words
        sentenceLength = len(words)
        if sentenceLength in sentLengths:
            sentLengths[sentenceLength] += 1
        else:
            sentLengths[sentenceLength] = 1

        # record occurrence of this word
        for word in words:
            numWords += 1
            if word in wordOccurrences:
                wordOccurrences[word] += 1
            else:
                wordOccurrences[word] = 1
        return (sentLengths, wordOccurrences, numWords)

corpusPath = os.getcwd()
# iterate over files in the corpus
demSentLengths = {}
repSentLengths = {}
demWordOccurrences = {}
repWordOccurrences = {}
demNumWords = 0
repNumWords = 0
for fileName in glob.glob("democrat/*.txt"):
    filePath = corpusPath + '/' + fileName
    file = open(filePath, 'r')
    print("Processing :" + filePath)
    for line in file:
        (demSentLengths, demWordOccurrences, demNumWords) = process_line(line, demSentLengths, demWordOccurrences, demNumWords)

for fileName in glob.glob("republican/*.txt"):
    filePath = corpusPath + '/' + fileName
    file = open(filePath, 'r')
    print("Processing :" + filePath)
    for line in file:
        (repSentLengths, repWordOccurrences, repNumWords) = process_line(line, repSentLengths, repWordOccurrences, repNumWords)

print("Republican number of words: " + str(repNumWords))
print("Democrat number of words: " + str(demNumWords))
print("Republican word types: " + str(len(repWordOccurrences)))
print("Democrat word types: " + str(len(demWordOccurrences)))
print("Republican normalized word types: " + str(float(len(repWordOccurrences)) / repNumWords))
print("Democrat normalized word types: " + str(float(len(demWordOccurrences)) / demNumWords))