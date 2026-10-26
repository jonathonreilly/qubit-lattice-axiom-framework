import itertools, collections, sys, time
E=[(1,0),(-1,0),(0,1),(0,-1)]
W=int(sys.argv[1]); N=int(sys.argv[2])
sites=[(x,y) for x in range(W) for y in range(W)]
def cr(p,c): return p[0]*c[1]-p[1]*c[0]
t0=time.time()
tot=conf=unres=0; ex=[]
for occ in itertools.combinations(sites,N):
    classes=collections.defaultdict(list)
    for ks in itertools.product(range(4),repeat=N):
        P=(sum(E[k][0] for k in ks),sum(E[k][1] for k in ks)); L=sum(cr(p,E[k]) for p,k in zip(occ,ks))
        tg=len({(p[0]+E[k][0],p[1]+E[k][1]) for p,k in zip(occ,ks)})==N
        classes[(P,L)].append((ks,tg))
    for key,mem in classes.items():
        anyfree=any(t for _,t in mem)
        for ks,t in mem:
            tot+=1
            if not t:
                conf+=1
                if not anyfree:
                    unres+=1
                    if len(ex)<3: ex.append((occ,ks))
print('W',W,'N',N,'configs',tot,'conflicting',conf,'unresolvable in own class',unres,'time',round(time.time()-t0,1))
for e in ex: print(' ex',e)
