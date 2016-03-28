# drummer2322
# corbin.mc96@gmail.com
# GCJ <year> <round> <problem>
# <date>

from sys import argv
import math

if len(argv) > 1:
	type_of_case = argv[1]+'_'
else:
	type_of_case = ''
lines = [line[:-1] for line in open(type_of_case+'input.in')]
output = open(type_of_case+'output.out','w')

def numRecycled(n):
	toReturn = 0
	strN = str(n)
	already_found = []
	for i in range(1, length):
		if not strN[-i] == "0":
			new = int(strN[-i:] + strN[:-i])
			if new <= B and new > n and new not in already_found:
				toReturn+=1
				already_found.append(new)
	return toReturn



for t in range(1,int(lines.pop(0))+1):
	print t

	recycled = 0

	A, B = map(int, lines.pop(0).split())

	strA = str(A)
	strB = str(B)
	length = len(strA)

	for n in range(A, B):
		recycled+=numRecycled(n)

	output.write("Case #%i: %d\n"%(t, recycled))

output.close()
