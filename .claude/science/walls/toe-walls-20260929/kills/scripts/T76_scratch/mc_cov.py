# random sequential formation (uniform over eligible sites) for a covariant 2D rule; Shannon entropy of final state
import random, sys, math, collections
from covariant2d import cls, NAMES
def run(L,R,nsamp,seed=1):
    rnd=random.Random(seed); Rset=set(R)
    DIRS=[(-1,0),(0,1),(1,0),(0,-1)]
    nb=[[ (r+a)*L+(c+b) if (0<=r+a<L and 0<=c+b<L) else -1 for a,b in DIRS] for r in range(L) for c in range(L)]
    cnt=collections.Counter()
    for _ in range(nsamp):
        rec=[0]*(L*L)
        def elig(v): return rec[v]==0 and cls([1 if (u!=-1 and rec[u]) else 0 for u in nb[v]]) in Rset
        el=[v for v in range(L*L) if elig(v)]; pos={v:i for i,v in enumerate(el)}
        def add(v): pos[v]=len(el); el.append(v)
        def rem(v):
            i=pos.pop(v); last=el.pop()
            if i<len(el): el[i]=last; pos[last]=i
        while el:
            v=el[rnd.randrange(len(el))]
            rec[v]=1; rem(v)
            for u in nb[v]:
                if u==-1: continue
                e=elig(u)
                if e and u not in pos: add(u)
                elif (not e) and u in pos: rem(u)
        cnt[tuple(rec)]+=1
    n=nsamp
    S=-sum(c/n*math.log(c/n) for c in cnt.values())
    return len(cnt),S+(len(cnt)-1)/(2*n)
if __name__=="__main__":
    R=[NAMES.index(x) for x in sys.argv[1].split(",")]
    for L in range(int(sys.argv[2]),int(sys.argv[3])+1,int(sys.argv[4])):
        d,S=run(L,R,int(sys.argv[5]))
        print(sys.argv[1],f"L={L} distinct={d} S_MM={S:.3f} S/L={S/L:.3f} S/L^2={S/L**2:.4f}",flush=True)
