# drummer2322
# corbin.mc96@gmail.com
# GCJ 2014 1C B
# 

from sys import argv
from string import ascii_lowercase as lower;
from math import factorial;

if len(argv) > 1:
	type_of_case = argv[1]+'_'
else:
	type_of_case = ''

lines = [line.strip() for line in open(type_of_case+'input.in')];
output = open(type_of_case+'output.out','w')

#returns if enough True's are in a list
def enoughTrue(mylist, minTrues):
	foundTrues = 0;
	for statement in mylist:
		if statement:
			foundTrues += 1;
		if foundTrues >= minTrues:
			return True;
	return False;

#case solving algorithm
def solve (input_string) :
	#parse input
	trains = input_string.split();

	#eliminate duplications in trains
	for i in xrange(len(trains)):
		train = trains[i][0]; #train will be a new version of trains[i] without duplicates
		rescent = train; #rescent will record the last unique train letter while scanning trains[i]
		for j in xrange(1, len(trains[i])):
			if trains[i][j] != rescent: #if scanned letter is unique:
				train += trains[i][j]; #add it to train
				rescent = trains[i][j]; #and set it as the new rescent
		trains[i] = train; #push duplication-free train back to train list "trains"
	
	
	#tests for internal letters that would need to be paired with an outer letter
	#if this situation exists, no solutions are possible
	#if not, internal parts of trains are negligible. internals are removed
	for i in xrange(len(trains)):
		if trains[i][0] == trains[i][-1] and len(trains[i]) > 2 :
			return 0
		for j in xrange(i, len(trains)):
			if (trains[i][0] in trains[j][1:-1]) or (trains[i][-1] in trains[j][1:-1]):
				return 0;
		trains[i] = [trains[i][0], trains[i][-1]];


	#checks for improper number of starts and stops
	#removes duplication of homogenous trains
	letter_multiplier = 1; #multiplier that accounts for remova of dublicate homogenous trains
	for letter in lower:
		homegeous_trains = 0; #number of homegenous trains of current letter
		starts = 0; #number of trains that only start with the current letter
		ends = 0; #number of trains that only end with the current letter
		start_letter = "";
		end_letter = "";
		for train in trains:
			if train[0] == train[1] == letter:
				homegeous_trains += 1;
			elif train[0] == letter:
				starts += 1;
				end_letter = train[1];
			elif train[1] == letter:
				ends += 1;
				start_letter=train[0];
		#only one train can start but not end with the same letter (and vice-versa)
		if max(starts, ends) > 1:
			return 0;
		letter_multiplier *= factorial(homegeous_trains); #considers homogenous train duplicates in multiplier
		#removes homogeous train duplicates
		for i in range(max(0, homegeous_trains-1)):
			trains.remove([letter,letter]);
	
	madeconnection = True;
	elimatedLetters = [];
	while madeconnection:
		for i, train1 in enumerate(trains):	
			madeconnection = False;
			for j, train2 in enumerate(trains):
				if i == j:
					continue;
				if [train1[1],train1[1]] in trains:
					if trains.index([train1[1],train1[1]]) != i:
						trains.remove([train1[1], train1[1]]);
						madeconnection = True;
						break;
				if train1[1] == train2[0]:
					trains.remove(train1);
					trains.remove(train2);
					trains.append([train1[0],train2[1]]);
					if train1[0] == train2[1]:
						return 0;
					madeconnection = True;
					break;
			if madeconnection:
				break;
	
	return (factorial(len(trains)) * letter_multiplier) % 1000000007;
		

#main loop
for t in range(1,int(lines.pop(0))+1):
	print t;
	number_of_trains = int(lines.pop(0));
	answer = solve(lines.pop(0));
	output.write("Case #%i: %s\n"%(t, answer));

output.close()

	

