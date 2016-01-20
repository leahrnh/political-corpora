import os
import glob
import re
import csv


def process_line(l, sent_lengths, word_occurrences, num_words):
    for sentence in re.split('(\.|\?|!)', l):
        # remove any words in parenthesis (tends to be (APPLAUSE) etc.)
        p = re.compile(r'\([A-Za-z]+\)', re.DOTALL)
        sentence = p.sub(' ', sentence)

        # remove anything at the beginning of a sentence with all caps and colon. Ex. TRUMP: or AUDIENCE MEMBERS:
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
        if sentenceLength in sent_lengths:
            sent_lengths[sentenceLength] += 1
        else:
            sent_lengths[sentenceLength] = 1

        # record occurrence of this word
        for word in words:
            num_words += 1
            if word in word_occurrences:
                word_occurrences[word] += 1
            else:
                word_occurrences[word] = 1
    return sent_lengths, word_occurrences, num_words

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

# write sentence length info to csv file
with open('dem_sent_lengths.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(['Sentence length', 'Democrat Occurrences'])
    for key in demSentLengths:
        writer.writerow([key, demSentLengths[key]])

with open('rep_sent_lengths.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(['Sentence length', 'Republican Occurrences'])
    for key in repSentLengths:
        writer.writerow([key, repSentLengths[key]])

# write word occurence distribution
dem_word_distribution = {}
for word in demWordOccurrences:
    num = demWordOccurrences[word]
    if num in dem_word_distribution:
        dem_word_distribution[num] += 1
    else:
        dem_word_distribution[num] = 1

rep_word_distribution = {}
for word in repWordOccurrences:
    num = repWordOccurrences[word]
    if num in rep_word_distribution:
        rep_word_distribution[num] += 1
    else:
        rep_word_distribution[num] = 1

with open('dem_word_distribution.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(['Word frequency', 'Number of words'])
    for key in dem_word_distribution:
        writer.writerow([key, dem_word_distribution[key]])

with open('rep_word_distribution.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(['Word frequency', 'Number of words'])
    for key in rep_word_distribution:
        writer.writerow([key, rep_word_distribution[key]])

