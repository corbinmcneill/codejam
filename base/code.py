# drummer2322
# corbin.mc96@gmail.com
# GCJ <year> <round> <problem>
# <date>

from sys import argv
import string

if len(argv) > 1:
	type_of_case = argv[1]+'_'
else:
	type_of_case = ''
lines = [line[:-1] for line in open(type_of_case+'input.in')]
output = open(type_of_case+'output.out','w')

digits = string.digits + string.letters

for t in range(1,int(lines.pop(0))+1):
	print t

	message = lines.pop(0);
	base = len(set(list(message)))
	base_x = "";
	base_10 = 0;
	base_matching = {};

	current_number = 1
	for i, letter in enumerate(message):
		if not letter in base_matching.keys():
			base_matching[letter] = digits[current_number] # change digits in this line to modified digits
			current_number+=1
		base_x += base_matching[letter]
	
	print base_x
	
	base_x[::-1]
	for i, letter in base_x:
		base_10 += base**i * digits.index(letter)

	output.write("Case #%i: %s\n"%(t, base_10))

output.close()
