# 3D Q1 (range 3): impose U == 1 on planes k3=0 and k3=pi (consequence of the 2D classification), then solve exactly.
import sympy as sp, pickle, time
from polysys import *
rb=pickle.load(open('q1_real_r3.pkl','rb')); nb=len(rb)
X=sp.symbols('x1:%d'%(nb+1))
W=combine(rb,X)
eqs=[]
for p3 in (0,1):
    P={}
    for n,v in W.items():
        s=(-1)**(p3*n[2]%2); key=(n[0],n[1])
        w=P.setdefault(key,[0,0,0,0])
        for c in range(4): w[c]+=s*v[c]
    for key,w in P.items():
        for c in range(4):
            e=sp.expand(w[c]-(1 if (c==0 and key==(0,0)) else 0))
            re,im=reim(e)
            for x in (re,im):
                if x!=0: eqs.append(x)
sol=sp.linsolve(eqs,X); sol=list(sol)[0]
free=sorted(set().union(*[s.free_symbols for s in sol]),key=str)
print('free after plane constraints:',len(free),free)
sub=dict(zip(X,sol))
W2={n:[sp.expand(e.subs(sub)) for e in v] for n,v in W.items()}
W2={n:v for n,v in W2.items() if any(x!=0 for x in v)}
print('support offsets:',sorted(W2)[:5],'... count',len(W2))
pickle.dump((free,W2),open('q1_after_planes.pkl','wb'))
ue=[e for e in unit_eqs(W2) if e!=0]
print('eqs',len(ue))
s='option(redSB);\nring r=0,(%s),dp;\nideal I=%s;\nint t=timer; ideal J=std(I); "time",timer-t; "dim",dim(J); "vdim",vdim(J); J;\n'%(','.join(map(str,free)),',\n'.join(to_sing(e) for e in ue))
s+='ideal R=radical(J); "radical:"; R;\nquit;\n'
s='LIB "primdec.lib";\n'+s
open('q1_after_planes.sing','w').write(s)
