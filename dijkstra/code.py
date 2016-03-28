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

A = [1, 0, 0, 0]
I = [0, 1, 0, 0]
J = [0, 0, 1, 0]
K = [0, 0, 0, 1]
 
def negate(a):
	a = a[:]
	for i in range(4):
		a[i] *= -1
	return a;

def multiply(a, b): # return = a*b
	return [a[0] * b[0] - a[1] * b[1] - a[2] * b[2] - a[3] * b[3], 
	        a[0] * b[1] + a[1] * b[0] + a[2] * b[3] - a[3] * b[2], 
	        a[0] * b[2] + a[2] * b[0] + a[3] * b[1] - a[1] * b[3], 
	        a[0] * b[3] + a[1] * b[2] - a[2] * b[1] + a[3] * b[0]]

def solve(word):
	toReturn = A
	for letter in word:
		if letter=='i':
			toReturn = multiply(toReturn, I)
		if letter=='j':
			toReturn = multiply(toReturn, J)
		if letter=='k':
			toReturn = multiply(toReturn, K)
	return toReturn

# a = the number you want to remove from the front
# b = the number to remove from
# return = b after a is removed
def pulloff(a,b): # b = a * return
	for test in [A, I, J, K]:
		if multiply(a, test) == b:
			return test
		if multiply(a, negate(test)) == b:
			return negate(test)
	assert(False)

for t in range(1,int(lines.pop(0))+1):
	print t

	L, X = map(int, lines.pop(0).split(' '))
	line = lines.pop(0);

	line *= X

	if len(line)<3 or solve(line) != negate(A):
		output.write("Case #%i: %s\n"%(t, "NO" ))
		continue
	

	solved = False
	for second_pos in range(1, L*X-1):
		reset = True;
		for third_pos in range(second_pos, L*X):
			if (solve(line[:second_pos]) == [0,1,0,0] and solve(line[second_pos:third_pos])==[0,0,1,0] and solve(line[third_pos:])==[0,0,0,1]) :
				output.write("Case #%i: %s\n"%(t, "YES" ))
				solved = True
				continue

	if not solved:
		output.write("Case #%i: %s\n"%(t, "NO" ))

output.close()
