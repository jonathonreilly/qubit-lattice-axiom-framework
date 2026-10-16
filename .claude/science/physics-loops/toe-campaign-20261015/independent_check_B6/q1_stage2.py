# Stage 2: after U==1 on planes k_j in {0,pi}, impose (real argument) d f/dk3 = 0 on planes k3=0,pi
# (1-f>=0 attains its minimum 0 there), then solve f^2+|g|^2=1 exactly.
import sympy as sp, pickle, itertools
from polysys import *
from exact_setup import rotations
free,W=pickle.load(open('q1_after_planes.pkl','rb'))
eqs=[]
for p3 in (0,1):
    P={}
    for n,v in W.items():
        s=(-1)**(p3*n[2]%2); key=(n[0],n[1])
        P[key]=P.get(key,0)+s*n[2]*v[0]
    for key,e in P.items():
        re,im=reim(sp.expand(e))
        for x in (re,im):
            if x!=0: eqs.append(x)
sol=sp.linsolve(eqs,free); sol=list(sol)[0]
free2=sorted(set().union(*[s.free_symbols for s in sol]),key=str)
sub=dict(zip(free,sol))
W2={n:[sp.expand(e.subs(sub)) for e in v] for n,v in W.items()}
W2={n:v for n,v in W2.items() if any(x!=0 for x in v)}
print('free after derivative constraints:',len(free2),free2)
pickle.dump((free2,W2),open('q1_stage2.pkl','wb'))
# equations only at O-orbit representatives
G=[sp.Matrix(R) for R in rotations()]
def canon(s):
    v=sp.Matrix(s); return max(tuple(R*v) for R in G)
ue_all={}
P={}
items=list(W2.items())
for n,v in items:
    for m,w in items:
        s=tuple(a+b for a,b in zip(n,m))
        if canon(s)!=s: continue
        P[s]=P.get(s,0)+sum(v[k]*w[k] for k in range(4))
ue=[]
for s,e in P.items():
    if s==(0,0,0): e=e-1
    re,im=reim(e)
    for x in (re,im):
        if x!=0: ue.append(x)
ue=list(set(ue))
print('eqs',len(ue))
s='LIB "primdec.lib";\noption(redSB);\nring r=0,(%s),dp;\nideal I=%s;\nint t=timer; ideal J=std(I); "time",timer-t; "dim",dim(J); "vdim",vdim(J); J;\n'%(','.join(map(str,free2)),',\n'.join(to_sing(e) for e in ue))
s+='ideal R=radical(J); "radical:"; std(R);\nquit;\n'
open('q1_stage2.sing','w').write(s)
