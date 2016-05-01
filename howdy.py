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
	    for line in content_file:
    		knowledge.append(line.strip().split(';;;'))
	    content_file.close()

#Check if there is answer in the lists. If yes, gives back the answer. If no, gives back the question.
    answer = ""
    for line in knowledge:
	if line[0].translate(string.maketrans("",""), string.punctuation).lower() \
		== question.translate(string.maketrans("",""), string.punctuation).lower():
	    print "Howdy: " + line[1]
	    answer = line[1]
	    next_question = raw_input("You: ")
	    for line in knowledge:
		if (line[0].translate(string.maketrans("",""), string.punctuation).lower() \
		     == answer.translate(string.maketrans("",""), string.punctuation).lower() \
		     and line[1].translate(string.maketrans("",""), string.punctuation).lower() \
		     == next_question.translate(string.maketrans("",""), string.punctuation).lower()):
		    line[2]= str(int(float(line[2]))+1)
		    print line

#	    Save it to the sentences file.
	    with open(sentences, 'w') as target:
		for elements in knowledge:
		    target.write(elements[0] + ";;;" + elements[1] + ";;;" + elements[2] + "\n")
		target.close()

#	    Save it to the words file.
	    target = open(words, 'a')
	    next_question2 = next_question.replace(" ","\n")
	    target.write(next_question2 + "\n")
	    target.close()

	    return next_question

    if answer == "":
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
