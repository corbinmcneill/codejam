# drummer2322
# corbin.mc96@gmail.com
# GCJ <year> <round<
# <date>

from sys import argv

if len(argv) > 1:
	type_of_case = argv[1]+'_'
else:
	type_of_case = ''

def to_int(binary):
	return int(str(binary),2)

def to_bin(integer):
	return bin(integer)[2:]

lines = [line.strip() for line in open(type_of_case+'input.in')];
output = open(type_of_case+'output.out','w')

for t in range(1,int(lines.pop(0))+1):

	#code goes here


	output.write("Case #%i: %s\n"%(t, answer ))

output.close()