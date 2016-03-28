# drummer2322
# corbin.mc96@gmail.com
# GCJ APAC Round:A Problem:A
# 18 Jan 2015

#UNKNOWN BUG
from sys import argv

if len(argv) > 1:
	type_of_case = argv[1]+'_'
else:
	type_of_case = ''
lines = [line[:-1] for line in open(type_of_case+'input.in')]
output = open(type_of_case+'output.out','w')

numbers = ["1111110", "0110000", "1101101", "1111001", "0110011", "1011011", "1011111", "1110000", "1111111", "1111011"]
segments = "ABCDEFG"

for t in range(1,int(lines.pop(0))+1):
	print t

	allinfo = lines.pop(0).split()
	numberOfStates = int(allinfo[0])
	states = allinfo[1:] #all states passed from input

	validStarts = range(10);

	#for i in range(min(10, numberOfStates)):
	#	assert(len(validStarts)>0)
	#	impossibleStartStates = [];
	#	for start in validStarts:
	#		for segment in range(7):
	#			if states[i][segment] == "1" and numbers[start-i][segment] == "0":
	#				impossibleStartStates.append(start);
	#				print "impossible:", str(start-i)
	#				break
	#	for impossibleStartState in impossibleStartStates:
	#		validStarts.remove(impossibleStartState)

	for start in validStarts[:]:
		badStart = False;
		for i in range(min(10, numberOfStates)):
			for segment in range(7):
				if states[i][segment] == "1" and numbers[start-i][segment] == "0":
					validStarts.remove(start)
					badStart = True;
					print "impossible:", str(start-i), "\t segment:", segments[segment], "\tpattern:", states[i]
					break
			if badStart:
				break
	
	assert(len(validStarts) > 0)
	if len(validStarts) > 1:
		output.write("Case #%i: ERROR!\n"%(t))
		continue;
	
	assert(len(validStarts) == 1)
	validStart = validStarts[0]

	segmentOperationality = ["1"] * 7;
	for i in range(min(10, numberOfStates)):
		for segment in range(7):
			if states[i][segment] == "0" and numbers[validStart-i][segment] == "1":
				segmentOperationality[segment] = "0"
	
	display = "";
	for i in range(7):
		if numbers[validStart-(numberOfStates%10)][i] == "0" or segmentOperationality[i] == "0":
			display += "0"
		else:
			display += "1"

	output.write("Case #%i: %s\n"%(t, display))

output.close()
