#=================
#IMPORT COOL STUFF
#=================
import string

#=========
#VARIABLES
#=========
sentences = 'knowledge_sentences.csv'
words = 'knowledge_words.csv'
testfile = 'knowledge_test.csv'

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
	if line[0].translate(string.maketrans("",""), string.punctuation).lower() \
		== question.translate(string.maketrans("",""), string.punctuation).lower():
	    answer = line[1]
	    print "Howdy: " + answer
	    next_question = raw_input("You: ")
	    wereanswer = True
	    break

#If there was an answer, check if he got the same next_question to that answer before. If yes, add + 1.
    if wereanswer is True:
	for line in knowledge:
	    if (line[0].translate(string.maketrans("",""), string.punctuation).lower() \
		 == answer.translate(string.maketrans("",""), string.punctuation).lower() \
		and line[1].translate(string.maketrans("",""), string.punctuation).lower() \
	        == next_question.translate(string.maketrans("",""), string.punctuation).lower()):
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

#	    Save it to the words file.
#	    target = open(words, 'a')
#	    next_question2 = next_question.replace(" ","\n")
#	    target.write(next_question2 + "\n")
#	    target.close()


    if wereanswer is False:
	    print "Howdy: " + question
	    next_question = raw_input("You: ")

#	    Save it to the sentences file.
	    target = open(sentences, 'a')
	    target.write(question + ";;;" + next_question + ";;;" + "1" + "\n")
	    target.close()

#	    Save it to the words file.
	    target = open(words, 'a')
	    next_question2 = next_question.replace(" ","\n")
	    target.write(next_question2 + "\n")
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
