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

keyboard = [' ', 'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
for t in range(1,int(lines.pop(0))+1):
	print t

	message = lines.pop(0);
	keypresses = []
	for letter in message:
		for i, button in enumerate(keyboard):
			for j, button_letter in enumerate(button):
				if letter==button_letter:
					if keypresses!=[] and keypresses[-1]==str(i+1):
						keypresses.append(' ')
					keypresses += [str(i+1)]*(j+1)

	for i in keypresses:
		if keypresses[i]=='1':
			keypresses[i]='0'

	output.write("Case #%i: %s\n"%(t, ''.join(keypresses)))

output.close()
