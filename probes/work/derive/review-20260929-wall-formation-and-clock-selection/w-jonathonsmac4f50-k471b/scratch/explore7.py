import itertools, collections
E=[(1,0),(-1,0),(0,1),(0,-1)]
W=3
sites=[(x,y) for x in range(W) for y in range(W)]
N=3
shown=0
for occ in itertools.combinations(sites,N):
    info=collections.defaultdict(list)
    for ks in itertools.product(range(4),repeat=N):
        P=(sum(E[k][0] for k in ks),sum(E[k][1] for k in ks))
        tg=len({((p[0]+E[k][0])%W,(p[1]+E[k][1])%W) for p,k in zip(occ,ks)})==N
        info[P].append((ks,tg))
    for P,mem in info.items():
        if not any(t for _,t in mem):
            print('occ',occ,'P',P,'class size',len(mem),'members',[m[0] for m in mem][:6]); shown+=1
    if shown>=4: break
