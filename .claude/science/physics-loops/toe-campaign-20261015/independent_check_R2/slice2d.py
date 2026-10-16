# 2D slice problem: V(k1,k2) (= V(k1,k2,0) or V(k1,k2,pi)) covariant under D4 = {R in O : R e3 = +-e3}
import itertools, sympy as sp, pickle, sys
from sympy import Matrix, I
from collections import defaultdict
G=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product([1,-1],repeat=3):
        M=sp.zeros(3,3)
        for i in range(3): M[i,p[i]]=s[i]
        if M.det()==1 and abs(M[2,2])==1: G.append(M)
assert len(G)==8
N=[(a,b,0) for a in range(-2,3) for b in range(-2,3)]
def act(g,n): return tuple(int(x) for x in g*Matrix(n))
seen=set(); orbits=[]
for n in N:
    if n in seen: continue
    orb=sorted(set(act(g,n) for g in G)); seen|=set(orb); orbits.append(orb)
params=[]; c0={}; cu={}
for orb in orbits:
    m=orb[-1]; H=[g for g in G if act(g,m)==m]; neg=tuple(-x for x in m); assert neg in orb
    g0=[g for g in G if act(g,m)==neg][0]
    t=sp.Symbol('p%d'%len(params),real=True); params.append(t)
    for n in orb: c0[n]=t
    rows=[]
    for g in H:
        A=sp.zeros(6,6); A[:3,:3]=g-sp.eye(3); A[3:,3:]=g-sp.eye(3); rows.append(A)
    B=sp.zeros(6,6); B[:3,:3]=g0-sp.eye(3); B[3:,3:]=g0+sp.eye(3); rows.append(B)
    ns=Matrix.vstack(*rows).nullspace(); vec=Matrix([0]*6)
    for b in ns:
        t=sp.Symbol('p%d'%len(params),real=True); params.append(t); vec+=t*b
    um=vec[:3,0]+I*vec[3:,0]
    for n in orb:
        g=[g for g in G if act(g,m)==n][0]; cu[n]=sp.expand(g*um)
print("orbits",[o[-1] for o in orbits],"nparams",len(params))
F=defaultdict(lambda:0)
for n in c0:
    for m in c0:
        s=tuple(a+b for a,b in zip(n,m)); F[s]+=c0[n]*c0[m]+sum(cu[n][j]*cu[m][j] for j in range(3))
F[(0,0,0)]-=1
eqs=set()
for s,v in F.items():
    v=sp.expand(v)
    for e in (sp.re(v),sp.im(v)):
        e=sp.expand(e)
        if e!=0: eqs.add(sp.expand(e/sp.Poly(e,*params).LC()))
eqs=sorted(eqs,key=str)
print("neqs",len(eqs))
pickle.dump(dict(params=params,c0=c0,cu=cu,eqs=eqs,orbits=orbits),open('slice2d.pkl','wb'))
