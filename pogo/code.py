# drummer2322
# GCJ <year> <round>
# <date>

from itertools import product

lines = [line.strip() for line in open('large_input.in')];
output = open('large_output.out','w')

directions = ['N','S','E','W']

for t in range(1,int(lines.pop(0))+1):
	print t

	#read input
	X,Y = map(int,lines.pop(0).split())

	Z = abs(X)+abs(Y)
	
	#N is the total traversal of the minimum number of jumps (building)
	N = 0

    #I is the minimum number of jumps (building)
	I = 0
	#build I and N
	while Z>N or (N-Z)%2==1: 
		I+=1
		N+=I
	#I AND N ARE BUILT


	xPos = 0
	yPos = 0
	neg = (N-Z)/2
	answer = ""

	for i in range(1,I+1)[::-1]:
		if i <= neg:
			neg -= i;
			if Y>0:
				answer += 'S'
				yPos-=i
			else:
				answer += 'N'
				yPos+=i
		elif i<=abs(X-xPos):
			if X>0:
				xPos+=i;
				answer += 'E'
			else:
				xPos-=i;
				answer += 'W'
		else:
			if Y>0:
				answer += 'N'
				yPos+=i;
			else:
				answer += 'S'
				yPos-=i;
	
	if X!=xPos or Y!=yPos:
		xPos = 0
		yPos = 0
		neg = (N-Z)/2
		answer = ""
		for i in range(1,I+1)[::-1]:
			if i <= neg:
				neg -= i;
				if X>0:
					answer += 'W'
					xPos-=i
				else:
					answer += 'E'
					xPos+=i
			elif i<=abs(Y-yPos):
				if Y>0:
					yPos+=i;
					answer += 'N'
				else:
					yPos-=i;
					answer += 'S'
			else:
				if X>0:
					answer += 'E'
					xPos+=i;
				else:
					answer += 'W'
					xPos-=i;

	assert X==xPos
	assert Y==yPos

	output.write("Case #%i: %s\n"%(t, answer[::-1]))

output.close()
