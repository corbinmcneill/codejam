# drummer2322
# corbin.mc96@gmail.com
# GCJ <year> <round> <problem>
# <date>

from sys import argv
import itertools

if len(argv) > 1:
	type_of_case = argv[1]
else:
	type_of_case = ''
lines = [line[:-1] for line in open(type_of_case)]

data = [[0 for x in range(10)] for x in range(10)]

acts = int(lines.pop(0))
for s in range(acts):
	for t in range(acts):
		if s != t:
			conflicts = 0
			for letter in lines[s]:
				if letter in list(lines[t]):
					conflicts += 1
			data[s][t] = conflicts

trials = itertools.permutations(range(acts),acts)

best_distance = 1000000000;
for trial in trials:
	distance = 0;
	for i in range(acts-1):
		distance += data[trial[i]][trial[i+1]]
	if distance < best_distance:
		best_distance = distance

print "Best Distance:  %i"%best_distance
