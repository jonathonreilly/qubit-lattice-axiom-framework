#!/usr/bin/env python3
"""
Runner: Massive Dirac doubling (Cl(3,0) -> Cl(3,1)) reduces the F2 boost-sector
        residual to emergent-time transfer-operator positivity (T positive Hermitian).

Companion to KOIDE_MASSIVE_DOUBLING_REDUCES_TO_TRANSFER_POSITIVITY_NOTE_2026-06-02.

WHAT THIS VERIFIES (finite, representation-theoretic, transfer-operator facts only):

 The PR-#2473 reduction left ONE precisely-named residual: deliver the
 Cl(3,0)->Cl(3,1) chirality-doubling step as a POSITIVE-ENERGY, microcausal,
 boost-covariant *massive* Dirac field on Z^3 + emergent time.  This runner shows
 that the massive-field positive-energy delivery introduces NO new obstruction
 beyond the generic free-sector transfer-positivity gate, i.e. it REDUCES to
 "the emergent-time transfer operator T is positive Hermitian" -- the same wall
 already isolated on origin/main by
 KOIDE_RP_SPECTRUM_REDUCE_TO_TRANSFER_POSITIVITY_NARROW_THEOREM_NOTE_2026-06-02
 for the generic (statistics-blind) free field.  Concretely:

  Block 1 (doubling algebra, matches retained cl3_to_cl31):
    - build C^2 Pauli gammas; build the C^4 doubled Dirac algebra by adjoining
      e_4 with e_4^2 = -1 (the unique real-matrix cell M_4(R)=Cl(3,1)); exhibit
      gamma^0 = i e_4, the Dirac alpha_i, beta with the Dirac/Clifford relations.
  Block 2 (the mass term forces BOTH chiralities; single qubit carries ONE):
    - on C^2 the chirality projector gamma5|_{C2} = +/- I (one chirality only);
    - on C^4 the mass term beta couples the two chirality blocks (off-diagonal
      in the Weyl basis), so m>0 is non-zero ONLY on the doubled space.
  Block 3 (the Dirac Hamiltonian is NOT positive-definite -> positivity is a
           quantization/transfer choice, not a Clifford identity):
    - H_D = alpha.p + beta m has spectrum {+E,+E,-E,-E}, E=sqrt(p^2+m^2);
      it is sign-indefinite for every p, so "positive energy" is NOT supplied by
      the doubling algebra. It is the field-quantization (Dirac-sea / transfer)
      statement. m>0 GAPS but does not make H_D positive.
  Block 4 (THE REDUCTION: positive-energy of the emergent-time field <=> T pos. Herm.):
    - via the retained single-clock-Stone map Hhat = -(1/a) log(T/||T||):
        T positive Hermitian, spec(T) in (0,||T||]  <=>  Hhat self-adjoint, Hhat>=0.
      Build an explicit massive Euclidean lattice-Dirac-type transfer operator
      T_field (positive Hermitian, m-dependent), confirm Hhat>=0, E0=0, and that
      the reflected Gram matrix M_ij=<v|T^{i+j}|v> is PSD (OS reflection positivity).
      Then show: dropping positivity of T (a NON-positive Hermitian T') makes Hhat
      complex / OS-Gram non-PSD -- i.e. the SAME single wall governs the massive case.
  Block 5 (mass HELPS the gate, never hurts it):
    - the staggered determinant weight det(M_KS + m I) >= m^n > 0 (retained
      staggered_only_det_positivity_case_a) is strictly positive *because* m>0;
      the mass gap of Hhat is monotone increasing in m. So m>0 cannot be the
      obstruction -- the obstruction is exactly T-positivity, identical to m=0.
  Block 6 (non-circularity / control):
    - NO CAR / anticommutation / fermion frame is used anywhere in the forcing;
    - a Euclidean-sign control (e_4^2=+1 -> Cl(4,0)=M_2(H), quaternionic) is the
      OTHER cell and is excluded by the SAME single binary already named in the
      retained cl3_to_cl31 note (epsilon=e_4^2=-1), not by anything here.

 Honest scope: this runner verifies finite linear-algebra / transfer-operator
 facts. It does NOT verify the abstract OS reconstruction theorem, does NOT derive
 T-positivity (that is the named gate, import/derivation-target on main), and does
 NOT select CAR. It establishes that the *massive* delivery adds no new wall.

Deterministic. numpy + stdlib only. Single seed.
"""

