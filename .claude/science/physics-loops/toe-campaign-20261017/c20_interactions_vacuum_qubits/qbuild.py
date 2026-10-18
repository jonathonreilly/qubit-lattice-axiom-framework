"""Pauli images of the corner-model one-fermion terms in the 48-qubit-per-site corner code (flux 1011),
checked: gauge invariance, fermionic algebra (mod stabilizers), and covariance under the code's rotations."""
import sys, itertools, random, numpy as np
from collections import deque
sys.argv=['q','4','1011']
Q_ = {}
exec(open('qcode.py').read().split("if __name__ == '__main__':")[0], Q_)
import diraclib as D
random.seed(3)
qs=Q_  # namespace
VERTS=qs['VERTS']; INC=qs['INC']; A=qs['A']; Bop=qs['Bop']; pmul=qs['pmul']; pcomm=qs['pcomm']
# --- stabilizer group (loops + R), and partial reduction to canonical form
G=qs['Group'](qs['NQ'])
stabs=[qs['Rop'](v,h) for v in qs['SITES'] for h in qs['HALF'] if sum(h[1])>0]+[qs['loop_op'](seq,qs['FLUX'][kind]) for kind,seq in qs['cycles']()]
for P in stabs: G.add(P)
# fix the logical sector: noncontractible Wilson loops with the holonomies of the identified gauge
def wilson(a):
    v0=(0,0,0); c0=[c for c in qs['CORN'] if a not in c and qs['neg'](a) not in c][0]
    q=(v0,c0); seq=[q]; disp=np.zeros(3,int)
    for step in range(qs['L']):
        nxt=(tuple((x+y)%qs['L'] for x,y in zip(q[0],a)),c0)
        p=path(q,nxt); seq+=p[1:]; q=nxt
    n=len(seq)-1; S=(0,0,n%4); up=1.0
    for i in range(n): S=pmul(S,A(seq[i],seq[i+1])); up*=u_dl(seq[i],seq[i+1])
    if up<0: S=(S[0],S[1],(S[2]+2)%4)
    return S
def canon(P):
    """reduce P modulo the stabilizer group: returns (x,z) remainder and phase exponent"""
    v=G.vec(P); comb=P
    while True:
        hit=False
        for c in sorted(G.piv, reverse=True):
            if (v>>c)&1:
                pv,pP=G.piv[c]; v^=pv; comb=pmul(comb,pP); hit=True; break
        if not hit: break
        # continue until no pivot bit remains
        if not any((v>>c)&1 for c in G.piv): break
    return (comb[0],comb[1]), comb[2]%4
# operator = dict {(x,z): complex coeff}  meaning sum coeff * X^x Z^z
def pauli_op(P, coef=1.0):
    return {(P[0],P[1]): coef*(1j**P[2])}
def omul(a,b):
    out={}
    for (x1,z1),c1 in a.items():
        for (x2,z2),c2 in b.items():
            s=(-1)**bin(z1&x2).count('1')
            k=(x1^x2,z1^z2); out[k]=out.get(k,0)+c1*c2*s
    return {k:v for k,v in out.items() if abs(v)>1e-12}
def oadd(a,b,s=1.0):
    out=dict(a)
    for k,v in b.items(): out[k]=out.get(k,0)+s*v
    return {k:v for k,v in out.items() if abs(v)>1e-12}
def ocanon(a):
    """reduce every Pauli modulo stabilizers (code-space equivalence)"""
    out={}
    for (x,z),c in a.items():
        k,ph=canon((x,z,0)); out[k]=out.get(k,0)+c*(1j**ph)
    return {k:v for k,v in out.items() if abs(v)>1e-9}
# --- gauge: identify code vertices with diraclib vertices and use diraclib's u as the code gauge
def dkey(q): v,c=q; return (v,frozenset(c))
DV={dkey(q):i for i,q in enumerate(VERTS)}
dl_index={ (v,c):i for i,(v,c) in enumerate(D.C.VERTS)}
def u_dl(q,r):
    a=dl_index[dkey(q)]; b=dl_index[dkey(r)]
    return (-1.0)**D.u[D.C.EID[frozenset((a,b))]]
def path(src,dst):
    prev={src:None}; dq=deque([src])
    while dq:
        x=dq.popleft()
        if x==dst: break
        for _,_,nb in INC[x]:
            if nb not in prev: prev[nb]=x; dq.append(nb)
    p=[dst]
    while p[-1]!=src: p.append(prev[p[-1]])
    return p[::-1]
def Gop(q,r):
    """image of gamma_q gamma_r: i^n prod A along a path / prod u"""
    p=path(q,r); n=len(p)-1; S=(0,0,n%4); uprod=1.0
    for i in range(n): S=pmul(S,A(p[i],p[i+1])); uprod*=u_dl(p[i],p[i+1])
    return pauli_op(S, 1.0/uprod)
def hop(q,r,h=1.0):
    """image of h c^dag_q c_r + h.c. (q != r): G (1+B_q)(1-B_r)/4 + h.c."""
    Gq=Gop(q,r); Bq=pauli_op(Bop(q)); Br=pauli_op(Bop(r)); one={(0,0):1.0}
    t=omul(omul(Gq,oadd(one,Bq)),oadd(one,Br,-1.0)); t={k:v*h/4 for k,v in t.items()}
    # hermitian conjugate
    tc={}
    for (x,z),c in t.items():
        ph=(-1)**bin(x&z).count('1')     # (X^x Z^z)^dag = Z^z X^x = (-1)^{|x&z|} X^x Z^z
        tc[(x,z)]=tc.get((x,z),0)+np.conj(c)*ph
    return oadd(t,tc)
