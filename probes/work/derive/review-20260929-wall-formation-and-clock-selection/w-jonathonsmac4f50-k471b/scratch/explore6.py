import itertools, collections, sys
E=[(1,0),(-1,0),(0,1),(0,-1)]
W=int(sys.argv[1])
sites=[(x,y) for x in range(W) for y in range(W)]
V=len(sites)
for N in range(2,V+1):
    tot=unres=0; unresL=0
    for occ in itertools.combinations(sites,N):
        info=collections.defaultdict(list)
        for ks in itertools.product(range(4),repeat=N):
            P=(sum(E[k][0] for k in ks),sum(E[k][1] for k in ks))
            tg=len({((p[0]+E[k][0])%W,(p[1]+E[k][1])%W) for p,k in zip(occ,ks)})==N
            info[P].append(tg)
        for P,mem in info.items():
            ok=any(mem)
            tot+=len(mem)
            if not ok: unres+=len(mem)
    print('torus',W,'N',N,'configs',tot,'unresolvable even with P-only class',unres,flush=True)
