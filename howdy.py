#=========================
#THE CONVERSATION FUNCTION
#=========================
def conversation(question):

#Open the file. Read lines into a list of lists.
    knowledge = []
    with open('knowledge.csv', 'r') as content_file:
	    for line in content_file:
    		knowledge.append(line.strip().split(','))

#Check if there is answer in the lists. If yes, gives back the answer. If no, gives back the question.
    answer = ""
    for line in knowledge:
	if line[0] == question:
	    print line[1]
	    answer = line[1]
    if answer == "":
	    print question

    next_question = raw_input()
    return next_question

#    target = open('knowledge.csv', 'a')
#    target.write(question)
#    target.write("\n")
#    target.close()


#==========================
#INTRO & CALLING FUNTCTIONS
#==========================
print "Hi, my name is Howdy! I don't know anything about the world. Please teach me!"

#Starts with user input.
question = ""
question = raw_input()

#calling the conversation function
while question != "exit":
    question = conversation(question)