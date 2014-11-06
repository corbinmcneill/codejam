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

L, D, N = map(int, lines.pop(0).split());
permanent_dict = [];
for i in range(D):
	permanent_dict.append(lines.pop(0));

for t in range(1,N+1):
	print t

	case_dict = permanent_dict[:];	

	case_word = lines.pop(0);

	while not case_word=="":
		if case_word[0] != '(':
			required_letters=[case_word[0]];
			case_word=case_word[1:];
		else:
			closing_location = case_word.find(")");
			required_letters = case_word[1:closing_location];
			case_word=case_word[closing_location+1:]

		indexes_to_be_deleted = [];

		for i in range(len(case_dict)):
			if not case_dict[i][0] in required_letters:
				indexes_to_be_deleted.append(i);
			else:
				case_dict[i]=case_dict[i][1:];

		for i in indexes_to_be_deleted[::-1]:
			case_dict.pop(i);

	output.write("Case #%i: %s\n"%(t, len(case_dict) ))

output.close()
