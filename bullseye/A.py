#corbin.mc96@gmail.com
#passed small and large

lines = [line.strip() for line in open('input.in')];
output = open('output.out','w')

for case in range(1,int(lines.pop(0))+1):
    print case

    r, t = map(int,lines.pop(0).split());

    t = int(t)
    first_ring = (r+1)**2 - r**2;

    hi = t
    lo = 0

    while hi>lo:
        middle = int(hi+lo)/2+1
        paint_required = first_ring*middle + 2*middle*(middle-1)
        if paint_required > t:
            hi = middle-1
        else:
            lo = middle

    output.write("Case #%i: %i\n"%(case, hi))

output.close()
