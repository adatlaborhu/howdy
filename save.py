import json
import string

def rmpu(x):
    return x.translate(string.maketrans("",""), string.punctuation).lower()

test_question = raw_input("You: ")
with open('test_sentences.json') as data_file:
    test_sentences = json.load(data_file)
data_file.close()

weresamenext = False

#print test_sentences
#print test_question
rmpu_question = rmpu(test_question)

for line in test_sentences:
    aline = line
    print rmpu(aline)
    if line == rmpu_question:
	test_sentences[line][1] += 1
	weresamenext = True
	break

if weresamenext == False:
	new_sentence = [0, 1, 10]
	new_sentence.append(rmpu_question.split())
#	print new_sentence
	test_sentences[test_question] = new_sentence
#	print test_sentences

#print test_sentences

#{"my name is tomi": [0, 1, 10, ["my", "name", "is", "tomi"]],
#"your name is tomi": [0, 1, 10, ["your", "name", "is", "tomi"]],
#"hello bello bye fine": [0, 1, 10, ["hello", "bello", "bye", "fine"]],
#"okkay tomi": [0, 1, 10, ["okkay", "tomi"]],
#"fine my name is tomi": [0, 1, 10, ["fine", "my", "name", "is", "tomi"]]}

