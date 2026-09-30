"""Test C: can residual-symmetry misalignment inside the lattice's finite group on the hw=1 triplet give a CKM-like matrix?"""
import itertools, numpy as np
def perms():
    return [np.array([[1.0 if j == p[i] else 0.0 for j in range(3)] for i in range(3)]) for p in itertools.permutations(range(3))]
def signed():
    out=[]
    for P in perms():
        for s in itertools.product((1,-1),repeat=3): out.append(np.diag(s)@P)
    return out
key=lambda M: tuple(np.round(M,6).flatten())
def closure(gens):
    els={key(np.eye(3)):np.eye(3)}; fr=[np.eye(3)]
    while fr:
        new=[]
        for a in fr:
            for g in gens:
                b=g@a; k=key(b)
                if k not in els: els[k]=b; new.append(b)
        fr=new
    return list(els.values())
def subgroups(G):
    subs={}
    for r in (1,2,3):
        for gens in itertools.combinations(G,r):
            H=closure(list(gens)); subs[frozenset(key(h) for h in H)]=H
    return list(subs.values())
ab=lambda H: all(np.allclose(a@b,b@a) for a in H for b in H)
rng=np.random.default_rng(3)
def joint(H):
    c=rng.normal(size=len(H))+1j*rng.normal(size=len(H)); N=sum(ci*h for ci,h in zip(c,H))
    w,V=np.linalg.eig(N)
    if min(abs(w[i]-w[j]) for i in range(3) for j in range(i+1,3))<1e-6: return None
    V=V/np.linalg.norm(V,axis=0)
    return V if np.allclose(V.conj().T@V,np.eye(3),atol=1e-8) else None
def run(G,label):
    bases=[]
    for H in subgroups(G):
        if ab(H):
            V=joint(H)
            if V is not None: bases.append(V)
    # distinct up to column perm/phase
    uniq={}
    for V in bases:
        a=np.abs(V)**2; uniq.setdefault(tuple(sorted(map(tuple,np.round(a.T,6)))),V)
    B=list(uniq.values())
    pats={}
    for Ua in B:
        for Ub in B:
            U=Ua.conj().T@Ub
            best=None
            for P in itertools.permutations(range(3)):
                A=np.abs(U[:,list(P)])
                off=max(A[i,j] for i in range(3) for j in range(3) if i!=j)
                if best is None or off<best[0]: best=(off,A)
            pats.setdefault(tuple(np.round(best[1].flatten(),4)),best)
    print(f"\n{label}: order {len(G)}, distinct joint eigenbases {len(B)}, distinct best-matched |V| patterns {len(pats)}")
    rows=sorted(pats.values(),key=lambda b:b[0])
    for off,A in rows:
        print(f"  max off-diagonal |V| = {off:.4f}   |V| rows: {np.round(A,3).tolist()}")
    nz=[b[0] for b in rows if b[0]>1e-6]
    smallest=min(nz) if nz else None
    print(f"  smallest nonzero max-off-diagonal over patterns: {smallest}   (Cabibbo needs ~0.225 with the OTHER off-diagonals much smaller)")
    ckmlike=[b for b in rows if 0.18<=b[0]<=0.28 and np.sort(np.abs(b[1]).flatten())[-4]<0.31]
    print(f"  CKM-like patterns (largest off-diag in [0.18,0.28], all off-diag <=0.31): {len(ckmlike)}")
run(perms(),"S3 (lattice cubic rotations act as S3 on hw=1)")
run(signed(),"O_h-type signed permutations (adds translation-character phases)")
print("\nReference: Blum-Hagedorn-Lindner (PRD77, 076004): |V_us| = |cos(3 pi/7)| = %.4f needs an order-7 element (D_7); the cubic group has elements of order 2,3,4 only." % abs(np.cos(3*np.pi/7)))
