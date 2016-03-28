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
examples = [line[:-1] for line in open('examples.in')]
output = open(type_of_case+'output.out','w')

mapping = {'z':'q', 'y':'a', 'e':'o', 'q':'z'}

for t in range(int(examples.pop(0))):
	original = examples.pop(0)
	new = examples.pop(0)
	for i in range(len(original)):
		mapping[new[i]] = original[i]

for item in mapping:
	print item + " " + mapping[item]

print len(mapping)

for t in range(1,int(lines.pop(0))+1):
	print t

	encoded = lines.pop(0)
	answer = ""

	for letter in encoded:
		answer+=mapping[letter]

	output.write("Case #%i: %s\n"%(t, answer ))


output.close()
