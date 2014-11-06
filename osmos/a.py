lines = [line.strip() for line in open('input.in')];
output = open('output.out','w')

def leastToUse (A, nodes):
	a=A
	for i, mote in enumerate(nodes):
		
		if a> mote:
			if len(nodes)==i+1:
				return 0
			a+=mote
		else:
			if len(nodes)==i+1:
				return 1
			if a==1:
				return len(nodes)
			addcounter = 0
			while not a>mote:
				a+=(a-1)
				addcounter+=1
			
			return min(len(nodes[i:]),addcounter+leastToUse(a,nodes[i+1:]))
			


for t in range(1,int(lines.pop(0))+1):

	print t
	
	A, N = map(int, lines.pop(0).split())
	motes = map(int, lines.pop(0).split())

	motes.sort()

	output.write("Case #%i: %i\n"%(t, leastToUse(A,motes)))

output.close()

