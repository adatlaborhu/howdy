#=========================
#THE CONVERSATION FUNCTION
#=========================
def conversation(question):

#Open the file. Read lines into a list of lists.
    knowledge = []
    with open('knowledge.csv', 'r') as content_file:
	    for line in content_file:
    		knowledge.append(line.strip().split(';;;'))
	    content_file.close()

#Check if there is answer in the lists. If yes, gives back the answer. If no, gives back the question.
    answer = ""
    for line in knowledge:
	if line[0] == question:
	    print "Howdy: " + line[1]
	    answer = line[1]
	    next_question = raw_input()
	    target = open('knowledge.csv', 'a')
	    target.write(answer + ";;;" + next_question + ";;;" + "1" + "\n")
	    target.close()
	    return next_question
    if answer == "":
	    print "Howdy: " + question
	    next_question = raw_input("You: ")
	    target = open('knowledge.csv', 'a')
	    target.write(question + ";;;" + next_question + ";;;" + "1" + "\n")
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
while question != "exit":
    question = conversation(question)