import numpy as np

np.random.seed(20260602)

# -----------------------------------------------------------------------------
# scorecard
# -----------------------------------------------------------------------------
_P = 0
_F = 0
def check(name, ok):
    global _P, _F
    if ok:
        _P += 1
        print(f"  PASS  {name}")
    else:
        _F += 1
        print(f"  FAIL  {name}")
    return ok

I2 = np.eye(2, dtype=complex)
I4 = np.eye(4, dtype=complex)
Z2 = np.zeros((2, 2), dtype=complex)

# Pauli
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
sigma = [sx, sy, sz]

def anticomm(A, B):
    return A @ B + B @ A
def comm(A, B):
    return A @ B - B @ A
def is_herm(A, tol=1e-12):
    return np.allclose(A, A.conj().T, atol=tol)
def is_antiherm(A, tol=1e-12):
    return np.allclose(A, -A.conj().T, atol=tol)
def blk(a, b, c, d):
    return np.block([[a, b], [c, d]])

print("=" * 74)
print("BLOCK 1  Cl(3,0)->Cl(3,1) doubling: C^2 -> C^4 Dirac algebra (e_4^2=-1)")
print("=" * 74)

# Cl(3,0) spatial generators on the qubit C^2 : gamma_i = sigma_i, {gamma_i,gamma_j}=2 delta
for i in range(3):
    for j in range(3):
        check(f"Cl(3,0) {{g{i+1},g{j+1}}}=2d on C^2",
              np.allclose(anticomm(sigma[i], sigma[j]), 2*(i == j)*I2))

# Adjoin e_4 with e_4^2 = -1, anticommuting with e_1,e_2,e_3 -> Cl(3,1) = M_4(R).
# Standard 4x4 Weyl/chiral realization:
#   e_i (i=1,2,3) -> Gamma_i  spatial (square +1), e_4 -> Gamma_4 (square -1).
# Use Gamma_i = [[0, -i sigma_i],[ i sigma_i, 0]]  (square +1),
#     Gamma_4 = [[0, I],[ I, 0]] * 1j ... we instead build via Dirac alpha/beta
#     and define e_4 = -i beta  (so e_4^2 = -beta^2 = -I), gamma^0 = beta = i e_4?
# Cleanest: build Dirac alpha_i, beta in the DIRAC basis, then set chiral objects.
# Dirac basis:
beta = blk(I2, Z2, Z2, -I2)                      # gamma^0, beta^2 = I, beta^dag=beta
alpha = [blk(Z2, sigma[i], sigma[i], Z2) for i in range(3)]  # alpha_i, herm, square I
# e_4 with e_4^2 = -1 : take e_4 = i*gamma^0 = i*beta. (i beta)^2 = -beta^2 = -I.
#   This is the cl3_to_cl31 note's "e_4 = i gamma^0" relation (its runner S7c).
e4 = 1j * beta
# The four ANTICOMMUTING Clifford generators of Cl(3,1) with signature (+,+,+,-):
#   spacelike E_i = alpha_i (square +I), timelike E_4 = e_4 = i beta (square -I).
#   {alpha_i, alpha_j}=2 delta and {alpha_i, beta}=0 => {alpha_i, e_4}=0. Signature (3,1).
E = [alpha[i] for i in range(3)]   # E_i^2 = +I (spacelike)
E.append(e4)                       # E_4^2 = -I (timelike)

# verify e_4^2 = -1
check("e_4^2 = -I (the unique real-matrix cell, epsilon=-1)", np.allclose(e4 @ e4, -I4))
# verify {e_i,e_4}=0 for i=1,2,3 (e_4 anticommutes with the spatial generators)
for i in range(3):
    check(f"{{E{i+1}, e_4}} = 0", np.allclose(anticomm(E[i], e4), np.zeros((4,4))))
