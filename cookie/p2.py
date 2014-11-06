lines = [line.strip() for line in open('input.in')];
output = open('output.out','w')


for case in range(int(lines.pop(0))):
	theinput = lines.pop(0);
	cost, farmyield, goal = map(float, theinput.split());
	stillLooking = True
	currentamount = 0.0;
	rate = 2.0
	time=0.0;
	while stillLooking:
		timetillend = (goal-currentamount)/rate;
		timetillpurchase = (cost-currentamount)/rate;
		timeafterpurchase = goal/(rate+farmyield);

		if (timeafterpurchase+timetillpurchase)<timetillend :
			time=time+timetillpurchase;
			currentamount=currentamount + rate*timetillpurchase;

			currentamount=currentamount-cost
			rate = rate+farmyield;

		else:
			time=time+timetillend;
			stillLooking=False;

	output.write("Case #%s: %s\n"%(case+1,time))

output.close()
