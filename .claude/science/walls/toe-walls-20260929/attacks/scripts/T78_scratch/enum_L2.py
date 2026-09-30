"""Exact enumeration on L=2: validate ice count 9600, flip components, mean N_f (expect 8 on 864-comp, 188/29 on 464 unit-flux comps)."""
import numpy as np, itertools, collections
from fractions import Fraction
L=2
idx={}
k=0
for a in range(3):
    for x in range(L):
        for y in range(L):
            for z in range(L):
                idx[(a,x,y,z)]=k;k+=1
n=k
states=np.arange(2**n,dtype=np.uint32)
def bit(state,i): return ((state>>np.uint32(i))&np.uint32(1)).astype(np.int8)  # 1 => +1 arrow
ok=np.ones(len(states),dtype=bool)
for x in range(L):
  for y in range(L):
    for z in range(L):
      out=bit(states,idx[(0,x,y,z)])+bit(states,idx[(1,x,y,z)])+bit(states,idx[(2,x,y,z)])
      out=out+(1-bit(states,idx[(0,(x-1)%L,y,z)]))+(1-bit(states,idx[(1,x,(y-1)%L,z)]))+(1-bit(states,idx[(2,x,y,(z-1)%L)]))
      ok&=(out==3)
ice=states[ok]
print("ice states",len(ice))
def plaqs():
    P=[]
    for x in range(L):
      for y in range(L):
        for z in range(L):
          for a,b in ((0,1),(1,2),(0,2)):
            v=(x,y,z)
            def sh(v,a):
                w=list(v); w[a]=(w[a]+1)%L; return tuple(w)
            va=sh(v,a); vb=sh(v,b)
            P.append((idx[(a,)+v],idx[(b,)+va],idx[(a,)+vb],idx[(b,)+v]))
    return P
P=plaqs()
def s_of(st,i): return 1 if (st>>i)&1 else -1
def flippable(st,p):
    s1,s2,s3,s4=[s_of(st,i) for i in p]
    return s1==s2 and s1==-s3 and s1==-s4
def flipmask(p): return sum(1<<i for i in p)
iceset=set(int(s) for s in ice)
Nf={int(s):sum(flippable(int(s),p) for p in P) for s in ice}
# components
seen={}
comps=[]
for s0 in iceset:
    if s0 in seen: continue
    cid=len(comps); stack=[s0]; seen[s0]=cid; mem=[s0]
    while stack:
        s=stack.pop()
        for p in P:
            if flippable(s,p):
                t=s^flipmask(p)
                assert t in iceset
                if t not in seen:
                    seen[t]=cid; stack.append(t); mem.append(t)
    comps.append(mem)
print("components",len(comps))
def flux(st):
    return tuple(sum(s_of(st,idx[(a,)+ ((0,u,w) if a==0 else (u,0,w) if a==1 else (u,w,0))]) for u in range(L) for w in range(L)) for a in range(3))
res=collections.defaultdict(list)
for c in comps:
    m=Fraction(sum(Nf[s] for s in c),len(c))
    res[(len(c),m,flux(c[0]))].append(1)
big=sorted(res.items(),key=lambda kv:-kv[0][0])[:8]
for (sz,m,fl),v in big: print(sz,m,float(m),fl,len(v))
# whole-sector means
sect=collections.defaultdict(list)
for s in iceset: sect[flux(s)].append(Nf[s])
for fl in [(0,0,0),(2,0,0)]:
    v=sect[fl]; print("sector",fl,len(v),Fraction(sum(v),len(v)),sum(v)/len(v))