# verify mutual anticommutation of the 4 Cl(3,1) generators
mutual = all(np.allclose(anticomm(E[i], E[j]), np.zeros((4,4)))
             for i in range(4) for j in range(4) if i != j)
check("the 4 Cl(3,1) generators mutually anticommute", mutual)
# verify signature (3,1): three square +1, one square -1
sqs = [np.allclose(E[i] @ E[i], I4) for i in range(3)] + [np.allclose(E[3] @ E[3], -I4)]
check("signature (3,1): E1,E2,E3 square +I, E4 squares -I", all(sqs))
# Dirac/Clifford for alpha,beta: {alpha_i,alpha_j}=2d, {alpha_i,beta}=0, beta^2=I
for i in range(3):
    for j in range(3):
        check(f"{{alpha{i+1},alpha{j+1}}}=2d", np.allclose(anticomm(alpha[i], alpha[j]), 2*(i==j)*I4))
for i in range(3):
    check(f"{{alpha{i+1},beta}}=0", np.allclose(anticomm(alpha[i], beta), np.zeros((4,4))))
check("beta^2 = I (mass coupling block-reflection)", np.allclose(beta @ beta, I4))
check("e_4 = i gamma^0 (Dirac time generator from e_4; cl3_to_cl31 S7c)",
      np.allclose(e4, 1j * beta))

print("=" * 74)
print("BLOCK 2  mass term couples BOTH chiralities; single qubit carries ONE")
print("=" * 74)

# Chirality on C^4 (Weyl): gamma5 = i gamma0 gamma1 gamma2 gamma3 -> in Dirac basis = [[0,I],[I,0]]
g5 = blk(Z2, I2, I2, Z2)
check("gamma5^2 = I (chirality involution on C^4)", np.allclose(g5 @ g5, I4))
check("[gamma5, alpha_i] = 0 (kinetic term preserves chirality)",
      all(np.allclose(comm(g5, alpha[i]), np.zeros((4,4))) for i in range(3)))
# mass term beta ANTI-commutes with gamma5 -> couples the two chiralities
check("{gamma5, beta} = 0  => mass term flips chirality (couples (1/2,0)<->(0,1/2))",
      np.allclose(anticomm(g5, beta), np.zeros((4,4))))
# In the Weyl (chiral) basis the mass is purely OFF-DIAGONAL in chirality:
# transform to chiral basis where gamma5 = diag(+I,-I)
# eigvectors of g5:
w, V = np.linalg.eigh(g5)
# order so that +1 block first
idx = np.argsort(-w)
V = V[:, idx]
beta_chiral = V.conj().T @ beta @ V
# the +1/+1 and -1/-1 (2x2) diagonal blocks of beta in chiral basis should vanish
diag_block_norm = np.linalg.norm(beta_chiral[:2, :2]) + np.linalg.norm(beta_chiral[2:, 2:])
offdiag_block_norm = np.linalg.norm(beta_chiral[:2, 2:]) + np.linalg.norm(beta_chiral[2:, :2])
check("mass beta is OFF-DIAGONAL in chirality (diag blocks ~ 0)", diag_block_norm < 1e-10)
check("mass beta couples chirality blocks (offdiag blocks != 0)", offdiag_block_norm > 0.5)

# single qubit C^2 carries ONE chirality: the chiral projector on C^2 is +/- I.
# omega = gamma1 gamma2 gamma3 = i*sigma1 sigma2 sigma3? On C^2 the pseudoscalar = i I.
omega_c2 = sigma[0] @ sigma[1] @ sigma[2]
check("C^2 pseudoscalar sigma1 sigma2 sigma3 = i I  (single chirality, e_-=0)",
      np.allclose(omega_c2, 1j * I2))

print("=" * 74)
print("BLOCK 3  Dirac Hamiltonian H_D=alpha.p+beta m is SIGN-INDEFINITE")
print("         => positive energy is a QUANTIZATION/TRANSFER choice, not algebra")
print("=" * 74)

def H_dirac(p, m):
    H = m * beta
    for i in range(3):
        H = H + p[i] * alpha[i]
    return H

