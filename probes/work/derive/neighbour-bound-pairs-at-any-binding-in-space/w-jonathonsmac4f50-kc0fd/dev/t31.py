import sympy as sp, itertools
I=sp.I
SX=sp.Matrix([[0,1],[1,0]]);SY=sp.Matrix([[0,-I],[I,0]]);SZ=sp.Matrix([[1,0],[0,-1]]);I2=sp.eye(2)
PA=(SX,SY,SZ)
kr=sp.kronecker_product
def hplus(a): return (kr(PA[a],I2)-kr(I2,PA[a]))/(2*I)
def hminus(a): return -hplus(a)
# spin +-1 along axis a: joint eigenvectors of sigma_a x 1 and 1 x sigma_a with equal eigenvalue
def pm_states(a):
    P=PA[a]
    (v1,v2)=[ (vec) for val,mult,vecs in P.eigenvects() for vec in vecs]
    ev=[val for val,mult,vecs in P.eigenvects()]
    # eigenvectors of sigma_a
    vs=[]
    for val,mult,vecs in P.eigenvects():
        v=vecs[0]; vs.append(sp.simplify(v/ sp.sqrt((v.H*v)[0])))
    return [kr(v,v) for v in vs]   # |++>, |-->
bonds=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
axis_of={b:[i for i in range(3) if b[i]!=0][0] for b in bonds}
# unknown amplitudes: 12
syms=sp.symbols('c0:12')
psi={}
for i,b in enumerate(bonds):
    st=pm_states(axis_of[b])
    psi[b]=syms[2*i]*st[0]+syms[2*i+1]*st[1]
def Hpsi(r):
    tot=sp.zeros(4,1)
    for a in range(3):
        e=[0,0,0]; e[a]=1
        rp=tuple(r[i]+e[i] for i in range(3)); rm=tuple(r[i]-e[i] for i in range(3))
        if rp in psi: tot+=hplus(a)*psi[rp]
        if rm in psi: tot+=hminus(a)*psi[rm]
    return tot
pos=set()
for b in bonds:
    for a in range(3):
        for s in (1,-1):
            r=list(b); r[a]+=s; pos.add(tuple(r))
pos.discard((0,0,0))
eqs=[]
for r in sorted(pos):
    v=Hpsi(r)
    eqs+= [sp.simplify(x) for x in v]
eqs=[e for e in eqs if e!=0]
A,_=sp.linear_eq_to_matrix(eqs,syms)
ns=A.nullspace()
print('nullspace dim (both exchange sectors, all 12 amplitudes):',len(ns))
# exchange: phi(-r)=eps*SWAP phi(r)
SW=sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
def ex_eps(v):
    sub={s:v[k] for k,s in enumerate(syms)}
    out=None
    # compare psi(-r) with SWAP psi(r)
    res=[]
    for b in bonds:
        nb=tuple(-x for x in b)
        lhs=psi[nb].subs(sub); rhs=SW*psi[b].subs(sub)
        # find eps with lhs=eps*rhs
        for eps in (1,-1):
            if sp.simplify(lhs-eps*rhs)==sp.zeros(4,1): res.append(eps)
    return res
for v in ns:
    print([sp.nsimplify(x) for x in v.T], ex_eps(v)[:3])
