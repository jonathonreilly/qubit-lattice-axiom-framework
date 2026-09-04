"""
T228 - reconciling R131 with R145: taste symmetry vs site-internal symmetry.

R131: commutant of the BLOCKED lattice Dirac operator -> six u(6) blocks at
      M12(C); "the SM representations can be embedded".
R145: commutant of the SPACETIME GAMMAS inside the site algebra M_{4k}(C)
      -> exactly u(k); the SM needs k = 5.

These are different objects.  The question that decides whether R131's route is
usable is: CAN A GAUGE SYMMETRY LIVE IN THE TASTE ALGEBRA?

A gauge symmetry must act at each point and commute with the Dirac operator
there -- i.e. commute with D(p) at FIXED p.  A taste generator instead relates
the doubler at p to the one at p + pi*e_mu.  Tested directly below.
"""
import numpy as np, itertools

I2 = np.eye(2,dtype=complex)
SX = np.array([[0,1],[1,0]],dtype=complex)
SY = np.array([[0,-1j],[1j,0]],dtype=complex)
SZ = np.array([[1,0],[0,-1]],dtype=complex)
Z2 = np.zeros((2,2),dtype=complex)
GAM = [np.block([[Z2,I2],[I2,Z2]])] + [np.block([[Z2,S],[-S,Z2]]) for S in (SX,SY,SZ)]

def D(p, k=1):
    M = sum(1j*np.sin(p[mu])*GAM[mu] for mu in range(4))
    return np.kron(M, np.eye(k)) if k > 1 else M

def commutant(mats, n):
    A = np.vstack([np.kron(np.eye(n), m.T) - np.kron(m, np.eye(n)) for m in mats])
    U, sv, Vt = np.linalg.svd(A, full_matrices=False)
    tol = max(A.shape)*np.finfo(float).eps*sv.max()
    return int(np.sum(sv <= tol))

rng = np.random.default_rng(3)
ps = [rng.uniform(-np.pi, np.pi, 4) for _ in range(8)]

print("=== 1. what commutes with D(p) at EVERY p?  (a gauge symmetry must) ===")
for k in (1,2,3,5):
    d = commutant([D(p,k) for p in ps], 4*k)
    print(f"   site algebra M_{4*k}(C):  commutant dimension {d:3d}   "
          f"(= k^2 = dim u({k}) : {d == k*k})")

print("\n=== 2. do the taste generators commute with D(p) at fixed p? ===")
print("   a doubler shift sends p_mu -> p_mu + pi, i.e. sin(p_mu) -> -sin(p_mu).")
for mu in range(4):
    worst_same, worst_shift = 0.0, 0.0
    # the operator implementing the shift on the spinor index
    T = GAM[mu] @ (1j*GAM[0]@GAM[1]@GAM[2]@GAM[3])
    for p in ps:
        q = p.copy(); q[mu] += np.pi
        worst_same  = max(worst_same,  np.max(np.abs(T@D(p) - D(p)@T)))
        worst_shift = max(worst_shift, np.max(np.abs(T@D(p) - D(q)@T)))
    print(f"   mu={mu}:  |[T, D(p)]| = {worst_same:.3f}   "
          f"|T D(p) - D(p+pi e_mu) T| = {worst_shift:.1e}")
print("   => the taste generator does NOT commute with D(p); it MOVES p.")
print("      It is a symmetry of the spectrum relating different momenta,")
print("      not a symmetry acting at a point.")

print("\n=== 3. so where can a gauge symmetry live? ===")
print("   only in the commutant at fixed p, which section 1 measures: u(k).")
print("   The taste algebra is momentum-mixing and cannot carry a gauge charge:")
print("   a gauge transformation acting there would rotate a particle into its")
print("   own doubler.")
print("""
=== verdict ===
  R131 and R145 do not contradict: they compute different commutants.
  But only R145's is a candidate for GAUGE symmetry.  R131's six u(6) blocks
  are taste blocks, and T209 already found the analogous fact for chirality --
  the only chirality on the blocked space was the staggered epsilon, a pure
  taste operator with NO Dirac content.  Housing the Standard Model in the
  taste algebra houses it in doubler space.""")