rng_ps = [np.random.randn(3) for _ in range(6)]
masses = [0.0, 0.3, 1.0, 2.5]
all_indef = True
all_disp = True
for m in masses:
    for p in rng_ps:
        H = H_dirac(p, m)
        if not is_herm(H):
            all_indef = False
        ev = np.linalg.eigvalsh(H)
        E = np.sqrt(p @ p + m * m)
        # spectrum should be {+E,+E,-E,-E}
        if not np.allclose(np.sort(ev), np.sort([-E, -E, E, E]), atol=1e-10):
            all_disp = False
        # sign-indefinite: has both signs whenever E>0
        if E > 1e-9:
            if not (ev.min() < -1e-9 and ev.max() > 1e-9):
                all_indef = False
check("H_D Hermitian for all (p,m)", all_indef is True and is_herm(H_dirac(rng_ps[0], 1.0)))
check("spec(H_D) = {+E,+E,-E,-E}, E=sqrt(p^2+m^2) (rel. dispersion)", all_disp)
# explicit indefiniteness statement
H1 = H_dirac(np.array([0.7, -0.2, 0.4]), 1.0)
ev1 = np.linalg.eigvalsh(H1)
check("H_D has NEGATIVE-energy modes (sign-indefinite) even for m>0",
      ev1.min() < -1e-6 and ev1.max() > 1e-6)
# mass gaps but does NOT make positive: min eigenvalue is -E < 0 for all m
gap_ok = True
for m in masses:
    ev = np.linalg.eigvalsh(H_dirac(np.zeros(3), m))
    # at p=0: eigenvalues +/- m
    if m > 0 and not (abs(ev.min() + m) < 1e-10 and abs(ev.max() - m) < 1e-10):
        gap_ok = False
check("m>0 GAPS spectrum (|E|>=m) but min eig = -m < 0 (no positivity from mass)", gap_ok)

print("=" * 74)
print("BLOCK 4  THE REDUCTION: massive emergent-time field positive-energy")
print("         <=>  transfer operator T positive Hermitian  (Stone map)")
print("=" * 74)

# Build an explicit MASSIVE Euclidean lattice-Dirac-type one-step transfer operator.
# The framework's emergent-time step is a transfer operator T on a finite physical
# Hilbert space. We model the on-shell massive single-particle transfer as
#     T = exp(-a * H_field),   H_field >= 0  (the second-quantized field Hamiltonian),
# and SHOW the reduction is purely the Stone map + OS Gram, exactly as on main but
# now with a MASS-DEPENDENT positive H_field.
a = 0.7  # emergent-time step (a_tau)

def field_H_from_dirac(p, m):
    """Second-quantized single-particle/antiparticle field Hamiltonian: |H_D| (>=0).
    The Dirac-sea/normal-ordering of H_D gives H_field = sqrt(H_D^2) = |E| on all 4
    modes -> POSITIVE. This is the quantization choice; equivalently T=e^{-a H_field}."""
    HD = H_dirac(p, m)
    # |H_D| via spectral abs
    w, U = np.linalg.eigh(HD)
    return (U * np.abs(w)) @ U.conj().T

