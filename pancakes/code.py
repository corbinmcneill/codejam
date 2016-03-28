# drummer2322
# corbin.mc96@gmail.com
# GCJ <year> <round> <problem>
# <date>

from sys import argv
from math import ceil

if len(argv) > 1:
	type_of_case = argv[1]+'_'
else:
	type_of_case = ''
lines = [line[:-1] for line in open(type_of_case+'input.in')]
output = open(type_of_case+'output.out','w')

for t in range(1,int(lines.pop(0))+1):
	print t

	numDiners = int(lines.pop(0));
	plates = list(map(int, lines.pop(0).split(" ")))
	total = sum(plates)
	specialNum = 0
	best = max(plates)
	for cutoff in range(1, max(plates)):
		moves = 0;
		for plate in plates:
			if plate>cutoff:
				moves += int(ceil(float(plate)/cutoff)) - 1
		best = min(best, cutoff+moves)

	output.write("Case #%i: %s\n"%(t, best))

output.close()
