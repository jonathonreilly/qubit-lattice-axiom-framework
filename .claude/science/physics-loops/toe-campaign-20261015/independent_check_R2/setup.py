# Exact parametrization of O-covariant SU(2)-normalized walks: V = u0 + i u.sigma
# u0 O-invariant, u O-equivariant real trig polys with Fourier support in N={-2..2}^3.
import itertools, sympy as sp, pickle
from sympy import Matrix, I, Rational

# proper rotations of cube
G=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product([1,-1],repeat=3):
        M=sp.zeros(3,3)
        for i in range(3): M[i,p[i]]=s[i]
        if M.det()==1: G.append(M)
assert len(G)==24
N=[tuple(n) for n in itertools.product(range(-2,3),repeat=3)]
def act(g,n): return tuple(int(x) for x in g*Matrix(n))
# orbits
seen=set(); orbits=[]
for n in N:
    if n in seen: continue
    orb=sorted(set(act(g,n) for g in G)); seen|=set(orb); orbits.append(orb)
print("orbits:",len(orbits),[len(o) for o in orbits])

params=[]   # real symbols
c0={}  # mode -> sympy complex expr (u0 coefficient)
cu={}  # mode -> 3-vector of complex expr
for orb in orbits:
    m=orb[-1]  # representative
    H=[g for g in G if act(g,m)==m]
    neg=tuple(-x for x in m)
    assert neg in orb
    g0=[g for g in G if act(g,m)==neg][0]
    # scalar: invariant -> c0_m arbitrary complex with conj(c0_m)=c0_m => real
    t=sp.Symbol('a%d'%len(params),real=True); params.append(t)
    for n in orb: c0[n]=t   # u0 coefficient same along orbit; real
    if m==(0,0,0):
        for n in orb: cu[n]=Matrix([0,0,0])
        continue
    # vector: x+iy in C^3, constraints g(x+iy)=x+iy for g in H ; x-iy = g0(x+iy)
    rows=[]
    for g in H:
        A=sp.zeros(6,6); A[:3,:3]=g-sp.eye(3); A[3:,3:]=g-sp.eye(3); rows.append(A)
    B=sp.zeros(6,6)
    B[:3,:3]=g0-sp.eye(3); B[3:,3:]=g0+sp.eye(3)   # g0 x = x ; g0 y = -y
    rows.append(B)
    A=Matrix.vstack(*rows)
    ns=A.nullspace()
    vec=Matrix([0]*6)
    for b in ns:
        t=sp.Symbol('b%d'%len(params),real=True); params.append(t); vec+=t*b
    um=vec[:3,0]+I*vec[3:,0]
    for n in orb:
        g=[g for g in G if act(g,m)==n][0]
        cu[n]=sp.expand(g*um)
    print(m,len(orb),"vec params",len(ns))
print("nparams",len(params))
pickle.dump(dict(params=params,c0=c0,cu=cu,orbits=orbits),open('param.pkl','wb'))
