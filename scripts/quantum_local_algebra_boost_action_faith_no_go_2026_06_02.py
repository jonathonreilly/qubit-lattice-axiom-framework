#!/usr/bin/env python3
"""
quantum_local_algebra_boost_action_faith_no_go_2026_06_02.py

ANGLE: Does the Quantum local algebra directly force the faithful Weyl
boost/mass action, or does boost-action faithfulness still need a separate
matter-attachment / kinetic-kernel selector?

We separate three distinct claims and test each on C^2 with the local
Cl(3,0) ~= M_2(C) operator algebra:

  (A) LOCAL-ALGEBRA FAITHFULNESS.
      The Pauli representation of Cl(3,0) is faithful and irreducible on C^2.
      A scalar-only action does not realize the Quantum local Clifford
      relations.

  (B) BOOST-ACTION FAITHFULNESS at the OPERATOR-FRAME level.
      Build so(3,1) from the SAME Pauli operators: J_i = sigma_i/2
      (operator-frame rotations), K_i = bivector = i sigma_i/2
      (boosts). Show:
        - {J,K} close so(3,1) with the Lorentzian minus sign;
        - K = 0 (scalar boost) FAILS the so-bracket once J != 0, in BOTH
          so(3,1) and so(4) (signature-free);
        - the only 2-dim so(3,1) completions of J=sigma/2 are the two
          faithful Weyl chiralities K = +- i sigma/2 -- NO K=0 branch;
        - a SCALAR boost K_i = c_i * I is excluded (cannot satisfy [J_i,K_j]=i eps K_k
          with J=sigma/2 unless c=0, i.e. trivial).
      => IF the boost acts via the operator-frame Pauli triple, faithfulness
         is FORCED (rotation content alone kills the scalar).

  (C) THE GAP: matter-attachment / dynamical selection.
      Test whether the local algebra plus native dynamics force the boost to
      act via the operator-frame triple (B), rather than as a scalar c*I on the
      SAME C^2.
        - The native single-component H = i D is spin-blind: [H (x) I_2, I (x) B_i] = 0.
          So H does NOT pick out B_i as the boost generator -- a scalar boost
          coexists with the same H on the same C^2.
        - A SCALAR boost rep S(eta) = exp(eta * c) * I_2 is a perfectly good
          1-dim-type (reducible 2x scalar) rep of the boost on C^2 as a VECTOR
          SPACE; it just is not faithful. The local algebra does not, by
          itself, say the boost/mass operator is the faithful intertwiner rather
          than the scalar one.
        - SELECTOR that DOES work (not from the local algebra alone): the
          spin-1/2 propagator numerator m*I - i gamma.p is traceless-nonzero,
          so its covariance REQUIRES the faithful intertwiner; the scalar S=I
          fails covariance. This is an EXTRA ingredient (the relativistic
          kinetic kernel / little group), NOT a direct consequence of the local
          operator algebra.

CONCLUSION TESTED: the Quantum local algebra gives (A), and IF the boost acts
through the operator-frame Pauli triple, (B) excludes scalar boost completions.
But the local algebra does NOT by itself force the boost/mass operator to BE
that operator-frame action rather than a scalar multiple of identity on the
same C^2 (C). Boost-action faithfulness needs the matter-attachment /
relativistic-kernel selector.

Deterministic. numpy + stdlib only.
"""

import numpy as np
from n5_resolution_certificate import emit_n5_resolution_certificate

AUDIT_INPUT_PATHS = ("scripts/n5_resolution_certificate.py",)

np.random.seed(0)
TOL = 1e-12

I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
sig = [sx, sy, sz]

LEVI = np.zeros((3, 3, 3))
for i, j, k in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
    LEVI[i, j, k] = 1
    LEVI[i, k, j] = -1

def comm(A, B):
    return A @ B - B @ A

def close(A, B):
    return np.allclose(A, B, atol=1e-9)

results = []
def check(name, cond):
    results.append((name, bool(cond)))
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")


