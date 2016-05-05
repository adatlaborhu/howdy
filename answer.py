import json
import string
from collections import Counter

def rmpu(x):
    return x.translate(string.maketrans("",""), string.punctuation).lower()

question = "lets okay to you"
worddict = ""

with open('knowledge_words.json') as data_file:
    worddict = json.load(data_file)
data_file.close()

with open('test_sentences.json') as data_file:
    test_sentences = json.load(data_file)
data_file.close()

print test_sentences

a = question.split()
probadict = {}

for idx,lword in enumerate(a):
    if a[idx] in worddict:
	d = Counter(worddict[a[idx]])
	print a[idx], d.most_common(3)
	for k, v in d.most_common(3):
	    for xxx in test_sentences:
		if k in test_sentences[xxx]:
		    print v
		    test_sentences[xxx][0] += v

print test_sentences
max(test_sentences, key=test_sentences.get)

#	maximum = max(worddict[a[idx]], key=worddict[a[idx]].get)
#	print maximum, worddict[a[idx]][maximum]


