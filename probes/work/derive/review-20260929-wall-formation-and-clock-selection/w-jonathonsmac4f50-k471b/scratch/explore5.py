import itertools, collections, sys, time
E=[(1,0),(-1,0),(0,1),(0,-1)]
W=int(sys.argv[1]); Nmax=int(sys.argv[2])
sites=[(x,y) for x in range(W) for y in range(W)]
def cr(p,c): return p[0]*c[1]-p[1]*c[0]
def d2(p,q): return (p[0]-q[0])**2+(p[1]-q[1])**2
R2s=[1,2,4,5,8]
for N in range(2,Nmax+1):
    t0=time.time()
    tot=0; bad={R:0 for R in R2s}; badcls=0
    for occ in itertools.combinations(sites,N):
        cfgs=list(itertools.product(range(4),repeat=N))
        idx={c:i for i,c in enumerate(cfgs)}
        free=[len({(p[0]+E[k][0],p[1]+E[k][1]) for p,k in zip(occ,ks)})==N for ks in cfgs]
        # class resolvable
        cl=collections.defaultdict(bool)
        key=[]
        for ks,f in zip(cfgs,free):
            P=(sum(E[k][0] for k in ks),sum(E[k][1] for k in ks)); L=sum(cr(p,E[k]) for p,k in zip(occ,ks))
            key.append((P,L)); cl[(P,L)] |= f
        for R in R2s:
            parent=list(range(len(cfgs)))
            def find(a):
                while parent[a]!=a:
                    parent[a]=parent[parent[a]]; a=parent[a]
                return a
            pairs=[(i,j) for i in range(N) for j in range(i+1,N) if d2(occ[i],occ[j])<=R]
            for ci,ks in enumerate(cfgs):
                for i,j in pairs:
                    a,b=ks[i],ks[j]
                    Pab=(E[a][0]+E[b][0],E[a][1]+E[b][1]); Lab=cr(occ[i],E[a])+cr(occ[j],E[b])
                    for u in range(4):
                        for v in range(4):
                            if (E[u][0]+E[v][0],E[u][1]+E[v][1])==Pab and cr(occ[i],E[u])+cr(occ[j],E[v])==Lab and (u,v)!=(a,b):
                                nk=list(ks); nk[i]=u; nk[j]=v
                                ra,rb=find(ci),find(idx[tuple(nk)])
                                if ra!=rb: parent[ra]=rb
            comp_free=collections.defaultdict(bool)
            for ci,f in enumerate(free): comp_free[find(ci)] |= f
            for ci in range(len(cfgs)):
                if not comp_free[find(ci)]: bad[R]+=1
        tot+=len(cfgs)
    print('W',W,'N',N,'configs',tot,'unresolved by pair-closure at R2:',bad,'t',round(time.time()-t0,1),flush=True)
