lines = [line.strip() for line in open('input.in')];
output = open('output.out','w')
allvalues = range(1,17);

for case in range(int(lines.pop(0))):
	firstguess = lines.pop(0)
	firstmap = []
	secondmap = []
	for i in range(4):
		firstmap.append(map(int, lines.pop(0).split()));
	secondguess = lines.pop(0)
	secondmap = []
	for i in range(4):
		secondmap.append(map(int, lines.pop(0).split()));

	result = [];
	for i in allvalues:
		if (i in firstmap[int(firstguess)-1]) and (i in secondmap[int(secondguess)-1]):
			result.append(i);

	if len(result) == 1 :
		output.write("Case #%s: %s\n" %(case+1, result[0]))
	elif len(result) >= 1 :
		output.write("Case #%s: Bad magician!\n"% str(case+1))
	else:
		output.write("Case #%s: Volunteer cheated!\n"%str(case+1))





output.close()