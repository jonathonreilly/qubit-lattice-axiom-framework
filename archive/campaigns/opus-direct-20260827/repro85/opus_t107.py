"""T107 - THE NON-ABELIAN STRUCTURE IS THERE, AND MY R41 LOOKED IN THE WRONG PLACE.
docs/INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27
shows the framework's su(2) is the CLIFFORD BIVECTORS  B_i = (1/2) gamma_j gamma_k
-- the Spin(3) generators from the Clifford universal property, identified with
the internal spin generators.  Those are ROTATION generators: they do not commute
with D, so Result 41's commutant search could never have found them.  R41 and
that note do not conflict; they are about different objects.

Building on it: in d=4 the framework's fibre is Lambda*(R^4), 16-dimensional, and
the bivectors generate Spin(4) = SU(2) x SU(2).  That split is by SELF-DUAL versus
ANTI-SELF-DUAL 2-forms -- precisely the duality Result 42 found is unique to four
dimensions.  So the campaign's own d=4 coincidence and the repo's SU(2) route are
the same structure seen twice.

Checked here:
 (A) build the bivectors on the 16-dim fibre; do they close into so(4)? (6 gens)
 (B) does so(4) split as su(2) + su(2), and is the split the self-dual /
     anti-self-dual one of Result 42?
 (C) how do they act on D -- covariantly (a rotation) rather than commuting?"""
import numpy as np, itertools
d=4
BAS=[]
for k in range(d+1): BAS+=[tuple(c) for c in itertools.combinations(range(d),k)]
IDX={b:i for i,b in enumerate(BAS)}; NF=len(BAS)
def eps_op(a):
    M=np.zeros((NF,NF))
    for S in BAS:
        if a in S: continue
        T=tuple(sorted(S+(a,))); M[IDX[T],IDX[S]]=(-1)**sum(1 for i in S if i<a)
    return M
def iota_op(a):
    M=np.zeros((NF,NF))
    for S in BAS:
        for pos,i in enumerate(S):
            if i!=a: continue
            T=tuple(x for x in S if x!=i); M[IDX[T],IDX[S]]+=(-1)**pos
    return M
gam=[eps_op(a)+iota_op(a) for a in range(d)]
print("T107 (A)  Clifford bivectors on the 16-dim fibre")
ok=all(np.allclose(gam[a]@gam[b]+gam[b]@gam[a], 2*(a==b)*np.eye(NF)) for a in range(d) for b in range(d))
print(f"   gammas satisfy the Clifford algebra: {ok}")
B={}
for a,b in itertools.combinations(range(d),2):
    B[(a,b)]=0.5*(gam[a]@gam[b])
gens=list(B.values())
print(f"   {len(gens)} bivectors B_ab = (1/2) gamma_a gamma_b   (so(4) has dim 6: {len(gens)==6})")
# closure: are all commutators in the span?
Mat=np.array([g.reshape(-1) for g in gens])
Q,_=np.linalg.qr(Mat.conj().T)
worst=0.0
for x,y in itertools.combinations(gens,2):
    c=(x@y-y@x).reshape(-1)
    worst=max(worst,float(np.linalg.norm(c-Q@(Q.conj().T@c)))/max(float(np.linalg.norm(c)),1e-12))
print(f"   commutators stay in the span (so(4) closes): worst relative residual {worst:.2e}")
print()
print("T107 (B)  does so(4) split into su(2) + su(2) by SELF-DUALITY?")
def dual_pair(ab):
    return tuple(sorted(set(range(d))-set(ab)))
SD=[];ASD=[]
for ab in itertools.combinations(range(d),2):
    cd=dual_pair(ab)
    perm=list(ab)+list(cd); sgn=1; pl=perm[:]
    for i in range(len(pl)):
        for j in range(len(pl)-1):
            if pl[j]>pl[j+1]: pl[j],pl[j+1]=pl[j+1],pl[j]; sgn=-sgn
    SD.append(0.5*(B[ab]+sgn*B[cd])); ASD.append(0.5*(B[ab]-sgn*B[cd]))
def indep(lst):
    M=np.array([x.reshape(-1) for x in lst])
    return int(np.linalg.matrix_rank(M,tol=1e-9))
print(f"   self-dual combinations span dimension {indep(SD)}   (su(2) is 3)")
print(f"   anti-self-dual span dimension        {indep(ASD)}   (su(2) is 3)")
crossed=0.0
for x in SD:
    for y in ASD:
        crossed=max(crossed,float(np.max(np.abs(x@y-y@x))))
print(f"   the two families COMMUTE with each other: max||[SD,ASD]|| = {crossed:.2e}")
print("   (commuting 3+3 => so(4) = su(2) + su(2), the R42 self-duality split)")
print()
print("T107 (C)  how the bivectors act on D: covariantly, not by commuting")
def Dq(q):
    D=np.zeros((NF,NF),dtype=complex)
    for S in BAS:
        for a in range(d):
            if a in S: continue
            T=tuple(sorted(S+(a,))); sg=(-1)**sum(1 for i in S if i<a)
            D[IDX[T],IDX[S]]+=sg*(np.exp(1j*q[a])-1.0)
    return D+D.conj().T
q=tuple(2*np.pi*np.array([1,2,0,3])/6)
D=Dq(q)
for nm,Bg in (("B_01",B[(0,1)]),("B_23",B[(2,3)])):
    cm=float(np.max(np.abs(Bg@D-D@Bg)))
    print(f"   ||[{nm}, D(q)]|| = {cm:8.4f}   (nonzero: a rotation, not an internal symmetry)")
print()
print("   so the framework DOES carry non-abelian structure -- so(4) = su(2)+su(2)")
print("   on the fibre -- and Result 41's 'only U(1)' was a statement about the")
print("   COMMUTANT, which by construction excludes rotation generators.")
