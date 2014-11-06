from sys import argv

if len(argv) > 1:
	type_of_case = argv[1]+'_'
else:
	type_of_case = ''

lines = [line.strip() for line in open(type_of_case+'input.in')];

for t in range(1,int(lines.pop(0))+1):

	number_of_classes = int(lines.pop(0))
	tree = {}
	for i in range(number_of_classes):
		tree[i+1] = map(int, lines.pop(0).split())[1:]

	print '#', t, ":", number_of_classes