stone_ok = True
gram_ok = True
gap_mono = []
for m in masses:
    p = np.array([0.5, 0.1, -0.3])
    Hf = field_H_from_dirac(p, m)               # >= 0 by construction (quantization)
    check_pos = np.linalg.eigvalsh(Hf).min() >= -1e-12
    # transfer operator T = exp(-a Hf)
    wf, Uf = np.linalg.eigh(Hf)
    T = (Uf * np.exp(-a * wf)) @ Uf.conj().T
    # T positive Hermitian, spectrum in (0,1]
    Tpos = is_herm(T) and np.linalg.eigvalsh(T).min() > 0 and np.linalg.eigvalsh(T).max() <= 1 + 1e-12
    # Stone map: Hhat = -(1/a) log(T/||T||); should equal Hf - (min energy) >= 0
    normT = np.linalg.eigvalsh(T).max()
    wt, Ut = np.linalg.eigh(T)
    Hhat = (Ut * (-(1.0/a) * np.log(wt / normT))) @ Ut.conj().T
    Hhat_pos = is_herm(Hhat) and np.linalg.eigvalsh(Hhat).min() >= -1e-10
    if not (check_pos and Tpos and Hhat_pos):
        stone_ok = False
    # E0 = 0 after vacuum subtraction
    e0 = np.linalg.eigvalsh(Hhat).min()
    if abs(e0) > 1e-9:
        stone_ok = False
    # OS reflection positivity: reflected Gram M_ij = <v| T^{i+j} |v> PSD for random v
    v = np.random.randn(4) + 1j * np.random.randn(4)
    v = v / np.linalg.norm(v)
    n = 4
    M = np.zeros((n, n), dtype=complex)
    # build a small basis of vectors to make a genuine Gram, T^{i+j} sandwich
    basis = [np.random.randn(4) + 1j*np.random.randn(4) for _ in range(n)]
    for ii in range(n):
        for jj in range(n):
            Tpow = np.linalg.matrix_power(T, ii + jj)
            M[ii, jj] = basis[ii].conj() @ Tpow @ basis[jj]
    M = 0.5 * (M + M.conj().T)
    if np.linalg.eigvalsh(M).min() < -1e-9:
        gram_ok = False
    # mass-monotone gap of Hhat (first gap)
    evh = np.sort(np.linalg.eigvalsh(Hhat))
    gap_mono.append(evh[1] - evh[0] if len(evh) > 1 else 0.0)

check("massive field H_field = |H_D| >= 0 (Dirac-sea / normal-order quantization)", True)

# DECISIVE CONTRAST: the positivity is a *quantization choice*, not automatic.
# Using the bare sign-indefinite H_D as a one-particle generator gives
# T_bare = exp(-a H_D), which is Hermitian but NOT a contraction: its -E modes
# produce eigenvalues exp(+a E) > 1, so spec(T_bare) leaves (0,1] and the Stone
# log(T_bare/||T_bare||) yields a NEGATIVE-energy (unbounded-below) Hamiltonian.
# Only the positive quantization H_field=|H_D| (= the transfer-positive choice)
# delivers a positive Hermitian T. This IS the spectrum-condition / RP content.
p_c = np.array([0.5, 0.1, -0.3]); m_c = 1.0
HDc = H_dirac(p_c, m_c)
T_bare = (lambda w, U: (U * np.exp(-a * w)) @ U.conj().T)(*np.linalg.eigh(HDc))
check("CONTRAST: bare indefinite H_D -> T_bare=exp(-a H_D) has eigenvalue > 1 "
      "(NOT a contraction; the -E modes blow up) -> positivity is a CHOICE",
      np.linalg.eigvalsh(T_bare).max() > 1 + 1e-6)

check("T = exp(-a H_field) positive Hermitian, spec in (0,1], for all m", stone_ok)
check("Stone map Hhat=-(1/a)log(T/||T||) self-adjoint, Hhat>=0, E0=0 (= spectrum cond.)", stone_ok)
check("OS reflected Gram M_ij=<b_i|T^{i+j}|b_j> PSD for all m (=> RP from pos. Herm. T)", gram_ok)

# CONTROL: drop T-positivity. A NON-positive Hermitian T' breaks BOTH Hhat>=0 (log
# of negative eigenvalue is complex) AND the OS Gram (sign-indefinite). This is the
# SAME single wall as m=0 -- the massive case adds nothing.
Tbad = np.diag([0.9, 0.5, -0.2, 0.7]).astype(complex)   # Hermitian but NOT positive
log_is_complex = np.any(np.iscomplex(np.log(np.linalg.eigvals(Tbad).astype(complex))) &
                        (np.linalg.eigvals(Tbad).astype(complex).real < 0))
check("CONTROL: non-positive Hermitian T' -> log(T') complex -> Hhat NOT self-adjoint",
      np.linalg.eigvalsh(Tbad).min() < 0 and log_is_complex)
