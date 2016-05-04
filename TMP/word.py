tesztdict = {"whats": {"your": 2, "name": 3}, "its":{"my": 2,"name": 3}}
answer = "hi whats my name"
next_question = "its tomi okkay"

for aword in list(set(answer.split())):
    if aword not in tesztdict:
	tesztdict[aword] = {}
    for qword in list(set(next_question.split())):
	if qword in tesztdict[aword]:
	    tesztdict[aword][qword] += 1
	else:
	    tesztdict[aword][qword] = 1