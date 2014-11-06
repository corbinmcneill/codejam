lines = [line.strip() for line in open('input.in')];
output = open('output.out','w')

for t in range(1,int(lines.pop(0))+1):
	E, R, N = map(int,lines.pop(0).split())
	V = map(int,lines.pop(0).split())

	gain =0;
	energy = E;

	for i in range(len(V)):
		v = V[i];

		distanceFromHigher = 0
		for j in range(len(V[i+1:])):
			k=V[i+1:][j]
			if v<k:
				distanceFromHigher = j+1;
				break

		if distanceFromHigher==0:
			optimalSpend = energy;
		else :
			optimalSpend = min(R*distanceFromHigher-E+energy,energy)
		if optimalSpend<0 :
			optimalSpend = 0

		# print "Value of (%s): spend: %s of %s"%(v,optimalSpend,energy)

		energy -= optimalSpend-R
		gain += optimalSpend*v
		energy = min(energy,E)

	output.write("Case #%i: %i\n"%(t, gain))

output.close()