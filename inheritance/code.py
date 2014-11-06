# drummer2322
# corbin.mc96@gmail.com
# GCJ <year> <round> <problem>
# <date>

import sys

print sys.setrecursionlimit(10000) # this recursion limit works. smaller limits may work. larger limits are allowed

if len(sys.argv) > 1:
	type_of_case = sys.argv[1]+'_'
else:
	type_of_case = ''

lines = [line.strip() for line in open(type_of_case+'input.in')];
output = open(type_of_case+'output.out','w')

found = False

def examine(child):
	global found

	working_list = tree[child][:] 
	
	for parent in tree[child]:
		if not found:
			working_list += examine(parent)
			if has_duplicates(working_list):
				found = True
				return []

	return working_list


def has_duplicates(check_list):
	return len(check_list) != len(set(check_list))

for t in range(1,int(lines.pop(0))+1):
	print t

	found = False

	number_of_classes = int(lines.pop(0))
	tree={}
	for i in range(number_of_classes):
		tree[i+1] = map(int, lines.pop(0).split())[1:]
	
	for i in range(number_of_classes):
		if not found:
			examine(i+1)
						
	output.write("Case #%i: %s\n"%(t, ["No", "Yes"][found] ))

output.close()
