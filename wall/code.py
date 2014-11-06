# drummer2322
# GCJ <year> <round>
# <date>

class Tribe():

	def __init__(self, startString):
		self.initial_attack, self.number_of_attacks, self.initial_west, self.initial_east, self.initial_strength, self.delta_days, self.delta_attack_location, self.delta_strength = map(int, startString.split())

	def attacks_on_day(self, day):
		return (day-self.initial_attack)%self.delta_days==0 and (day-self.initial_attack)/self.delta_days < self.number_of_attacks and day>=self.initial_attack

	def last_attack(self) :
		return self.initial_attack + (self.delta_days*self.number_of_attacks)

	def attack_locations_on_day(self, day):
		attack_number = (day-self.initial_attack)/self.delta_days
		east = self.initial_east+attack_number*self.delta_attack_location
		west = self.initial_west+attack_number*self.delta_attack_location
		return range(west,east)

	def strength_on_day(self, day):
		attack_number = (day-self.initial_attack)/self.delta_days
		return attack_number*self.delta_strength+self.initial_strength



def merge_walls(wall1, wall2):
	result = wall1
	for wall_segment in wall2.keys():
		if not wall_segment in result:
			result[wall_segment] = wall2[wall_segment]
		result[wall_segment] = max(wall1[wall_segment], wall2[wall_segment]);
	return result



lines = [line.strip() for line in open('large_input.in')];
output = open('large_output.out','w')

for t in range(1,int(lines.pop(0))+1):

	print t
	
	successful_attacks= 0

	number_of_tribes = int(lines.pop(0))
	tribes=[]
	for i in range(number_of_tribes):
		tribes.append(Tribe(lines.pop(0)))

	wall={}

	first_attacks = []
	last_attacks = []
	for tribe in tribes:
		first_attacks.append(tribe.initial_attack)
		last_attacks.append(tribe.last_attack())
	first_attack = min(first_attacks);
	last_attack = max(last_attacks);

	for day in range(first_attack,last_attack+1):
		new_wall={}
		for tribe in tribes:
			if tribe.attacks_on_day(day):
				attack_is_successful = False;
				for wall_segment in tribe.attack_locations_on_day(day):
					if not wall_segment in wall or wall[wall_segment]<tribe.strength_on_day(day):
						attack_is_successful = True
						break
				if attack_is_successful:
					successful_attacks+=1
					temp_wall={}
					for wall_segment in tribe.attack_locations_on_day(day):
						temp_wall[wall_segment] = tribe.strength_on_day(day)
				new_wall=merge_walls(new_wall,temp_wall)

		wall = merge_walls(wall, new_wall)

	output.write("Case #%i: %s\n"%(t, successful_attacks))

output.close()
