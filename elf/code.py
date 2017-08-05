# drummer2322
# corbin.mc96@gmail.com
# GCJ <year> <round<
# <date>

from sys import argv;

if len(argv) > 1:
	type_of_case = argv[1]+'_';
else:
	type_of_case = '';

lines = [line.strip() for line in open(type_of_case+'input.in')];
output = open(type_of_case+'output.out','w');

def solve(n,d,depth):

	n=int(n)
	d=int(d)

	# print "node",n,d

	if depth>40:
		return "impossible";

	if n==d:
		print "at",depth,"same", d
		return depth;

	n,d = simplify(n,d)

	print "node",n,d,depth

	n1,d1 = simplify(n+1,d);
	n2,d2 = simplify(n-1,d);

	if (d1<=d2 and n1!=0) or d2==0:
		return solve(n1,d1,depth+1)
	else :
		return solve(n2,d2,depth+1)

def simplify(n,d):
	if n==0:
		return 0,0
	for i in range(1,n+1)[::-1]:
		if int(n)%i==0 and int(d)%i==0:
			n=n/i
			d=d/i
	return n,d


for t in range(1,int(lines.pop(0))+1):
	print t

	n, d = lines.pop(0).split("/");

	n= int(n)
	d= int(d)

	n,d = simplify(n,d)

	check = 1.0;
	while check<d:
		check*=2
	if check!=d:
		output.write("Case #%i: impossible\n"%t);
		continue;

	if d==1:
		output.write("Case #%i: 0\n"%t);
		continue;

	generation = solve(n,d,0)
	output.write("Case #%i: %s\n"%(t, generation ))

output.close()
