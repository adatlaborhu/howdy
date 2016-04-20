import csv
#=====================
#THE CONVERSATION PART
#=====================
def conversation():

#Starts with user input.
    question = raw_input()

#Open the file. Read lines into a list of lists.
    knowledge = []
    with open('knowledge.csv', 'r') as content_file:
	    for line in content_file:
    		knowledge.append(line.strip().split(','))
    print knowledge[1][1]


#If there is an answer, gives back the answer. If there is no answer, gives back the question.
    if question in knowledge:
	print "OK"
    else:
	print question

#    target = open('knowledge.csv', 'a')
#    target.write(question)
#    target.write("\n")
#    target.close()


#=================
#CALLING FUNCTIONS
#=================
print "Hi, my name is Howdy! I don't know anything about the world. Please teach me!"
question = ""
while question != "exit":
    conversation()