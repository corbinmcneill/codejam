infile = open("input.txt",'r')
fileline = [line for line in infile.readlines()]

def solve(t):
	R, C = map(int, fileline.pop(0).split())
	grid=[]
	for r in range(R):
		grid.append(list(fileline.pop(0)))
	count = 0;
	for i in range(R):
		for j in range(C):
			bad = True;
			if grid[i][j] =='^':
				for I in range(0,i):
					if grid[I][j] != ".":
						bad = False
			if grid[i][j] =='v':
				for I in range(i+1,R):
					if grid[I][j] != ".":
						bad = False
			if grid[i][j] =='>':
				for J in range(j+1,C):
					if grid[i][J] != ".":
						bad = False
			if grid[i][j] =='<':
				for J in range(0,j):
					if grid[i][J] != ".":
						bad = False
			if grid[i][j] =='.':
				bad = False;

			if bad:
				count+=1;
	print("Case #%d: %d"%(t,count));

T = int(fileline.pop(0))

for t in range(1, T+1):
	solve(t)
