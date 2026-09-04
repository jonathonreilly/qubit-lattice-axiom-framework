"""T91b - identify the commutant, and test the SHIFT-type symmetries.
T91: the momentum-diagonal internal symmetry of the framework's operator is only
2-dimensional (identity plus one), not the 16 of u(4).  But that question is
narrower than it looks: the Kahler-Dirac / staggered FLAVOUR symmetry is known to
act by lattice SHIFTS combined with fibre rotations, which a momentum-diagonal
ansatz excludes by construction.

Two things here:
 (A) identify the second commutant element -- is it the Hodge star?
 (B) test the shift-type transformations.  A shift by one site in direction a,
     combined with a fibre operation, is the natural candidate for a flavour
     rotation.  In momentum space a unit shift is the phase exp(i q_a), so the
     candidate symmetry is  M_a(q) = exp(i q_a) * (fibre matrix), and the test is
     whether ANY fibre matrix makes it commute with D(q) for every q."""
import numpy as np, itertools
d=4
BAS=[]
for k in range(d+1): BAS+=[tuple(c) for c in itertools.combinations(range(d),k)]
IDX={b:i for i,b in enumerate(BAS)}; NF=len(BAS)
def Dq(q):
    D=np.zeros((NF,NF),dtype=complex)
    for S in BAS:
        for a in range(d):
            if a in S: continue
            T=tuple(sorted(S+(a,))); sg=(-1)**sum(1 for i in S if i<a)
            D[IDX[T],IDX[S]]+=sg*(np.exp(1j*q[a])-1.0)
    return D+D.conj().T
L=6
qs=[tuple(2*np.pi*np.array(n)/L) for n in itertools.product(range(L),repeat=d)]
sel=qs[::7][:60]
# (A) identify the commutant
rows=[np.kron(np.eye(NF),Dq(q))-np.kron(Dq(q).T,np.eye(NF)) for q in sel]
A=np.vstack(rows); u,s,vh=np.linalg.svd(A)
tol=1e-9*max(A.shape)*s[0]; nul=int(np.sum(s<tol))+(A.shape[1]-len(s))
B=vh[len(s)-nul:].conj().reshape(nul,NF,NF)
print(f"T91b (A)  commutant dimension {nul}; identifying its elements")
star=np.zeros((NF,NF))
for S in BAS:
    C=tuple(sorted(set(range(d))-set(S)))
    perm=list(S)+list(C); sgn=1
    pl=perm[:]
    for i in range(len(pl)):
        for j in range(len(pl)-1):
            if pl[j]>pl[j+1]: pl[j],pl[j+1]=pl[j+1],pl[j]; sgn=-sgn
    star[IDX[C],IDX[S]]=sgn
deg=np.diag([len(b) for b in BAS]).astype(complex)
par=np.diag([(-1)**len(b) for b in BAS]).astype(complex)
cands={"identity":np.eye(NF),"Hodge star":star,"degree":deg,"parity (-1)^deg":par}
P=B.reshape(nul,-1)
Q,_=np.linalg.qr(P.conj().T)
for nm,M in cands.items():
    v=M.reshape(-1).astype(complex); v=v/np.linalg.norm(v)
    resid=float(np.linalg.norm(v-Q@(Q.conj().T@v)))
    print(f"     {nm:>18}: in the commutant? {resid<1e-7}   (residual {resid:.2e})")
print()
print("T91b (B)  SHIFT-type symmetries:  M_a(q) = exp(i q_a) * X,  any fibre X?")
for a in range(d):
    rows=[]
    for q in sel:
        D=Dq(q); ph=np.exp(1j*q[a])
        # [ph*X, D] = 0  <=>  ph*(X D - D X) = 0  <=>  [X,D]=0 : same condition.
        # the genuine staggered shift also permutes the fibre basis, so test
        # X D(q) - D(q) X = 0 with X allowed to depend on the DIRECTION only
        rows.append(np.kron(np.eye(NF),D)-np.kron(D.T,np.eye(NF)))
    Aa=np.vstack(rows); sa=np.linalg.svd(Aa,compute_uv=False)
    tol=1e-9*max(Aa.shape)*sa[0]
    print(f"     direction {a}: solution dimension {int(np.sum(sa<tol))+(Aa.shape[1]-len(sa))}")
print()
print("     a pure phase cannot help -- exp(i q_a) is a scalar and cancels out of")
print("     the commutator -- so shift symmetries of this form add nothing.  The")
print("     genuine staggered flavour rotation permutes the fibre basis AS WELL as")
print("     shifting, and that mixes momenta; it is not diagonal in q at all, so it")
print("     lies outside what this computation can see.")
