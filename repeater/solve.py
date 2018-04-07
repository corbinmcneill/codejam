def simplify(string):
	result = ""
	result += string[0]
	for i in range(1,len(string)):
		if string[i-1] != string[i]:
			result += string[i]
	return result

def solve(casenum,data):
	simplified = []
	for i in range(len(data)):
		simplified.append(simplify(data[i]))
	for i in range(len(data)-1):
		if simplified[i] != simplified[i+1]:
			print "Case #%d: Fegla Won"%casenum
			return
	
	occurences = [[0 for i in range(len(simplified[0]))] for j in range(len(data))]
	for i in range(len(data)):
		index = 0
		for j in range(len(data[i])-1):
			occurences[i][index] += 1
			if (data[i][j] != data[i][j+1]):
				index+=1
	
	targets = []
	for i in range(len(simplified[0])):
		allvals=[]
		for j in range(len(occurences)):
			allvals.append(occurences[j][i])
		targets.append(sorted(allvals)[len(allvals)/2])

	total = 0
	for i in range(len(data)):
		for j in range(len(targets)):
			total += abs(targets[j] - occurences[i][j])
	
	print "Case #%d: %d"%(casenum,total)
	




infile = open("input.txt", 'r')
T = int(infile.readline())
for t in range(1,T+1):
	N = int(infile.readline())
	data=[]
	for n in range(N):
		data.append(infile.readline().strip())
	solve(t, data)

