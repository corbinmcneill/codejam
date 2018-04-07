def solve(caseNum, inN, inP, inR, inS):
	results = []
	for i in range(3):
		left = [inP, inR, inS]
		if left[i] == 0:
			continue
		building = [i] 
		left[i] -= 1 
		result = bottomLayer(inN-1, building, left)
		if result != "NONE":
			results.append(result)
	results=map(minimize,results)
	if len(results)>0:
		print "Case #%d: %s"%(caseNum, min(results))
	else:
		print "Case #%d: IMPOSSIBLE"%(caseNum)

def minimize(theString):
	length = len(theString)
	if length <= 1:
		return theString
	a = minimize(theString[:length/2])
	b = minimize(theString[length/2:])
	if a<b:
		return a+b
	else:
		return b+a

def bottomLayer(layersTillBottom, building, left):
	for i in xrange(len(building)):
		if not left[(building[i]+1)%3] > 0:
			return "NONE"
		left[(building[2*i]+1)%3] -= 1
		building.insert(i*2+1, (building[i]+1)%3)
	if layersTillBottom == 0:
		toReturn = ""
		ref = ["R","P","S"]
		for i in xrange(len(building)):
			toReturn += ref[building[i]]
		return toReturn
	else:
		return bottomLayer(layersTillBottom-1, building, left)

infile = open("input.in")
T = int(infile.readline())
for t in xrange(1, T+1):
	N,P,R,S = map(int, infile.readline().split(" "))
	solve(t,N,P,R,S)
