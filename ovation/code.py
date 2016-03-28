# drummer2322
# corbin.mc96@gmail.com
# GCJ <year> <round> <problem>
# <date>

from sys import argv

if len(argv) > 1:
	type_of_case = argv[1]+'_'
else:
	type_of_case = ''
lines = [line[:-1] for line in open(type_of_case+'input.in')]
output = open(type_of_case+'output.out','w')

for t in range(1,int(lines.pop(0))+1):
	print t

	maxS, everyone = lines.pop(0).split(" "); 

	number_standing = 0;
	number_added = 0;
	for number_needed in range(int(maxS)+1):
		increment = max(0, number_needed-number_standing)
		number_added += increment;
		number_standing += increment + int(everyone[number_needed])

	output.write("Case #%i: %s\n"%(t, number_added ))

output.close()
