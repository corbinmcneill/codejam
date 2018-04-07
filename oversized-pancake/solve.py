infile = open("input.txt", 'r');

def flip(x):
    return (x+1)%2

def solve(casenum, pstring, K):

    flips = 0
    pancakes = []
    for i in pstring:
        if i=='+':
            pancakes.append(1)
        else:
            pancakes.append(0)
    for p in range(len(pancakes)-K+1):
        if pancakes[p]==0:
            flips+=1
            for i in range(p, p+K):
                pancakes[i] = flip(pancakes[i])
    for p in pancakes[len(pancakes)-K+1:]:
        if p==0:
            flips="IMPOSSIBLE"
    flips = str(flips)

    print "Case #%d: %s"%(casenum, flips)

T = int(infile.readline());
for t in range(1, T+1):
    pancake, K = infile.readline().split(' ')
    K = int(K)
    solve(t, pancake, K);
