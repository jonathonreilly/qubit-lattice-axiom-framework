"""New legal-charge/link path builder; no author or earlier builder imports."""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/mobile_compensation_model_20260924.py',)
from collections import defaultdict
from itertools import combinations,product
import math
import numpy as np

CUBE_EDGES=tuple((x,y) for x in range(8) for y in range(x+1,8) if (x^y).bit_count()==1)
CUBE_A=frozenset((0,3,5,6))
CUBE_CHORDS=((2,3),(4,5),(4,6),(5,7),(6,7))

def words(n,A,population,charge,grade):
    k=(population-charge)//2
    assert 2*k==population-charge and k>=0
    out=[]
    for occ in combinations(range(n),population):
        if sum(a not in occ for a in A)!=grade:continue
        for negative in combinations(occ,k):
            out.append(tuple(-1 if x in negative else 1 if x in occ else 0 for x in range(n)))
    return out

def neighbors(a,edges):return tuple(y if a==x else x for x,y in edges if a in (x,y))

def gauss(q,E,A,edges):
    div=[0]*len(q)
    for (x,y),e in zip(edges,E):div[x]+=e;div[y]-=e
    return tuple(div)==tuple(q[x]-int(x in A) for x in range(len(q)))

def move(q,E,source,destination,edges,S=None):
    if q[source]==0 or q[destination]!=0:return None
    e=edges.index(tuple(sorted((source,destination))))
    direction=1 if source<destination else -1
    shift=-direction*q[source]
    amplitude=1.
    if S is not None:
        if abs(E[e]+shift)>S:return None
        amplitude=math.sqrt(1-(E[e]**2+shift*E[e])/(S*(S+1)))
    out=list(q);out[destination]=out[source];out[source]=0
    field=list(E);field[e]+=shift
    return (tuple(out),tuple(field)),amplitude

def F_paths(state,a,edges,S=None,adjoint=False):
    q,E=state
    for b in neighbors(a,edges):
        item=move(q,E,b if adjoint else a,a if adjoint else b,edges,S)
        if item is not None:yield item

def birth_paths(state,edge,charge,edges,S=None):
    q,E=state;x,y=edges[edge]
    if q[x] or q[y]:return
    for c in (-1,1) if charge is None else (charge,):
        if S is not None and abs(E[edge]+c)>S:continue
        amp=1. if S is None else math.sqrt(1-(E[edge]**2+c*E[edge])/(S*(S+1)))
        out=list(q);out[x]=c;out[y]=-c
        field=list(E);field[edge]+=c
        yield (tuple(out),tuple(field)),amp

def effective_birth(state,edge,charge,A,edges,S=None):
    out=defaultdict(float)
    for a in A:
        for mid,amp in F_paths(state,a,edges,S):
            for final,amp2 in birth_paths(mid,edge,charge,edges,S):
                if all(final[0][c] for c in A):out[final]+=amp*amp2
    return dict(out)

def apply_paths(vector,path_rule):
    out=defaultdict(complex)
    for state,amp in vector.items():
        for target,weight in path_rule(state):out[target]+=amp*weight
    return {s:a for s,a in out.items() if abs(a)>1e-13}

def gate(q,a,A,edges):
    near=set(neighbors(a,edges))
    return all(q[c] for c in A if c!=a and near.intersection(neighbors(c,edges)))

def F_matrix(src,dst,a,edges,phase_powers):
    ix={q:i for i,q in enumerate(dst)};F=np.zeros((len(dst),len(src)),complex)
    E=(0,)*len(edges)
    for col,q in enumerate(src):
        for (q2,shift),amp in F_paths((q,E),a,edges):
            if q2 in ix:F[ix[q2],col]+=amp*1j**sum(s*p for s,p in zip(shift,phase_powers))
    return F

def B_matrix(src,dst,edge,charge,A,edges,phase_powers):
    ix={q:i for i,q in enumerate(dst)};B=np.zeros((len(dst),len(src)),complex)
    for col,q in enumerate(src):
        for (q2,shift),amp in effective_birth((q,(0,)*len(edges)),edge,charge,A,edges).items():
            B[ix[q2],col]+=amp*1j**sum(s*p for s,p in zip(shift,phase_powers))
    return B

def rotor_coefficients(n,A,edges,population,charge,phase_powers):
    bases=[words(n,A,population,charge,w) for w in range(3)]
    F0=[F_matrix(bases[0],bases[1],a,edges,phase_powers) for a in sorted(A)]
    F1=[F_matrix(bases[1],bases[2],a,edges,phase_powers) for a in sorted(A)]
    Aop=-sum(F0);M=Aop.conj().T@Aop;Z=(-sum(F1))@Aop
    C0=sum(f.conj().T@f for f in F0)
    C1=np.zeros((len(bases[1]),len(bases[1])),complex)
    C1_plain=C1.copy()
    for a,f in zip(sorted(A),F1):
        m=f.conj().T@f;C1_plain+=m
        Q=np.diag([int(gate(q,a,A,edges)) for q in bases[1]])
        assert np.allclose(Q@m,m@Q)
        C1+=m@Q
    def fourth(C):return M@M-.5*Z.conj().T@Z+Aop.conj().T@C@Aop-.5*(M@C0+C0@M)
    return bases,M,C0,C1,fourth(C1),fourth(C1_plain),Z