def single(q,r):   # c^dag_q c_r alone (for algebra tests)
    Gq=Gop(q,r); Bq=pauli_op(Bop(q)); Br=pauli_op(Bop(r)); one={(0,0):1.0}
    t=omul(omul(Gq,oadd(one,Bq)),oadd(one,Br,-1.0)); return {k:v/4 for k,v in t.items()}
for a in [(1,0,0),(0,1,0),(0,0,1)]:
    W=wilson(a); assert qs['herm'](W)
    r=G.add(W)
    print('Wilson loop',a,'added as independent generator' if r is True else ('dependent, consistent' if r==0 else 'INCONSISTENT'))
PASS=FAIL=0
def check(name,ok,detail=''):
    global PASS,FAIL
    PASS+=bool(ok); FAIL+=(not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}"+(f"  {detail}" if detail else ''))
# 1. gauge invariance: images commute with every stabilizer
verts=random.sample(VERTS,40)
ok=True
for _ in range(20):
    q,r=random.sample(verts,2); T=single(q,r)
    for S in random.sample(stabs,150):
        for (x,z) in T:
            if not pcomm((x,z,0),S): ok=False
check("images of c^dag_q c_r commute with all sampled stabilizers (loops and repetition terms)", ok)
# 2. fermionic algebra mod stabilizers: [c^dag_a c_b, c^dag_b c_c] = c^dag_a c_c
bad=0; tested=0
for _ in range(25):
    a,b,c=random.sample(verts,3)
    X1=single(a,b); X2=single(b,c); X3=single(a,c)
    comm=oadd(omul(X1,X2),omul(X2,X1),-1.0)
    d=ocanon(oadd(comm,X3,-1.0)); tested+=1
    if d: bad+=1
check("fermionic algebra: [Q(c+_a c_b), Q(c+_b c_c)] = Q(c+_a c_c) on the code space (random triples, mod stabilizers)", bad==0, f"{tested-bad}/{tested}")
bad=0
for _ in range(15):
    a,b=random.sample(verts,2); c_,d_=random.sample([v for v in verts if v not in (a,b)],2)
    comm=ocanon(oadd(omul(single(a,b),single(c_,d_)),omul(single(c_,d_),single(a,b)),-1.0))
    if comm: bad+=1
check("disjoint bilinears commute on the code space", bad==0)

# 3. on-site density terms: n_q = (1 - B_q)/2 ; algebra [n_a, c+_a c_b] = c+_a c_b
def dens(q): return oadd({(0,0):0.5}, pauli_op(Bop(q)), -0.5)
bad=0
for _ in range(15):
    a,b=random.sample(verts,2)
    comm=oadd(omul(dens(a),single(a,b)),omul(single(a,b),dens(a)),-1.0)
    if ocanon(oadd(comm,single(a,b),-1.0)): bad+=1
check("[Q(n_a), Q(c+_a c_b)] = Q(c+_a c_b) on the code space", bad==0)
# 4. covariance under the code's rotation operators U_R (site permutation x on-site CZ x Z fixes)
EDGES=[]; seen=set()
for q in VERTS:
    for k,e,nb in INC[q]:
        key=frozenset((qs['VID'][q],qs['VID'][nb]))
        if key not in seen: seen.add(key); EDGES.append((q,nb) if qs['canon_first'](q,nb) else (nb,q))
def rot_op(R):
    perm=qs['qperm'](R); cz=qs['cz_network'](R); zf=0
    for e in EDGES:
        img=qs['apply_cz'](qs['apply_perm'](A(*e),perm),cz); q,r=e
        Rq=(qs['rs'](R,q[0]),qs['rc'](R,q[1])); Rr=(qs['rs'](R,r[0]),qs['rc'](R,r[1]))
        tgt=A(Rq,Rr)
        if (img[2]-tgt[2])%4==2:
            if not qs['canon_first'](Rq,Rr): Rq,Rr=Rr,Rq
            zf^=1<<qs['edge_zqubit'](Rq,*[ed for k,ed,nb in INC[Rq] if nb==Rr][0])
    return perm,cz,zf
def U_apply(rop,opr):
    perm,cz,zf=rop; out={}
    for (x,z),c in opr.items():
        P=qs['apply_zfix'](qs['apply_cz'](qs['apply_perm']((x,z,0),perm),cz),zf)
        k=(P[0],P[1]); out[k]=out.get(k,0)+c*(1j**P[2])
    return out
def d_index(R):
    for k,S in enumerate(D.C.ROTS):
        if (S==R).all(): return k
bad=0; tested=0
for R in [qs['ROTS'][i] for i in random.sample(range(24),6)]:
    rop=rot_op(R); P_,sg=D.rots[d_index(R)]
    for _ in range(6):
        q,r=random.sample(verts,2)
        Rq=(qs['rs'](R,q[0]),qs['rc'](R,q[1])); Rr=(qs['rs'](R,r[0]),qs['rc'](R,r[1]))
        sq=(-1.0)**sg[dl_index[dkey(q)]]; sr=(-1.0)**sg[dl_index[dkey(r)]]
        lhs=U_apply(rop,single(q,r)); rhs={k:v*sq*sr for k,v in single(Rq,Rr).items()}
        tested+=1
        if ocanon(oadd(lhs,rhs,-1.0)): bad+=1
check("covariance: U_R Q(c+_q c_r) U_R^dag = sigma_R(q) sigma_R(r) Q(c+_Rq c_Rr) with the fermion-level PSG signs (6 rotations x 6 terms)", bad==0, f"{tested-bad}/{tested}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
