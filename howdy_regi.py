#=================
#IMPORT COOL STUFF
#=================
import string
import json

#==============
#MAIN VARIABLES
#==============
sentences = 'knowledge_sentences.csv'
words = 'knowledge_words.json'
testfile = 'knowledge_test.csv'

#==============================================
#THE REMOVE PUNCTUATION AND UPPERCASES FUNCTION
#==============================================
def rmpu(x):
    return x.translate(string.maketrans("",""), string.punctuation).lower()

#==============================
#THE BASIC ML FUNCTION ON WORDS
#==============================
#Howdy learns what words can be correct answers for one word - based on the user's answers.
def mlwords(answer, next_question):
    worddict = ""
    with open('knowledge_words.json') as data_file:
	worddict = json.load(data_file)
    data_file.close()
    for aword in list(set(rmpu(answer).split())):
	if aword not in worddict:
	    worddict[aword] = {}
	for qword in list(set(rmpu(next_question).split())):
	    if qword in worddict[aword]:
		worddict[aword][qword] += 1
	    else:
		worddict[aword][qword] = 1

    with open('knowledge_words.json', 'w') as fp:
	json.dump(worddict, fp)
    fp.close()

#=========================
#THE CONVERSATION FUNCTION
#=========================
def conversation(question):

#Open the file. Read lines into a list of lists.
    knowledge = []
    with open(sentences, 'r') as content_file:
	alma = 0
	for line in content_file:
    	    knowledge.append(line.strip().split(';;;'))
	    knowledge[alma][2] = int(float(knowledge[alma][2]))
	    alma = alma + 1
	content_file.close()

#Check if there is answer in the lists. If yes, gives back the answer.
    answer = ""
    wereanswer = False
    weresamenext = False
    for line in knowledge:
	if rmpu(line[0]) == rmpu(question):
	    answer = line[1]
	    print "Howdy: " + answer
	    next_question = raw_input("You: ")
	    wereanswer = True
	    mlwords(answer, next_question)
	    break

#If there was an answer, check if he got the same next_question to that answer before. If yes, add + 1.
    if wereanswer is True:
	for line in knowledge:
	    if (rmpu(line[0]) == rmpu(answer) and rmpu(line[1]) == rmpu(next_question)):
		    line[2]= line[2]+1
		    knowledge = sorted(knowledge,key=lambda x: x[2], reverse=True)
		    weresamenext = True

#Save it to the sentences file.
    if (wereanswer is True and weresamenext is True):
	with open(sentences, 'w') as target:
	    for elements in knowledge:
		target.write(elements[0] + ";;;" + elements[1] + ";;;" + str(elements[2]) + "\n")
	    target.close()
	    return next_question

    if (wereanswer is True and weresamenext is False):
	target = open(sentences, 'a')
	target.write(answer + ";;;" + next_question + ";;;" + "1" + "\n")
	target.close()
	return next_question

#If howdy doesn't know the answer, he gives back the same question as an answer.
    if wereanswer is False:
	    answer = question
	    print "Howdy: " + answer
	    next_question = raw_input("You: ")
	    mlwords(answer, next_question)

#Save it to the sentences file.
	    target = open(sentences, 'a')
	    target.write(answer + ";;;" + next_question + ";;;" + "1" + "\n")
	    target.close()
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
