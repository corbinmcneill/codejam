# drummer2322
# corbin.mc96@gmail.com
# GCJ <year> <round> <problem>
# <date>

from sys import argv
from math import floor

if len(argv) > 1:
	type_of_case = argv[1]+'_'
else:
	type_of_case = ''
lines = [line[:-1] for line in open(type_of_case+'input.in')]
output = open(type_of_case+'output.out','w')

for t in range(1,int(lines.pop(0))+1):
	print t

	power = int(lines.pop(0))
	base = 3.0 + 5.0**.5

	number = 1.0;
	for i in range(power):
		number *= base
		number = number % 1000;

	number = str(int(floor(number) % 1000))
	number = "0"*(3-len(number)) + number

	output.write("Case #%i: %s\n"%(t, number ))

output.close()
