def conversation():
    question = raw_input()
    target = open('knowledge.csv', 'a')
    target.write(question)
    target.write("\n")
    target.close()

print "Hi, my name is Howdy! I'm a little baby right now, so I don't know anything about the world. Please teach me everything!"
conversation()