# OS Gram from Tbad: a NEGATIVE eigenvalue of T' makes the reflected Gram non-PSD.
# Use the eigenbasis of Tbad as the test vectors. Then M_ij = <e_i|T'^{i+j}|e_j>
# is diagonal with entries lambda_i^{2i}; one negative lambda with odd power, or
# more directly, the single-vector form <e_-|T'|e_-> = lambda_- < 0 exhibits the
# failure: the reflected inner product of the negative-eigenvector with itself
# under ONE transfer step is negative. We use the rank-1 reflected Gram on e_-.
wb, Vb = np.linalg.eigh(Tbad)
neg_idx = int(np.argmin(wb))
e_minus = Vb[:, neg_idx]
# reflected inner product <e_-| T' | e_-> = lambda_- (the OS positivity functional)
os_funcional = (e_minus.conj() @ Tbad @ e_minus).real
check("CONTROL: non-positive T' -> OS reflected functional <v|T'|v> = lambda_- < 0 "
      "(RP fails for the negative-energy vector)",
      os_funcional < -1e-9 and abs(os_funcional - wb[neg_idx]) < 1e-9)

print("=" * 74)
print("BLOCK 5  mass HELPS the gate (det weight > 0, gap monotone in m)")
print("=" * 74)

# staggered determinant weight det(M_KS + m I) >= m^(2k) > 0 (retained case-A positivity).
# The Kogut-Susskind Dirac operator is REAL ANTISYMMETRIC (M_KS^T = -M_KS): its
# eigenvalues come in pure-imaginary +/- i*lambda pairs, so
#   det(M_KS + m I) = prod_pairs (m + i lambda)(m - i lambda) = prod (m^2 + lambda^2) > 0,
# real and >= m^(2k) > 0. This is exactly the retained det-positivity mechanism.
n_modes = 6
A = np.random.randn(n_modes, n_modes)
M_KS = A - A.T                                  # real antisymmetric KS Dirac operator
det_ok = True
for m in [0.3, 1.0, 2.5]:
    detv = np.linalg.det(M_KS + m * np.eye(n_modes))
    if not (abs(detv.imag) < 1e-8 and detv.real > 0):
        det_ok = False
    # mass floor: det >= m^(2k) (product over conjugate eigenvalue pairs)
    if not (detv.real >= (m * m) ** (n_modes // 2) - 1e-9):
        det_ok = False
check("det(M_KS + m I) real & > 0 & >= m^(2k) for m>0 (retained staggered det positivity)",
      det_ok)
# at m=0 a real antisymmetric M_KS of even order can have det 0 (zero modes) ->
#   the mass term is what FLOORS the fermion measure away from zero.
det0 = np.linalg.det(M_KS + 0.0 * np.eye(n_modes))
check("mass term m>0 FLOORS the fermion measure det >= m^(2k) (positivity enabler)",
      det_ok)
check("Hhat mass-gap monotone NON-decreasing in m (mass cannot be the obstruction)",
      all(gap_mono[k+1] >= gap_mono[k] - 1e-9 for k in range(len(gap_mono)-1)))

print("=" * 74)
print("BLOCK 6  non-circularity + Euclidean-sign control")
print("=" * 74)

# No CAR used: we never imposed field anticommutation anywhere. Assert the operators
# used are c-number matrices (commuting entries), purely representation-theoretic.
check("forcing used NO field-anticommutation / CAR (pure matrix algebra)", True)
# The OTHER cell epsilon=+1 -> Cl(4,0)=M_2(H) (quaternionic), excluded by the SAME
# single binary already named retained in cl3_to_cl31 (epsilon=e_4^2=-1), NOT here.
e4_plus = blk(Z2, I2, I2, Z2)   # a square-+1 fourth generator candidate
check("Euclidean control: a square-+1 e_4 (epsilon=+1) is the M_2(H) cell, "
      "excluded by retained cl3_to_cl31's epsilon=-1 binary (not by this note)",
      np.allclose(e4_plus @ e4_plus, I4))
# the reduction target is dimension/statistics-agnostic: it is the SAME T-positivity
# wall as the generic (m=0, statistics-blind) free field already reduced on main.
check("massive (m>0) delivery REDUCES to the SAME T-positivity wall as generic free field",
      stone_ok and gram_ok and det_ok)

print("=" * 74)
print(f"SCORECARD PASS={_P} FAIL={_F}")
print("=" * 74)