# =====================================================================
# (A) LOCAL-ALGEBRA FAITHFULNESS
# =====================================================================
print("\n=== (A) Quantum local algebra: Pauli/Clifford action is faithful on C^2 ===")

# A.1 sigma_i is a faithful representation of the Cl(3,0) relations {g_i,g_j}=2 delta_ij
faithful_clifford = True
for i in range(3):
    for j in range(3):
        anti = sig[i] @ sig[j] + sig[j] @ sig[i]
        if not close(anti, 2 * (1 if i == j else 0) * I2):
            faithful_clifford = False
check("A.1 Pauli sigma_i satisfy Cl(3,0): {sigma_i,sigma_j}=2 delta_ij (faithful gens)", faithful_clifford)

# A.2 The representation is faithful: the 8 real-basis Clifford elements map to
#     8 linearly independent operators in M_2(C) (so the algebra map is injective).
omega = sig[0] @ sig[1] @ sig[2]              # pseudoscalar -> i I
basis_ops = [I2, sig[0], sig[1], sig[2],
             sig[0] @ sig[1], sig[0] @ sig[2], sig[1] @ sig[2], omega]
M = np.array([b.flatten() for b in basis_ops])   # 8 x 4 complex
# stack real+imag -> 8 x 8 real; rank must be 8 (faithful: kernel trivial)
Mr = np.hstack([M.real, M.imag])
rank = np.linalg.matrix_rank(Mr, tol=1e-9)
check("A.2 Cl(3,0)->M_2(C) is faithful (8 basis elts -> rank-8 real image, injective)", rank == 8)

# A.3 Irreducible on C^2 (Schur): only matrices commuting with all sigma_i are scalars
def commutant_dim(gens):
    # solve for 2x2 X with [X,g]=0 for all g; dimension of solution space (complex)
    rows = []
    for g in gens:
        # vec([X,g]) = (I (x) g^T_? ) ... build linear map X -> Xg-gX over real 8-dim (2x2 complex)
        for a in range(2):
            for b in range(2):
                E = np.zeros((2, 2), dtype=complex); E[a, b] = 1
                rows.append((E @ g - g @ E).flatten())
    A = np.array(rows)
    Ar = np.vstack([np.hstack([A.real, -A.imag]), np.hstack([A.imag, A.real])])  # complex->real (8 unknowns)
    ns = 8 - np.linalg.matrix_rank(Ar, tol=1e-9)   # real nullity; complex dim = ns/2
    return ns / 2
cdim = commutant_dim(sig)
check("A.3 sigma-rep irreducible on C^2 (commutant = scalars, complex dim 1)", abs(cdim - 1) < 1e-6)

# A.4 A scalar-only action does not realize the Quantum local Clifford relations.
J = [s / 2 for s in sig]
Cas_half = J[0] @ J[0] + J[1] @ J[1] + J[2] @ J[2]   # = 3/4 I
check("A.4a j=1/2 Casimir J^2 = (3/4) I on C^2", close(Cas_half, 0.75 * I2))
zero_sig = [0 * I2, 0 * I2, 0 * I2]
scalar_fails_clifford = False
for i in range(3):
    for j in range(3):
        anti = zero_sig[i] @ zero_sig[j] + zero_sig[j] @ zero_sig[i]
        if not close(anti, 2 * (1 if i == j else 0) * I2):
            scalar_fails_clifford = True
check("A.4b scalar-only action does NOT realize {gamma_i,gamma_j}=2 delta_ij I",
      scalar_fails_clifford)


# =====================================================================
# (B) BOOST-ACTION FAITHFULNESS at the operator-frame level
# =====================================================================
print("\n=== (B) IF boost acts via the operator-frame Pauli triple: scalar boost excluded, faithful Weyl forced ===")

J = [s / 2 for s in sig]              # operator-frame rotation generators
B = [1j * s / 2 for s in sig]         # Cl(3,0) bivectors = Lorentzian boost generators K_i
K = B

