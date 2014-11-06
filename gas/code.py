# drummer2322
# corbin.mc96@gmail.com
# GCJ 2012 1C B
# 9 Jun 2014

# UNFINISHED -- NEEDS TO BE CLEANED

from sys import argv

if len(argv) > 1:
	type_of_case = argv[1]+'_'
else:
	type_of_case = ''

lines = [line.strip() for line in open(type_of_case+'input.in')];
output = open(type_of_case+'output.out','w')

for t in range(1,int(lines.pop(0))+1):

	print t;
	output.write("Case #%i:\n"%(t))

	house_location, number_of_points, number_of_accerations = lines.pop(0).split()
	house_location = float(house_location)
	number_of_points = int(number_of_points)
	number_of_accerations = int(number_of_accerations)

	points=[]
	for i in range(number_of_points):
		point = map(float, lines.pop(0).split())
		points.append(point)

	print points
	accerations=map(float, lines.pop(0).split())

	for car_acceration in accerations:
		previous_time = 0.;
		car_position = 0.;
		car_velocity = 0.;
		first = True;
		for point in points[1:]:
			#print "At time", previous_time, "position is", car_position, "velocity is", car_velocity
			endtime = point[0]
			endpoint = point[1]
			if endpoint > house_location:
				if first:
					previous_time = 2 * endpoint / car_acceration
					car_position = house_location
					break
				endtime = (endtime-previous_time)/(endpoint-car_position) * (house_location-car_position) + previous_time
				endpoint = house_location
			time_difference = endtime-previous_time
			freefall_position = car_position + car_velocity*time_difference + 0.5*car_acceration*time_difference**2
			if freefall_position > endpoint:
				car_velocity = float((endpoint-car_position)/(time_difference))
				#if first:
					#car_velocity = (2 * endpoint / car_acceration) ** 0.5 * car_acceration
				car_position = float(endpoint)
			else:
				car_velocity=car_velocity + (car_acceration*time_difference)
				car_position=freefall_position
			previous_time = float(endtime)
			first = False
			if endpoint == house_location:
				break
			
		additional_time = ((car_velocity**2 + 2*car_acceration*(house_location-car_position))**(.5) - car_velocity) / car_acceration
		print "previous_time:", previous_time
		print "additional_time:", additional_time
		total_time = previous_time + additional_time
		print "total_time:", total_time

		output.write(str(total_time)+"\n");
	


output.close()
