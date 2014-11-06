# drummer2322
# GCJ <year> <round>
# <date>

import operator

lines = [line.strip() for line in open('small_input.in')];
output = open('small_output.out','w')

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

for t in range(1,int(lines.pop(0))+1):

	print "CASE",t

	keys_entered, password_length = map(int,lines.pop(0).split())
	key_chances = map(float,lines.pop(0).split())

	reverse_key_chances = key_chances[::-1]
	product = prod(key_chances);
	expected = 2+password_length
	running_probability = 1;

	for i, chance in enumerate(key_chances):
		running_probability*=chance;
		strokes_if_right = 2*(keys_entered-i-1)+password_length - keys_entered+1
		strokes_if_wrong = strokes_if_right + password_length + 1
		new_expected = strokes_if_right*running_probability + strokes_if_wrong*(1 - running_probability)
		expected=min(expected,new_expected)

		# print "NEW", new_expected
		# print "Best", expected

	# print t, i
	output.write("Case #%i: %s\n"%(t, expected ))

output.close()