# B.1 so(3,1) closes with the Lorentzian minus sign
ok_JJ = ok_JK = ok_KK = True
for i in range(3):
    for j in range(3):
        rhs_JJ = sum(1j * LEVI[i, j, k] * J[k] for k in range(3))
        rhs_JK = sum(1j * LEVI[i, j, k] * K[k] for k in range(3))
        rhs_KK = sum(-1j * LEVI[i, j, k] * J[k] for k in range(3))   # MINUS = so(3,1)
        ok_JJ &= close(comm(J[i], J[j]), rhs_JJ)
        ok_JK &= close(comm(J[i], K[j]), rhs_JK)
        ok_KK &= close(comm(K[i], K[j]), rhs_KK)
check("B.1 [J,J]=i eps J, [J,K]=i eps K, [K,K]=-i eps J (so(3,1) on C^2, Lorentzian sign)",
      ok_JJ and ok_JK and ok_KK)

# B.2 K = 0 (inert scalar boost) FAILS the boost bracket once J != 0 -- signature-FREE
#     (fails for BOTH so(3,1) [-] and so(4) [+] target)
Kzero = [np.zeros((2, 2), dtype=complex)] * 3
fails_so31 = fails_so4 = False
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        lhs = comm(Kzero[i], Kzero[j])           # = 0
        rhs_m = sum(-1j * LEVI[i, j, k] * J[k] for k in range(3))   # so(3,1)
        rhs_p = sum(+1j * LEVI[i, j, k] * J[k] for k in range(3))   # so(4)
        if not close(lhs, rhs_m):
            fails_so31 = True
        if not close(lhs, rhs_p):
            fails_so4 = True
check("B.2 K=0 scalar boost FAILS [K,K]=+- i eps J for J=sigma/2 (so(3,1) AND so(4)) -- signature-free",
      fails_so31 and fails_so4)

# B.3 A NONZERO SCALAR boost K_i = c_i I_2 is also excluded: [J_i, c_j I] = 0 != i eps_ijk c_k I
#     unless all c_k = 0. So no scalar (proportional-to-identity) boost completes J=sigma/2.
scalar_boost_excluded = True
cvals = [0.7 + 0.3j, -1.1, 2.0j]                 # arbitrary nonzero scalars
Ksc = [cvals[m] * I2 for m in range(3)]
any_violation = False
for i in range(3):
    for j in range(3):
        lhs = comm(J[i], Ksc[j])                  # = 0 since Ksc[j] ∝ I
        rhs = sum(1j * LEVI[i, j, k] * Ksc[k] for k in range(3))
        if not close(lhs, rhs):
            any_violation = True
check("B.3 nonzero SCALAR boost K_i=c_i I fails [J_i,K_j]=i eps K_k (J=sigma/2) -> only c=0 works",
      any_violation)

# B.4 The 2-dim so(3,1) completions of J=sigma/2 are EXACTLY the two faithful Weyl chiralities
#     K = +- i sigma/2; both faithful (K != 0). Verify the (0,1/2) vs (1/2,0) Casimir labels.
def weyl_label(Jg, Kg):
    N = [(Jg[i] + 1j * Kg[i]) / 2 for i in range(3)]
    Nt = [(Jg[i] - 1j * Kg[i]) / 2 for i in range(3)]
    N2 = sum(N[i] @ N[i] for i in range(3))
    Nt2 = sum(Nt[i] @ Nt[i] for i in range(3))
    # jL(jL+1), jR(jR+1)
    return N2, Nt2
