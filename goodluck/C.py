# THIS CODE IS NOT YET FINISHED

import math;

lines = [line.strip() for line in open('input.in')];
output = open('output.out','w')

for t in range(1,int(lines.pop(0))+1):
	R, N, M, K = map(int, lines.pop(0).split())
	numbers = range(2,M+1)
	for i, products in enumerate(map(int, lines.pop(0).split())):
		commonfactors = []
		factors=[]
		for product in products:
			factors.append(getAllFactors(product))
		for k in factors[0]:
			for l in range(i,len(factors)):
				if not k in factors[l]:
					break;
			else:
				commonfactors.append(k);

				








	output.write("Case #%i: %i\n"%(t, gain))

output.close()


def getAllFactors(n):
	n=int(n)
	result = [n]
	for i in range(1,n+1):
		j = float(n)/i
		if j == math.floor(j) and j>1:
			result.append(i);
			result+=getAllFactors(i)

	result = list(set(result));
	result.sort()
	return result

print getAllFactors(1)