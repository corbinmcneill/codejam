def solve(caseNum, contents):
	result = 0
	for i in range(len(contents)-1):
		if contents[i]!=contents[i+1]:
			result+=1
	if not contents[len(contents)-1]:
		result+=1
	print "Case #%d: %d"%(caseNum, result)


infile = open("input.in", 'r')
T = int(infile.readline())
for t in range(1, T+1):
	intext = infile.readline()
	contents = []
	for inchar in intext:
		if inchar == "+":
			contents.append(True)
		elif inchar == "-":
			contents.append(False)
	solve(t, contents)

