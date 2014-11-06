# drummer2322
# GCJ <year> <round>
# <date>

from itertools import product

lines = [line.strip() for line in open('small_input.in')];
output = open('small_output.out','w')

directions = ['N','S','E','W']

for t in range(1,int(lines.pop(0))+1):

	X,Y = map(int,lines.pop(0).split())
	answer=""

	if X>=0:
		answer+="WE"*X
	else:
		answer+="EW"*(X*-1)

	if Y>=0:
		answer+="SN"*Y
	else:
		answer+="NS"*(Y*-1)


	output.write("Case #%i: %s\n"%(t, answer))

output.close()