# Process entropy of random sequential formation for rule E (A={0,2,3,4}) on LxL sealed box, outside unrecorded:
# at each step choose uniformly among eligible empty sites (k in A). Frozen when none. Estimate Shannon entropy of the final state.
import random, sys, math, collections
def run(L, nsamp, seed=1):
    rnd=random.Random(seed)
    nb=[[ (r+a)*L+(c+b) for a,b in((1,0),(-1,0),(0,1),(0,-1)) if 0<=r+a<L and 0<=c+b<L] for r in range(L) for c in range(L)]
    A={0,2,3,4}
    cnt=collections.Counter()
    for _ in range(nsamp):
        rec=[0]*(L*L); k=[0]*(L*L)
        elig=set(i for i in range(L*L) if k[i] in A)
        el=list(elig); pos={v:i for i,v in enumerate(el)}
        def add(v):
            pos[v]=len(el); el.append(v)
        def rem(v):
            i=pos.pop(v); last=el.pop()
            if i<len(el): el[i]=last; pos[last]=i
        el=[i for i in range(L*L)]; pos={v:i for i,v in enumerate(el)}
        while el:
            v=el[rnd.randrange(len(el))]
            rec[v]=1; rem(v)
            for u in nb[v]:
                if rec[u]: continue
                before = k[u] in A
                k[u]+=1
                after = k[u] in A
                if before and not after: rem(u)
                elif after and not before: add(u)
        cnt[tuple(rec)]+=1
    n=nsamp
    S=-sum(c/n*math.log(c/n) for c in cnt.values())
    # Miller-Madow bias correction
    S_mm=S+(len(cnt)-1)/(2*n)
    return len(cnt),S,S_mm
if __name__=="__main__":
    for L in range(3,int(sys.argv[1])+1):
        ns=int(sys.argv[2])
        d,S,Smm=run(L,ns)
        print(f"L={L} distinct={d} S1={S:.3f} S_MM={Smm:.3f} S/L={Smm/L:.3f} S/L^2={Smm/L**2:.4f}",flush=True)
