# drummer2322
# GCJ <year> <round>
# <date>

lines = [line.strip() for line in open('large_input.in')];
output = open('large_output.out','w')

for t in range(1,int(lines.pop(0))+1):

	number_of_levels = int(lines.pop(0))
	levels = []
	for i in range(number_of_levels):
		levels.append(map(int,lines.pop(0).split()))

	levels.sort(key = lambda x:-x[1])

	number_of_stars = 0
	number_of_plays = 0

	still_looking =True
	part_to_check = 2

	completed_levels = [[],[]]

	while still_looking:
		for index, level in enumerate(levels):
			if number_of_stars >= level[part_to_check-1] and not index in completed_levels[part_to_check-1]:
				number_of_plays += 1
				number_of_stars += part_to_check
				if index in completed_levels[0]:
					number_of_stars -= 1
				for i in range(part_to_check):
					if not index in completed_levels[i]:
						completed_levels[i].append(index)
				part_to_check = 2
				break
		else:
			if part_to_check==2:
				part_to_check = 1
			else:
				break

	if not sorted(completed_levels[1]) == range(number_of_levels):
		number_of_plays = "Too Bad"


	output.write("Case #%i: %s\n"%(t, number_of_plays ))

output.close()