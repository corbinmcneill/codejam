def opp(x):
	return (x+1)%2

def solve(casenum, inlist):
	inlist.pop(0)
	
	pos=[1,1]
	time=0
	waitingOn = 0

	queue = []
	while len(inlist) > 0:
		queue.append((1 if inlist.pop(0)=='O' else 0, int(inlist.pop(0))))

	primary = queue.pop(0)
	while len(queue) > 0:
		waitingOn = primary[0]
		primetime = abs(primary[1] - pos[waitingOn]) + 1
		pos[waitingOn]=primary[1]
		while (len(queue) > 0 and queue[0][0] == waitingOn):
			primary=queue.pop(0)
			primetime += abs(primary[1] - pos[waitingOn]) + 1
			pos[waitingOn]=primary[1]
		if (len(queue)>0):
			secondary = queue.pop(0)
			if primetime >= abs(pos[opp(waitingOn)] - secondary[1]):
				pos[opp(waitingOn)] = secondary[1]
			else:
				pos[opp(waitingOn)] = secondary[1] - (abs(pos[opp(waitingOn)] - secondary[1])) + primetime
			primary = secondary
			time+=primetime
		else:
			time+=primetime
			print "Case #%d: %d"%(casenum, time)
			return

	waitingOn = primary[0]
	time += abs(primary[1] - pos[waitingOn]) + 1
	print "Case #%d: %d"%(casenum, time)
	return 

infile = open("input.txt")
T =int(infile.readline().strip())

for t in range(1, T+1):
	solve(t, infile.readline().split(' '))

