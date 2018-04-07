def solve(case, n):
	marker = [False]*10
	p = n
	for i in range(101):
		stringN = str(n)
		for charN in stringN:
			marker[int(charN)] = True
			done = True
			for j in range(len(marker)):
				if not marker[j]:
					done = False
					break
			if done:
				print "Case #%d: %d"%(case,n)
				return
		n+=p
	print "Case #%d: INSOMNIA"%case

infile = open("input.txt", 'r')
T = int(infile.readline())

for t in range(1,T+1):
	N = int(infile.readline())
	solve(t, N)
