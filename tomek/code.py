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


def solve(case):
	matrix = []
	for i in range(4):
		matrix.append(lines.pop(0).split())
	
	game_done = True
	for i in range(4):
		validX = True;
		validO = True;
		for j in range(4):
			if matrix[i][j] == '.':
				game_done = False
				validX = False
				validO = False
				break
			elif matrix[i][j] == 'X':
				validO = False
			elif matrix[i][j] == 'O':
				validX = False
		if validX:
			print "Case #%d: X won"%t
			return
		if validO:
			print "Case #%d: O won"%t
			return


	for j in range(4):
		validX = True;
		validO = True;
		for i in range(4):
			if matrix[i][j] == '.':
				game_done = False
				validX = False
				validO = False
				break
			elif matrix[i][j] == 'X':
				validO = False
			elif matrix[i][j] == 'O':
				validX = False
		if validX:
			print "Case #%d: X won"%t
			return
		if validO:
			print "Case #%d: O won"%t
			return
	
	diagonal_points = [[0,0],[1,1],[2,2],[3,3]]
	validX=True
	validO=True
	for point in diagonal_points:
		if matrix[point[0]][point[1]] == "O":
			validX=False
		elif matrix[point[0]][point[1]] == "X":
			validO=False
		else
			validX=False
			validO=True
	
	if validX:
		print "Case #%d: X won"%t
		return
	if validO:
		print "Case #%d: O won"%t
		return

for t in range(1,int(lines.pop(0))+1):
	print t

	solve(t)

output.close()
