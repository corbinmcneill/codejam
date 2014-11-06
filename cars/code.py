# drummer2322
# GCJ 2013 1A
# 24 Apr 2014

# CODE NOT FINISHED

from sys import argv
from itertools import combinations

if len(argv) > 1:
	type_of_case = argv[1]+'_'
else:
	type_of_case = ''

lines = [line.strip() for line in open(type_of_case+'input.in')];
output = open(type_of_case+'output.out','w')

class Car():
	def __init__(self, velocity, start_location):
		self.start_location = float(start_location)
		self.velocity = float(velocity)
	
	def location_at_time(self, time):
		car_location = self.start_location + self.velocity*float(time)
		return car_location

def overlap_exists(locations):
 	if max(locations) - min(locations) < 5.0:
		return True
	return False

def find_overlap_time(car1, car2):
	if car1.velocity == car2.velocity:
		if abs(car1.start_location - car2.start_location) < 5:
			return [-float("inf"), float("inf")]
		else:
			return [0,0]
	return sorted([(car1.start_location - car2.start_location + 5)/(car2.velocity - car1.velocity), (car1.start_location - car2.start_location - 5)/(car2.velocity - car1.velocity)])

def calculate_overlap(a,b):
	allpoints = sorted(a+b)
	if min(a)>max(b) or min(b)>max(a):
		return [0,0]
	return [allpoints[1],allpoints[2]]


for t in range(1,int(lines.pop(0))+1):
	print t

	number_of_cars = int(lines.pop(0))

	cars = []
	for i in range(number_of_cars):
		car_info = lines.pop(0).split()
		cars.append( Car(car_info[1],car_info[2]) )

	first_incedent = float("inf")

	for car_set in combinations(cars,3):

		car1, car2, car3 = sorted(car_set, key=lambda x:x.velocity)

		if car1.velocity == car3.velocity:
			continue

		first_overlap = find_overlap_time(car1, car2)
		second_overlap = find_overlap_time(car1,car3)
		third_overlap = find_overlap_time(car2, car3)
		total_overlap = calculate_overlap(third_overlap, calculate_overlap(first_overlap, second_overlap))
		print first_overlap, second_overlap, third_overlap, total_overlap
		if not total_overlap == [0,0]:
			first_incedent=min(first_incedent,min(total_overlap))


		






	if first_incedent == float("inf"):
		first_incedent = "Possible"


	output.write("Case #%i: %s\n"%(t, first_incedent ))

output.close()