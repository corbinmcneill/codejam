# dolphinigle
# GCJ 2013 1B
# 4 May 2013

lines = [line.strip() for line in open('input.in')];

output = open('output.out','w')


for t in range(1,int(lines.pop(0))+1):

  my_mote, n = map(int, lines.pop(0).split())

  motes = sorted(map(int, lines.pop(0).split()))

  if my_mote == 1:

    output.write("Case #%i: %i\n"%(t,n))

    continue

  best_answer = n

  my_answer = 0
  for index, i in enumerate(motes):

    if i < my_mote:

      my_mote += i

      continue

    # maybe stop here?

    best_answer = min([best_answer, my_answer + n - index])

    while my_mote <= i:

      my_mote += my_mote - 1

      my_answer += 1

    my_mote += i

  best_answer = min([best_answer, my_answer])

  output.write("Case #%i: %i\n"%(t,best_answer))
  
output.close()