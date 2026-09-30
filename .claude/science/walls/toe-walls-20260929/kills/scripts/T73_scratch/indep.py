# independent re-implementation: frozenset-based RSA, MIS enumeration by backtracking
import math, itertools
from fractions import Fraction
def grid(L,d):
    S=list(itertools.product(range(L),repeat=d)); nb={s:[] for s in S}
    for s in S:
        for k in range(d):
            for dv in(-1,1):
                t=list(s);t[k]+=dv;t=tuple(t)
                if t in nb: nb[s].append(t)
    return S,nb
def mis(S,nb):
    S=list(S);out=[]
    def rec(i,chosen,blocked):
        if i==len(S):
            # maximal iff every unchosen is blocked
            if all((s in chosen) or (s in blocked) for s in S): out.append(frozenset(chosen))
            return
        s=S[i]
        if s not in blocked:
            rec(i+1,chosen|{s},blocked|set(nb[s]))
        # skip s: must be blocked eventually
        rec(i+1,chosen,blocked)
    rec(0,frozenset(),frozenset())
    return out
def rsa_exact(S,nb):
    # exact Fractions, memo on recorded set -> probability of reaching; forward DP by layers
    layer={frozenset():Fraction(1)}; frozen={}
    while layer:
        nxt={}
        for st,p in layer.items():
            bl=set(st)
            for s in st: bl|=set(nb[s])
            el=[s for s in S if s not in bl]
            if not el: frozen[st]=frozen.get(st,0)+p;continue
            q=p/len(el)
            for s in el:
                k=st|{s}; nxt[k]=nxt.get(k,0)+q
        layer=nxt
    return frozen
for d,Ls in ((1,range(2,13)),(2,range(2,6))):
    for L in Ls:
        S,nb=grid(L,d)
        M=mis(S,nb); fr=rsa_exact(S,nb)
        assert set(M)==set(fr), (d,L)
        assert sum(fr.values())==1
        S1=-sum(float(p)*math.log(float(p)) for p in fr.values())
        print(d,L,len(M),round(math.log(len(M)),4),round(S1,4),round(S1/math.log(len(M)),4) if len(M)>1 else 1)
