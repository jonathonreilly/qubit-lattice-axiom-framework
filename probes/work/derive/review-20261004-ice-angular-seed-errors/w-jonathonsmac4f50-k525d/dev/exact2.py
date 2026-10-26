import numpy as np, itertools, time
from fractions import Fraction
t0=time.time()
L=2
sites=[(x,y,z) for x in range(2) for y in range(2) for z in range(2)]
sid={s:n for n,s in enumerate(sites)}
links=[(i,s) for i in range(3) for s in sites]          # 24 links: (axis, tail)
def head(i,s):
    t=list(s); t[i]=(t[i]+1)%2; return tuple(t)
tail_idx=[sid[s] for i,s in links]; head_idx=[sid[head(i,s)] for i,s in links]
inc=[[] for _ in sites]      # per site: (link index, +1 if tail else -1)
for a,(i,s) in enumerate(links):
    inc[sid[s]].append((a,+1)); inc[head_idx[a] ].append((a,-1))
# backtracking: assign link values in order; check a site as soon as all its links are assigned
last=[max(a for a,_ in inc[v]) for v in range(8)]
check_at=[[v for v in range(8) if last[v]==a] for a in range(24)]
cfgs=[]
val=[0]*24
def rec(a):
    if a==24: cfgs.append(tuple(val)); return
    for v in (1,-1):
        val[a]=v; ok=True
        for s in check_at[a]:
            if sum(sg*val[b] for b,sg in inc[s])!=0: ok=False;break
        if ok: rec(a+1)
rec(0)
print(len(cfgs),time.time()-t0)
# exact S_ii(k) at the three L=2 wavevectors of the multiset {0,1,1}: k=(0,pi,pi),(pi,0,pi),(pi,pi,0)
def sgn(k,s): return -1 if sum(k[j]*s[j] for j in range(3))%2 else 1
KS=[(0,1,1),(1,0,1),(1,1,0)]
from collections import defaultdict
Ssum={(i,k):0 for i in range(3) for k in KS}
cons=0
for c in cfgs:
    for k in KS:
        F=[sum(c[i*8+sid[s]]*sgn(k,s) for s in sites) for i in range(3)]
        for i in range(3): Ssum[(i,k)]+=F[i]**2
        # divergence constraint at k: sum_i (1-(-1)^{k_i}) F_i = 2 sum_{i: k_i=1} F_i = 0
        if sum(F[i] for i in range(3) if k[i])!=0: cons+=1
print("constraint violations",cons)
S={key:Fraction(v,8*len(cfgs)) for key,v in Ssum.items()}
for key,v in S.items(): print(key,v)
Kc=Fraction(17,24)
A=sum(S[(i,k)] for k in KS for i in range(3) if k[i]==0)/Fraction(3)
B=sum(S[(i,k)] for k in KS for i in range(3) if k[i]==1)/Fraction(6)
print("A",A,"B",B,"D2",Kc*(2*B-A), float(Kc*(2*B-A)))
