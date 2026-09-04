"""
T227 - how big must the site algebra be to carry BOTH spacetime and the
Standard Model gauge algebra?

R143: M4(C) = Cl(1,3) (x) C exactly -- the spacetime Clifford algebra with
nothing left over.  If so, M4(C) has NO room for internal symmetry, and the
internal symmetry available in M_{4k}(C) is exactly the commutant of the
spacetime gammas.

  step 1  commutant of {Gamma_mu (x) I_k} inside M_{4k}(C)  =?  I_4 (x) M_k(C)
          -> internal symmetry is exactly u(k)
  step 2  minimal k with a FAITHFUL k-dim rep of su(3) + su(2) + u(1)

Nothing here is imported: both steps are computed.
"""
import numpy as np, itertools

I2 = np.eye(2, dtype=complex)
SX = np.array([[0,1],[1,0]],dtype=complex)
SY = np.array([[0,-1j],[1j,0]],dtype=complex)
SZ = np.array([[1,0],[0,-1]],dtype=complex)
Z2 = np.zeros((2,2),dtype=complex)
g0 = np.block([[Z2,I2],[I2,Z2]])
GAM = [g0] + [np.block([[Z2,S],[-S,Z2]]) for S in (SX,SY,SZ)]

def commutant_dim(gens, n):
    A = np.vstack([np.kron(np.eye(n), g.T) - np.kron(g, np.eye(n)) for g in gens])
    U, sv, Vt = np.linalg.svd(A, full_matrices=False)
    tol = max(A.shape)*np.finfo(float).eps*sv.max()
    return int(np.sum(sv <= tol))

print("=== step 1: internal symmetry = commutant of the spacetime gammas ===")
print("   k    dim M_{4k}(C)   commutant dim   expect k^2 (= u(k))")
for k in (1,2,3,5):
    G = [np.kron(g, np.eye(k)) for g in GAM]
    d = commutant_dim(G, 4*k)
    print(f"  {k:2d}      {(4*k)**2:7d}        {d:7d}          {k*k:5d}   "
          f"{'OK' if d==k*k else 'MISMATCH'}")
print("  => M4(C) alone (k=1) has commutant dimension 1: SCALARS ONLY.")
print("     the spacetime Clifford algebra uses up ALL of M4(C);")
print("     internal symmetry requires M_{4k}(C) and is exactly u(k).")

print("\n=== step 2: minimal k with a faithful rep of su(3)+su(2)+u(1) ===")
# irreps of su(3) x su(2) have dimension d3*d2; enumerate small ones
d3s = [1,3,3,6,8]          # 1, 3, 3bar, 6, 8
d2s = [1,2,3,4]            # 1, 2, 3, 4
def partitions(k):
    """multisets of irrep dims (d3,d2) summing to k"""
    items = [(a,b) for a in d3s for b in d2s]
    seen = set()
    def rec(rem, start, cur):
        if rem == 0: seen.add(tuple(sorted(cur))); return
        for i in range(start, len(items)):
            d = items[i][0]*items[i][1]
            if d <= rem: rec(rem-d, i, cur+[items[i]])
    rec(k, 0, [])
    return seen
for k in range(1, 7):
    ok = []
    for p in partitions(k):
        su3_faithful = any(a != 1 for a,b in p)      # some su(3)-nontrivial piece
        su2_faithful = any(b != 1 for a,b in p)      # some su(2)-nontrivial piece
        if su3_faithful and su2_faithful: ok.append(p)
    print(f"  k={k}: faithful decompositions = {len(ok)}"
          + (f"   e.g. {sorted(ok, key=len)[0]}" if ok else "   -> IMPOSSIBLE"))

print("""
  su(3) needs a piece of dimension >= 3 and su(2) a piece of dimension >= 2,
  and they must be DIFFERENT summands unless combined as (3,2) which is 6.
  So the minimum is 3 + 2 = 5, realised by (3,1) + (1,2), with u(1) acting
  with different charges on the two summands.

=== the result ===
  minimal site algebra carrying spacetime AND the SM gauge algebra:
      M4(C) (x) M5(C) = M20(C),  internal symmetry u(5)
  and (3,1)+(1,2) is exactly the 5 of SU(5) -- the same statement, not a
  second one.""")

# verify the k=5 embedding explicitly
print("\n=== explicit check that su(3)+su(2)+u(1) embeds in u(5) faithfully ===")
lam = []
for i in range(3):
    for j in range(3):
        if i<j:
            E = np.zeros((3,3),dtype=complex); E[i,j]=1; E[j,i]=1; lam.append(E)
            F = np.zeros((3,3),dtype=complex); F[i,j]=-1j; F[j,i]=1j; lam.append(F)
lam.append(np.diag([1,-1,0]).astype(complex))
lam.append(np.diag([1,1,-2]).astype(complex)/np.sqrt(3))
su2 = [SX, SY, SZ]
gens = []
for L in lam:
    M = np.zeros((5,5),dtype=complex); M[:3,:3] = L; gens.append(M)
for S in su2:
    M = np.zeros((5,5),dtype=complex); M[3:,3:] = S; gens.append(M)
Y = np.diag([1,1,1,-1.5,-1.5]).astype(complex); gens.append(Y)
print(f"  generators built: {len(gens)}  (8 su(3) + 3 su(2) + 1 u(1) = 12)")
V = np.array([g.ravel() for g in gens])
print(f"  real span dimension of the 12 generators in u(5): "
      f"{np.linalg.matrix_rank(V, tol=1e-9)}  (12 => faithful, independent)")
tr = max(abs(np.trace(g)) for g in gens[:11])
print(f"  su(3) and su(2) generators traceless: max |tr| = {tr:.1e}")
