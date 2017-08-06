infile = open("input.txt", 'r');

def isTidy(N):
    n = str(N)[::-1]
    for i in range(len(n)-1)[::-1]:
        if n[i]<n[i+1]:
            return i
    return -1

def solve(casenum, N):
    while isTidy(N) != -1:
        num = isTidy(N)
        N/=int(10**(num+1))
        N*=int(10**(num+1))
        N-=1
    print "Case #%d: %d"%(casenum,N)


T = int(infile.readline());
for t in range(1, T+1):
    solve(t, int(infile.readline()));
