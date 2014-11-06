# drummer2322
# corbin.mc96@gmail.com
# GCJ <year> <round> <problem>
# <date>

from sys import argv

if len(argv) > 1:
	type_of_case = argv[1]+'_'
else:
	type_of_case = ''

lines = [line.strip() for line in open(type_of_case+'input.in')];
output = open('old_output.out','w')

def examine(child):
	results = []
	for parent in tree[child]:
		results.append(parent)
		for result_item in examine(parent):
			results.append(result_item)
	return results;


for t in range(1,int(lines.pop(0))+1):
	print t

	number_of_classes = int(lines.pop(0))
	tree = {}
	for i in range(number_of_classes):
		tree[i+1] = map(int, lines.pop(0).split())[1:]
	
	answer = "No"

	for c1 in tree.keys():
		result_list = examine(c1)			
		for c2 in tree.keys():
			if result_list.count(c2)>1:
				answer="Yes"
				print c1
			
	output.write("Case #%i: %s\n"%(t, answer ))

output.close()
