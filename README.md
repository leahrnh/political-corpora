Political Corpus Comparison
============================

This project compares Democrat and Republican debate and speech transcripts from the 2015-2016 primary season.

Corpus Stats
-------------
The entire corpus (with no pre-processing) consists of 200,048 words.
For each sub-corpus, approximately 75% of the corpus is from debates, and 25% is from speeches.
The Democrat corpus consists of 100,028 words, with 76,942 words from four different debates, and 23,086 words from seven different speeches.
The Republican corpus consists of 100,020 words, with 76,748 words from four different debates, and 23,272 words from eleven different speeches.
Post-processing, the Democrat corpus has 99,966 words, and the Republican corpus has 100,688 words.

dem_sent_lengths.csv and rep_sent_lengths.csv map the length of sentences to the number of times a sentence of that length occurs.
For example, "14,205" means that there are 205 sentences of length 14.
dem_word_distribution.csv and rep_word_distributions.csv map the numbers of times a word occurs to the number of words that occur that many times.
For example, "6,174" means that there are 174 word types that occur 6 times.

exclusive_words.txt lists words that occur ONLY in either the Democrat or Republican corpus.

Running the script (analyzeCorpus.py) also provides information about the number tokens and types in each corpus, and the comparative frequency of types in the different corpora.
