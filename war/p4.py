lines = [line.strip() for line in open('input.in')];
output = open('output.out','w')


for case in range(1,int(lines.pop(0))+1):

	blocksPerPlayer = int(lines.pop(0));
	nBlocks = map(float, lines.pop(0).split())
	kBlocks = map(float, lines.pop(0).split())
	nBlocks.sort()
	kBlocks.sort()

	scores = [0,0]

	used=[]
	for nBlock in nBlocks:
		for kBlock in kBlocks:
			if kBlock>nBlock and kBlock not in used:
				used.append(kBlock);
				break;
		else:
			for kBlock in kBlocks:
				if kBlock not in used:
					used.append(kBlock)
					break
			scores[0]+=1

	used=[]
	for nBlock in nBlocks:
		for kBlock in kBlocks:
			if nBlock > kBlock and kBlock not in used:
				scores[1]+=1
				used.append(kBlock);
				break

	output.write("Case #%i: %i %i\n"%(case, scores[1],scores[0]));


output.close();