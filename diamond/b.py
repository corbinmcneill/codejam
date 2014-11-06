from sys import argv
import math
import itertools

filename, inputfilename, outputfilename = argv

lines = [line.strip() for line in open(inputfilename)];
output = open(outputfilename,'w')

for t in range(1,int(lines.pop(0))+1):

	print t

	N, X, Y = map(int, lines.pop(0).split());

	if X<0:
		X=X*-1

	row = (X+Y)/2 #starting with 0 at increments of one
	numberUpSide=row*2 #not including top
	impossibles= (numberUpSide**2 - numberUpSide)/2 

	
	if X==0:
		impossibles = impossibles+numberUpSide*2
		if N> impossibles:
			percent=1.0
			output.write("Case #%i: %s\n"%(t, str(percent)))
			continue
		else:
			percent =0.0
			output.write("Case #%i: %s\n"%(t, str(percent)))
			continue

	if impossibles>=N:
		percent = 0.0
		output.write("Case #%i: %s\n"%(t, str(percent)))
		continue

	numberToFill = (numberUpSide+1)*(numberUpSide+2)/2
	if N>=numberToFill:
		percent = 1.0
		output.write("Case #%i: %s\n"%(t, str(percent)))
		continue

	extras = int(N-impossibles)

	# if extras>(numberUpSide)*2 :
	#  	print "ERROR",t #This line is being reached -- tofix
	
	allpossibilties = list(itertools.product((0,1), repeat = extras))
	newpossibles=[]
	for i, possible in enumerate(allpossibilties):
		print possible
		if not (possible.count(0)>numberUpSide or possible.count(1)>numberUpSide):
			newpossibles.append(possible)

	count =0
	
	for possible in newpossibles:
		if possible.count(0)>Y:
			count+=1

	print row, count, "out of", len(newpossibles), extras
	print newpossibles

	percent=float(count)/len(newpossibles);
	output.write("Case #%i: %s\n"%(t, str(percent)))
	
		
	

output.close()