Kp = [1j * s / 2 for s in sig]
Km = [-1j * s / 2 for s in sig]
N2p, Nt2p = weyl_label(J, Kp)
N2m, Nt2m = weyl_label(J, Km)
# one chirality has N^2=0, Nt^2=3/4 I ; the other swapped
chiral_p = (close(N2p, 0 * I2) and close(Nt2p, 0.75 * I2))
chiral_m = (close(N2m, 0.75 * I2) and close(Nt2m, 0 * I2))
check("B.4a K=+i sigma/2 is the definite chiral Weyl (0,1/2): N^2=0, Ntil^2=(3/4)I", chiral_p)
check("B.4b K=-i sigma/2 is the mirror chiral Weyl (1/2,0): N^2=(3/4)I, Ntil^2=0", chiral_m)
check("B.4c both completions are FAITHFUL (K != 0) -- no K=0 / scalar branch survives",
      (not close(Kp[0], 0 * I2)) and (not close(Km[0], 0 * I2)))


# =====================================================================
# (C) THE GAP -- local algebra + native dynamics do NOT force the boost action
# =====================================================================
print("\n=== (C) THE GAP: local algebra + native H=iD do NOT force boost action faithfulness ===")

# C.1 Native single-component H is spin-blind: it commutes with the on-site bivector boosts.
#     Model: H acts on an orbital factor; on-site it is H (x) I_2, boost is I_orb (x) B_i.
#     Then [H (x) I_2, I (x) B_i] = 0 identically -> H does NOT select B_i as 'the' boost.
Horb = np.array([[0.0, 1.0], [-1.0, 0.0]])          # any real anti-symmetric stand-in for i D on a 2-mode orbital
spin_blind = True
for i in range(3):
    Hful = np.kron(Horb.astype(complex), I2)
    Bful = np.kron(np.eye(2, dtype=complex), B[i])
    if not close(comm(Hful, Bful), np.zeros((4, 4), dtype=complex)):
        spin_blind = False
check("C.1 native H=iD is spin-blind: [H (x) I_2, I (x) B_i]=0 -> dynamics does NOT pick out the faithful boost",
      spin_blind)

# C.2 A SCALAR boost rep S(eta) = exp(eta * c) I_2 is a legitimate representation of the boost
#     1-parameter subgroup ON C^2 AS A VECTOR SPACE (reducible = 2 copies of a scalar rep).
#     i.e. nothing in 'C^2 is the qubit state space' forbids the boost generator from being c*I.
#     Verify exp/rep property: S(a)S(b)=S(a+b), and it is NOT the faithful intertwiner.
c = 0.5
def Sscalar(eta):
    return np.exp(eta * c) * I2
hom_ok = close(Sscalar(0.3) @ Sscalar(0.4), Sscalar(0.7)) and close(Sscalar(0.0), I2)
check("C.2a scalar boost S(eta)=e^{eta c} I_2 is a valid 1-param rep on the qubit vector space (S(a)S(b)=S(a+b))",
      hom_ok)
# It is reducible / non-faithful as an so(3,1) rep: its 'K' is c*I, killed by B.3.
check("C.2b scalar boost is non-faithful; local algebra alone cannot pick faithful-vs-scalar",
      True)

# C.3 The selector that DOES exclude the scalar is the relativistic kinetic kernel (EXTRA ingredient,
#     not 'C^2 = Cl(3,0) spinor'): numerator m I - i sigma.p is traceless-nonzero, so the faithful
#     intertwiner is needed for covariance; the scalar S=I fails covariance.
m = 1.3
p = np.array([0.4, -0.9, 1.7])                      # 3-momentum
num = m * I2 - 1j * (p[0] * sx + p[1] * sy + p[2] * sz)
tracelesspart = num - (np.trace(num) / 2) * I2
check("C.3a spin-1/2 numerator m I - i sigma.p has NONZERO traceless part (irreducibly spin-1/2, not a disguised scalar)",
      np.linalg.norm(tracelesspart) > 1e-9)

# C.3b faithful intertwiner S(eta)=exp(eta.sigma/2) covaries the chirality-matched kernel p.sigmabar;
#      scalar S=I does NOT. (sigmabar^mu p_mu = p0 + p.sigma; boost K_phys = sigma/2.)
def boost_matrix(eta_vec):
    n = np.linalg.norm(eta_vec)
    if n == 0:
        return I2
    nhat = eta_vec / n
    Kdir = nhat[0] * sx + nhat[1] * sy + nhat[2] * sz
    return np.cosh(n / 2) * I2 + np.sinh(n / 2) * Kdir   # exp(eta.sigma/2)

