"""
T225 - what IS the single addition, algebraically?

The Qubit axiom names M2(C), and offers Cl(3,0) as an equivalent presentation.
Claim to test: Cl(1,3)^+ -- the EVEN part of the Clifford algebra of 3+1
SPACETIME (rotations and boosts) -- is the SAME real algebra, M2(C).  If so the
axioms already carry the Lorentz group of four-dimensional spacetime while
supplying only three lattice directions, and the R142 enlargement to M4(C)
adds exactly the ODD part: the four gammas.

  Cl(3,0)      real dim 8   ~ M2(C)     (the axiom's own presentation)
  Cl(1,3)^+    real dim 8   ~ M2(C)     <- to be verified
  Cl(1,3) (x)C cplx dim 16  ~ M4(C)     (what R142 forces)
"""
import numpy as np, itertools

I2 = np.eye(2, dtype=complex)
SX = np.array([[0,1],[1,0]],dtype=complex)
SY = np.array([[0,-1j],[1j,0]],dtype=complex)
SZ = np.array([[1,0],[0,-1]],dtype=complex)
S  = [SX, SY, SZ]
kr = lambda a,b: np.kron(a,b)

# Weyl basis: gamma^0 = [[0,I],[I,0]], gamma^k = [[0,sigma_k],[-sigma_k,0]]
Z2 = np.zeros((2,2), dtype=complex)
g0 = np.block([[Z2, I2],[I2, Z2]])
gk = [np.block([[Z2, S[k]],[-S[k], Z2]]) for k in range(3)]
GAM = [g0] + gk
g5 = 1j*GAM[0]@GAM[1]@GAM[2]@GAM[3]

eta = np.diag([1,-1,-1,-1]).astype(float)
worst = 0.0
for a in range(4):
    for b in range(4):
        worst = max(worst, np.max(np.abs(GAM[a]@GAM[b] + GAM[b]@GAM[a] - 2*eta[a,b]*np.eye(4))))
print(f"Cl(1,3) relations {{g_a,g_b}} = 2 eta_ab : max err {worst:.1e}")
print(f"gamma5 = i g0g1g2g3 ; gamma5^2 = I : {np.max(np.abs(g5@g5-np.eye(4))):.1e}")

# ---- real span of the EVEN subalgebra --------------------------------------
def real_span_dim(mats):
    V = np.array([np.concatenate([m.real.ravel(), m.imag.ravel()]) for m in mats])
    return np.linalg.matrix_rank(V, tol=1e-9)

even = [np.eye(4, dtype=complex)]
for a in range(4):
    for b in range(a+1,4):
        even.append(GAM[a]@GAM[b])
omega = GAM[0]@GAM[1]@GAM[2]@GAM[3]     # the REAL pseudoscalar: no factor of i.
even.append(omega)                       # (g5 = i*omega is NOT in the real algebra)
print(f"\nCl(1,3)^+ spanned by 1, the 6 bivectors, and omega -> "
      f"real span dimension {real_span_dim(even)}  (expect 8)")

cl30 = []
for r in range(4):
    for T in itertools.combinations(range(3), r):
        M = np.eye(2, dtype=complex)
        for a in T: M = M @ S[a]
        cl30.append(M)
print(f"Cl(3,0) spanned by products of the 3 Paulis      -> "
      f"real span dimension {real_span_dim(cl30)}  (expect 8, = M2(C))")

# ---- is the even part block-diagonal, and is the upper block all of M2(C)? --
offdiag = max(np.max(np.abs(m[:2,2:])) + np.max(np.abs(m[2:,:2])) for m in even)
print(f"\nevery even element is block-diagonal in the Weyl basis: "
      f"max off-block entry {offdiag:.1e}")
upper = [m[:2,:2] for m in even]
print(f"upper blocks of Cl(1,3)^+ span, as a REAL algebra, dimension "
      f"{real_span_dim(upper)}  (8 = all of M2(C))")
lower = [m[2:,2:] for m in even]
# report the ACTUAL relation between the blocks rather than asserting one
cands = {"lower = upper": lambda u: u,
         "lower = conj(upper)": np.conj,
         "lower = inv(upper^dagger)": lambda u: np.linalg.pinv(u.conj().T)}
for nm, fn in cands.items():
    try:
        e = max(np.max(np.abs(l - fn(u))) for u, l in zip(upper, lower))
        print(f"   {nm:28s}: max err {e:.1e}")
    except Exception as ex:
        print(f"   {nm:28s}: n/a")
print(f"   the upper-block map is an injective real-algebra map onto M2(C)"
      f" iff its image has real dimension 8 (above).")

# ---- and the full complexified algebra is M4(C) -----------------------------
full = []
for r in range(5):
    for T in itertools.combinations(range(4), r):
        M = np.eye(4, dtype=complex)
        for a in T: M = M @ GAM[a]
        full.append(M)
V = np.array([m.ravel() for m in full])
print(f"\nCl(1,3) (x) C spanned by the 16 gamma products -> complex span "
      f"dimension {np.linalg.matrix_rank(V, tol=1e-9)}  (16 = all of M4(C))")

print("""
=== what the single addition IS ===
  the axioms' site algebra M2(C) = Cl(3,0) = Cl(1,3)^+ :
      the ROTATIONS AND BOOSTS of 3+1 spacetime, and nothing else.
  the R142 enlargement to M4(C) = Cl(1,3) (x) C adds exactly the ODD part:
      the four gammas themselves.
  => the axioms already carry the SYMMETRY of four-dimensional spacetime
     while supplying only three directions for it to act on.  The addition
     supplies the missing directions, and nothing more.""")
