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

for t in range(1,int(lines.pop(0))+1):
	print t

	amount_of_money = int(lines.pop(0));
	number_of_store_items = int(lines.pop(0));

	items = map(int, lines.pop(0).split());

	found = False;
	for i in range(len(items)):
		if not found:
			for j in range(i+1,len(items)):
				if items[i]+items[j] == amount_of_money:
					found = True;
					output.write("Case #%i: %s %s\n"%(t, i+1, j+1 ))
					break;

output.close()
