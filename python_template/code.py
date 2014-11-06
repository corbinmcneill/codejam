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

	#code goes here

	output.write("Case #%i: %s\n"%(t, answer ))

output.close()
