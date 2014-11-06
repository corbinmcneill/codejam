# drummer2322
# GCJ 2013 1B
# 15 APR 2014

from itertools import combinations as c
import string

def changeLetterAtIndex(index, stringToChange):
	result = []
	for letter in string.ascii_lowercse:
		stringToChange[index] = letter;
		result.append(stringToChange)
	return result

lines = [line.strip() for line in open('input.in')];
output = open('output.out','w')
dictionary_words = [line.strip() for line in open('dictionary.txt')]

for t in range(1,int(lines.pop(0))+1):

	S = lines.pop(0)

	found_minimum = False;
	minimum = 100000000

	if S in dictionary_words:
		output.write("Case #%i: %s\n"%(t, "0" ))
		continue


	while not found_minimum:
		for number_of_altercations in range(1,len(S)):
			print number_of_altercations
			while not found_minimum:
				for number_of_swaps in range(number_of_altercations+1):
					print number_of_swaps
					number_of_spaces = number_of_altercations - number_of_swaps
					space_location_sets = c(range(1,len(S)),number_of_spaces);
					while not found_minimum:
						for space_locations in space_location_sets:
							s1=S
							for space_location in space_locations:
								str(list(s1).insert(space_location, ' '))
							swap_location_sets = c(range(len(s1)),number_of_swaps);
							s2=s1
							strings_to_apply_to = [s2]
							for swap_locations in swap_location_sets:
								result = []
								for swap_location in swap_locations:
									for string_to_apply_to in strings_to_apply_to:
										result+=changeLetterAtIndex(swap_location,string_to_apply_to)
								strings_to_apply_to = result
							passesTest=True
							for word in str(result).split():
								if word not in dictionary_words:
									passesTest=False
									break
							if passesTest:
								found_minimum =True
								minimum = number_of_altercations;

	output.write("Case #%i: %i\n"%(t, minimum ))

output.close()