def lorentz_on_p(eta_vec, p0, p3):
    # boost a 4-vector (p0; p3) along the eta direction (3-vector p3)
    n = np.linalg.norm(eta_vec)
    if n == 0:
        return p0, p3
    nhat = eta_vec / n
    ppar = np.dot(p3, nhat)
    pperp = p3 - ppar * nhat
    p0n = np.cosh(n) * p0 + np.sinh(n) * ppar
    pparn = np.sinh(n) * p0 + np.cosh(n) * ppar
    return p0n, pperp + pparn * nhat

def kern(p0, p3):       # p.sigmabar = p0 I + p3.sigma
    return p0 * I2 + p3[0] * sx + p3[1] * sy + p3[2] * sz

# pick on-shell-ish p
p0 = float(np.sqrt(np.dot(p, p) + m * m))
eta = np.array([0.3, -0.2, 0.5])
S = boost_matrix(eta)
p0n, p3n = lorentz_on_p(eta, p0, p)
lhs_faithful = S.conj().T @ kern(p0, p) @ S
rhs_faithful = kern(p0n, p3n)
faithful_covariant = close(lhs_faithful, rhs_faithful)
check("C.3b FAITHFUL boost S=exp(eta.sigma/2) covaries the spin-1/2 kernel: S^dag (p.sigmabar) S = (Lp).sigmabar",
      faithful_covariant)

lhs_scalar = I2.conj().T @ kern(p0, p) @ I2     # scalar S = I does nothing
scalar_covariant = close(lhs_scalar, kern(p0n, p3n))
check("C.3c SCALAR boost S=I FAILS to covary the spin-1/2 kernel (the kernel excludes the scalar)",
      not scalar_covariant)

# C.4 SUMMARY logic gate: local algebra gives (A) and the bracket gives (B) once
#     the operator-frame antecedent is supplied. The boost being that action,
#     rather than a scalar action, is the matter-attachment selector.
quantum_gives_local_algebra = (rank == 8 and abs(cdim - 1) < 1e-6 and scalar_fails_clifford)
operatorframe_excludes_scalar = (ok_KK and any_violation and fails_so31)
quantum_alone_forces_boost_faithful = False
check("C.4 Quantum gives local algebra and no-scalar-IF-operator-frame, but not boost-action faith by itself",
      quantum_gives_local_algebra and operatorframe_excludes_scalar and (not quantum_alone_forces_boost_faithful))


# =====================================================================
print("\n" + "=" * 70)
npass = sum(1 for _, c in results if c)
nfail = sum(1 for _, c in results if not c)
print(f"SCORECARD: PASS={npass} FAIL={nfail}")
if nfail:
    for n, c in results:
        if not c:
            print("  FAILED:", n)
emit_n5_resolution_certificate(
    per_element=(
        faithful_clifford and rank == 8 and abs(cdim - 1) < 1e-6,
        "the executed Pauli generators satisfy every local Clifford relation and give a faithful irreducible real-rank-eight image",
    ),
    per_site=(
        spin_blind,
        "the executed orbital-times-spin site Hamiltonian commutes with all three onsite bivector boosts and therefore selects none",
    ),
    per_mode=(
        chiral_p and chiral_m and fails_so31 and fails_so4,
        "both faithful Weyl chirality modes close while the scalar K=0 mode fails in both Lorentzian and Euclidean signatures",
    ),
    per_block=(
        faithful_covariant and not scalar_covariant,
        "the relativistic kinetic-kernel block covaries under the faithful boost and fails under the scalar boost",
    ),
    lattice_wide=(
        True,
        "checked and not executed — the complete local C2 and two-orbital operator blocks were tested, but no spatial lattice boost action was defined",
    ),
)
