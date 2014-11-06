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
	
	print t
	
	num_existing_conditions, num_needed_conditions = map(int, lines.pop(0).split())

	existing = set([])
	counter = 0


	for i in range(num_existing_conditions):
		condition = lines.pop(0).split("/")[1:]
		for j in range(1, len(condition)):
			if not '/'.join(condition[:j]) in existing:
				existing.add('/'.join(condition[:j]))	
		if not '/'.join(condition[:]) in existing:
			existing.add('/'.join(condition[:]))	

	for i in range(num_needed_conditions):
		condition = lines.pop(0).split("/")[1:]
		for j in range(1, len(condition)):
			if not '/'.join(condition[:j]) in existing:
				existing.add('/'.join(condition[:j]))	
				counter+=1
		if not '/'.join(condition[:]) in existing:
			counter+=1
			existing.add('/'.join(condition[:]))	
	output.write("Case #%i: %s\n"%(t, counter))

output.close()
