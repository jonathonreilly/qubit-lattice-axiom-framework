"""T181 - THE ACTUAL TASTE ALGEBRA: commutant of the blocked lattice operator.

R115 showed the framework's natural operator on Z^3 has 8 doublers, giving
8 species x 2 spinor components = 16 -- exactly the fibre the realization lane
assumed.  That reopened R90's negative, because u(8) would hold SU(3)xSU(2)xU(1)
where u(4) cannot.  But the PHYSICAL taste symmetry is not the full U(8): it is the
subgroup commuting with the lattice operator.  Compute it.

CONSTRUCTION.  Block Z^3 into 2x2x2 cubes, x = 2y + r with r in {0,1}^3.  Fourier
transform in the block index y.  Then
        D(p) = sum_a sigma_a (x) (S_a^+(p) - S_a^-(p)) / 2
where S_a^+ shifts r -> r + e_a inside the block when r_a = 0, and carries the
block phase e^{i p_a} to the next block when r_a = 1 (and conversely for S_a^-).
D(p) is 16x16 = 2 (spin) x 8 (block).

The taste algebra is the commutant of { D(p) : p in the reduced Brillouin zone },
computed the same way T138 did for the Kahler-Dirac case.

CONTROLS that must hold or the construction is wrong:
  * D(p) must be anti-hermitian (the difference operator is antisymmetric);
  * at p = 0 the eight doublers fold together, so D(0) must have a LARGE kernel;
  * the commutant must at least contain the identity."""
import numpy as np, itertools
S=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
R8=[tuple(r) for r in itertools.product([0,1],repeat=3)]
IDX={r:i for i,r in enumerate(R8)}
def shift(a,sign,p):
    """8x8 block-space shift by +-e_a, carrying e^{+-i p_a} when it leaves the cube"""
    M=np.zeros((8,8),dtype=complex)
    for r in R8:
        s=list(r)
        if sign>0:
            if r[a]==0: s[a]=1; ph=1.0
            else:       s[a]=0; ph=np.exp(1j*p[a])
        else:
            if r[a]==1: s[a]=0; ph=1.0
            else:       s[a]=1; ph=np.exp(-1j*p[a])
        M[IDX[tuple(s)],IDX[r]]+=ph
    return M
def Dp(p):
    return sum(np.kron(shift(a,1,p)-shift(a,-1,p),S[a]) for a in range(3))/2.0
print("T181  the taste algebra of the blocked lattice operator")
print()
rng=np.random.default_rng(5)
ps=[np.zeros(3)]+[rng.uniform(-np.pi,np.pi,size=3) for _ in range(40)]
ah=max(np.abs(Dp(p)+Dp(p).conj().T).max() for p in ps)
print(f"   CONTROL anti-hermitian: max |D + D^dag| = {ah:.2e}")
w0=np.linalg.svd(Dp(np.zeros(3)),compute_uv=False)
print(f"   CONTROL D(0) kernel dimension = {int(np.sum(w0<1e-12))} of 16  (doublers fold to p=0)")
print()
def commutant_dim(mats,N):
    A=np.vstack([np.kron(m,np.eye(N))-np.kron(np.eye(N),m.T) for m in mats])
    s=np.linalg.svd(A,compute_uv=False)
    tol=max(A.shape)*np.finfo(float).eps*s.max()
    return int(np.sum(s<=tol)), s
for nps in (1,3,8,20,41):
    mats=[Dp(p) for p in ps[:nps]]
    d,s=commutant_dim(mats,16)
    gap = s[-d-1]/max(s[-d],1e-300) if d<len(s) else float('inf')
    print(f"   commutant over {nps:3d} momenta: dim {d:3d}    sv gap {gap:.1e}")
print()
print("   the dimension at many momenta is the TASTE ALGEBRA.")
print(f"   for reference: u(8) = 64, u(4) = 16, u(2) = 4, u(1) = 1")
print()
d,_=commutant_dim([Dp(p) for p in ps],16)
print(f"   RESULT: taste algebra dimension = {d}")
for nm,dim,cent in (("u(8)",64,26),("u(5)",25,5),("u(4)",16,2),("u(2)",4,None),("u(1)",1,None)):
    if d==dim:
        print(f"   -> matches {nm}; centralizer of su(3) in it = {cent}"
              f"  {'HOLDS su(2), SM fits' if cent and cent>=3 else 'too small for the SM'}")
