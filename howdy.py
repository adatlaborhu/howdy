#=================
#IMPORT COOL STUFF
#=================
import string
import json
from collections import Counter
import re

#==============
#MAIN VARIABLES
#==============
sentences = 'test_sentences.json'
words = 'knowledge_words.json'
testfile = 'knowledge_test.csv'

#==============================================
#THE REMOVE PUNCTUATION AND UPPERCASES FUNCTION
#==============================================
def rmpu(x):
    return x.translate(string.maketrans("",""), string.punctuation).lower()

def rmpu2(x):
    return re.sub("[\.\t\,\:;\(\)\.\!\?]", "", x, 0, 0).lower()

#==============================
#THE BASIC ML FUNCTION ON WORDS
#==============================
#Howdy learns what words can be correct answers for one word - based on the user's answers.
def mlwords(answer, next_question):
    worddict = ""
    with open('knowledge_words.json') as data_file:
	worddict = json.load(data_file)
    data_file.close()
    for aword in list(set(rmpu2(answer).split())):
	if aword not in worddict:
	    worddict[aword] = {}
	for qword in list(set(rmpu2(next_question).split())):
	    if qword in worddict[aword]:
		worddict[aword][qword] += 1
	    else:
		worddict[aword][qword] = 1

    with open(words, 'w') as fp:
	json.dump(worddict, fp)
    fp.close()

#===============================
#THE SAVE NEXT QUESTION FUNCTION
#===============================
def save_next_question(next_question, knowledge_new):
#    print "fire save next question"
    weresamenext = False
    rmpu_question = rmpu(next_question)
    for line in knowledge_new:
	if rmpu2(line) == rmpu_question:
	    knowledge_new[line][1] += 1
	    weresamenext = True
	    break

    if weresamenext == False:
	    new_sentence = [0, 1, 10]
	    new_sentence.append(rmpu_question.split())
	    knowledge_new[next_question] = new_sentence

    with open(sentences, 'w') as fp:
	json.dump(knowledge_new, fp)
    fp.close()

#=========================
#THE CONVERSATION FUNCTION
#=========================
def conversation(question):
    worddict = ""
    knowledge = {}
    knowledge_new = ""

#Open the known sentences and the known words.
    with open(words) as data_file:
	worddict = json.load(data_file)
    data_file.close()

    with open(sentences) as data_file:
	knowledge = json.load(data_file)
    data_file.close()

    with open(sentences) as data_file:
	knowledge_new = json.load(data_file)
    data_file.close()

#Check if there is answer in the lists. If yes, gives back the answer.
    answer = ""
    wereanswer = False
    weresamenext = False
    qs = question.split()
    for idx,lword in enumerate(qs):
	qs[idx]=rmpu(qs[idx])
	if qs[idx] in worddict:
	    d = Counter(worddict[qs[idx]])
	    for k, v in d.most_common(3):
		for xxx in knowledge:
		    if k in knowledge[xxx][3]:
			knowledge[xxx][0] += v
    for checker in knowledge:
	if knowledge[checker][0] > 0:
	    wereanswer = True
	    break

    if wereanswer is True:
	answer = max(knowledge, key=knowledge.get)
	print "Howdy: " + answer
	next_question = raw_input("You: ")
	mlwords(answer, next_question)
	save_next_question(next_question, knowledge_new)
	return next_question

#If howdy doesn't know the answer, he gives back the same question as an answer.
    if wereanswer is False:
	    answer = question
	    print "Howdy: " + answer
	    next_question = raw_input("You: ")
	    mlwords(answer, next_question)
	    save_next_question(next_question, knowledge_new)
	    return next_question

#==========================
#INTRO & CALLING FUNTCTIONS
#==========================
print "Hi, my name is Howdy! I don't know anything about the world. Please teach me!"

#Starts with user input.
question = ""
question = raw_input("You: ")

#calling the conversation function
while question != "bye":
    question = conversation(question)
