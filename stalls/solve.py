infile = open("input.txt", 'r');

def solve(casenum, N, K):
    #print "N: %d    \tK: %d"%(N,K)
    h=1 #tree height
    n=N #unmatched stalls
    k=K #unmatched people

    #place people until we get to the final round
    while k > 2**(h-1):
        #print "%d people left : %d openings : %d clusters : advance"%(k,n,2**(h-1))
        numMatched = 2**(h - 1)
        k-=numMatched
        n-=numMatched
        h+=1

    #print "%d people left : %d openings : %d clusters : done"%(k,n,2**(h-1))
    numClusters = 2**(h-1)
    smallClusterSize = n / numClusters
    largeClusterSize = smallClusterSize + 1
    numLargeClusters = n - (numClusters*smallClusterSize)
    
    #print "small/large size: %d %d"%(smallClusterSize, largeClusterSize)
    #print "small/large number: %d %d"%(numClusters - numLargeClusters, numLargeClusters)

    if (k <= numLargeClusters):
        maximum = largeClusterSize / 2
        minimum = (largeClusterSize - 1) / 2
    else:
        maximum = smallClusterSize / 2
        minimum = (smallClusterSize - 1) / 2

    print "Case #%d: %d %d"%(casenum, maximum, minimum)
    #print "--------------------------------------------"

def solve2(casenum, N, K):
    options = [N]
    for i in range(K-1):
        pick = options.pop(options.index(max(options)))
        options.append(pick/2)
        options.append((pick-1)/2)
    pick = options.pop(options.index(max(options)))
    print "Case #%d: %d %d"%(casenum, pick/2, (pick-1)/2)

T = int(infile.readline());
for t in range(1, T+1):
    N, K = map(int, infile.readline().split())
    solve(t,N,K);
    #solve2(t,N,K);
    #print
