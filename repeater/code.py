# drummer2322
# corbin.mc96@gmail.com
# GCJ <year> <round<
# <date>

from sys import argv

if len(argv) > 1:
	type_of_case = argv[1]+'_'
else:
	type_of_case = ''

lines = [line.strip() for line in open(type_of_case+'input.in')];
output = open(type_of_case+'output.out','w')

for t in range(1,int(lines.pop(0))+1):

	number_of_strings = int(lines.pop(0))

	originals = []
	for i in xrange(number_of_strings):
		originals.append(list(lines.pop(0)))

	original = [originals[0][0]];
	for letter in originals[0]:
		if letter != original[-1]:
			original.append(letter)
	original=str(original)

	for test in originals:
		seen = []
		new = []
		for letter in test:
			if len(seen)==0 or letter != seen[-1]:
				seen.append(letter)
				new.append(letter)
		if str(new) != original:
			# print str(original)
			# print str(new)
			break
	else:

		occurences = []
		for index, s in enumerate(originals):
			occurences.append([])
			count = 0
			for i in xrange(len(originals[index])):
				count+=1
				if i ==len(originals[index])-1:
					occurences[index].append(count)
				else:
					if s[i]!=s[i+1]:
						occurences[index].append(count)
						count=0
		for i in range(len(originals)):
			print ''.join(originals[i])
			print occurences[i]

		totaldistance = 0

		for i in xrange(len(occurences[0])):
			distance = 0
			allvalues = sorted([x[i] for x in occurences])
			
			median = allvalues[len(occurences)/2] 

			for number in [x[i] for x in occurences]:
				distance+=abs(number-median)
			# print "median",median
			# print "distance", distance
			totaldistance+=distance

		output.write("Case #%i: %s\n"%(t, totaldistance ))
		continue

	output.write("Case #%i: Fegla Won\n"%(t))

output.close()