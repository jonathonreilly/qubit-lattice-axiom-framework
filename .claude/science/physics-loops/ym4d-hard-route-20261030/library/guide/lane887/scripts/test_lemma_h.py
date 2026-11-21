# Refutation test (GUIDE-level; proves nothing) of Lemma G / Lemma H / Corollary TOP+ counting.
# Index units: a level-j box has index x in (Z/M_j)^3, M_j = 4*10^(J-j); it lies inside the level-(j+1) box X
# iff (x_i - 10 X_i) mod M_j is in [0,18] for all i. bad_(j+1)(X): two distinct same-class bad_j boxes inside X,
# local offsets differing by at most 8 in each coordinate. Lemma H (level j): a connected family F of bad_0 boxes
# whose union lies in no box with 9*10^(j-1) g sites per side has every member inside a bad_j box.
import random, sys, itertools, time
def inside_parents(x, M, Mp):
    # all parent indices X (mod Mp) with (x_i - 10 X_i) mod M in [0,18]
    per=[]
    for xi in x:
        c=[]
        for X in ((xi//10)%Mp, (xi//10-1)%Mp):
            if (xi-10*X)%M<=18: c.append(X)
        per.append(c)
    return list(itertools.product(*per))
def next_level(bad, M):
    Mp=M//10
    out=set()
    offs=[o for o in range(-8,9,2)]
    for x in bad:
        for d in itertools.product(offs,repeat=3):
            if d==(0,0,0): continue
            y=tuple((x[i]+d[i])%M for i in range(3))
            if y in bad:
                for X in inside_parents(x,M,Mp):
                    ok=True
                    for i in range(3):
                        a=(x[i]-10*X[i])%M; b=(y[i]-10*X[i])%M
                        if b>18 or abs(a-b)>8: ok=False;break
                    if ok: out.add(X)
    return out
def components(S,M):
    S=set(S); comps=[]
    nb=[d for d in itertools.product((-1,0,1),repeat=3) if d!=(0,0,0)]
    while S:
        s=S.pop(); comp=[s]; st=[s]
        while st:
            u=st.pop()
            for d in nb:
                v=tuple((u[i]+d[i])%M for i in range(3))
                if v in S: S.remove(v); comp.append(v); st.append(v)
        comps.append(comp)
    return comps
def span_values(vals,M):
    # number of index values in the minimal cyclic interval covering vals
    v=sorted(set(vals))
    if len(v)==1: return 1
    gaps=[(v[(k+1)%len(v)]-v[k])%M for k in range(len(v))]
    return M-max(gaps)+1
def in_some(x,level,badj,M0):
    # is level-0 index x inside some bad level-`level` box?
    Mj=M0//(10**level); w=10**level
    per=[]
    for xi in x:
        c=[]
        for X in ((xi//w)%Mj, (xi//w-1)%Mj):
            if (xi-w*X)%M0<=2*w-2: c.append(X)
        per.append(c)
    return any(X in badj for X in itertools.product(*per))
def snake(M,n,start,adversarial):
    pts=[]; x=list(start)
    for k in range(n):
        pts.append(tuple(c%M for c in x))
        if adversarial:
            x[0]+=1
            if k%4==1: x[1]+=1
            if k%4==3: x[2]+=1
        else:
            d=random.choice([d for d in itertools.product((-1,0,1),repeat=3) if d!=(0,0,0)])
            # biased walk so it travels
            x=[x[0]+ (1 if random.random()<0.7 else d[0]), x[1]+d[1], x[2]+d[2]]
    return pts
def trial(J,seed):
    random.seed(seed)
    M0=4*10**J
    bad=set()
    kind=random.choice(["adv","walk","noise","advwrap"])
    if kind in("adv","advwrap"):
        n = M0 if kind=="advwrap" else random.randint(5, 3*10**J)
        bad|=set(snake(M0,n,[random.randrange(M0) for _ in range(3)],True))
    if kind=="walk":
        bad|=set(snake(M0,random.randint(5,3*10**J),[random.randrange(M0) for _ in range(3)],False))
    for _ in range(random.randint(0,300)):
        bad.add(tuple(random.randrange(M0) for _ in range(3)))
    levels=[bad]; M=M0
    for j in range(J):
        levels.append(next_level(levels[-1],M)); M//=10
    viol=0; checked=0
    for comp in components(bad,M0):
        spans=[span_values([p[i] for p in comp],M0) for i in range(3)]
        for j in range(1,J+1):
            if max(spans)+1>9*10**(j-1):       # union lies in no box with 9 g_(j-1) sites per side
                checked+=1
                for p in comp:
                    if not in_some(p,j,levels[j],M0): viol+=1
        if len(comp)<=8 and max(spans)+1>9: viol+=10**6   # Lemma G(b): n<=8 boxes fit in 9 g sites per side
    return kind,len(bad),[len(l) for l in levels],checked,viol
t=time.time(); tot=0; ch=0
for J,ntr in ((1,300),(2,40)):
    for s in range(ntr):
        kind,nb,lv,checked,viol=trial(J,1000*J+s)
        tot+=viol; ch+=checked
        if viol: print("VIOLATION",J,s,kind,nb,lv,checked,viol)
    print("J =",J,"trials",ntr,"done; cumulative families checked",ch,"violations",tot,"time %.1fs"%(time.time()-t))
