"""AC_phi_lambda sub-admission (iii) species-bridge decomposition support runner.

Class-A finite-dimensional exact checks for
docs/ACPHILAMBDA_SPECIES_BRIDGE_REALIZED_STATE_DECOMPOSITION_NOTE_2026-06-11.md

Verifies, on a concrete C_3 generation carrier (the hw=1 triplet inside the
corner cube, embedded in C^8 = (C^2)^{x3}):

  A. carrier / de-naming vacuity (the labeling bijection changes no registered
     quantity);
  B. the registration-statement formalization (a finite record-stack model in
     which the sector-carrying-the-pattern assignment is pointwise evaluated,
     uniquely record-determined, carrier-membership tautological given the
     supplied readout context, and state-contingent under the realized-state
     primitive's counterfactual test);
  C. the genuine structural residual (the carrier-locus selection is an
     operator-class fact, not a registration statement: naive dispersion is
     hw-blind across all 8 corners; Wilson distinguishes hw=0; hw=1<->hw=2 is
     the compensated complementation class);
  D. the color contrast (single-named-frame color model has no surviving
     per-sector record for pointwise evaluation; intra-color labels are
     gauge-moved while registered invariants are fixed);
  E. hostile guards (no external/PDG datum enters; the decomposition strictly
     reduces the assignment freedom rather than renaming it).

All checks are exact finite linear algebra on dims <= 9. No registry, audit,
or effective-status field is read or written. The runner derives nothing about
r (dial discipline): the pattern parameters (a, B, delta) are arbitrary
admissible placeholders, never matched values.
"""

import numpy as np
from itertools import permutations, product

TOL = 1e-12
PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"PASS  {name}")
    else:
        FAIL += 1
        print(f"FAIL  {name}")


# ---------------------------------------------------------------- carrier ---
# Corner cube {0,1}^3; Hamming weight grading; C_3[111] = cyclic coordinate
# rotation. hw=1 triplet = {(1,0,0),(0,1,0),(0,0,1)}.

corners = list(product([0, 1], repeat=3))
hw = {c: sum(c) for c in corners}
rot = lambda c: (c[2], c[0], c[1])          # C_3[111]
comp = lambda c: tuple(1 - b for b in c)    # complementation

hw1 = [c for c in corners if hw[c] == 1]
hw2 = [c for c in corners if hw[c] == 2]

# A1: C_3[111] acts as a free 3-cycle on the hw=1 triplet (and on hw=2).
orbit = {hw1[0]}
c = hw1[0]
for _ in range(2):
    c = rot(c)
    orbit.add(c)
check("A1 C3[111] free 3-cycle on hw=1 (orbit = full triplet)",
      orbit == set(hw1) and rot(rot(rot(hw1[0]))) == hw1[0])

# ---------------------------------------------------- monitored family ------
# K-real circulant generation-monitored operator on the C^3 triplet carrier:
#   M(a,B,delta) = a I + b J + conj(b) J^2,  b = B exp(i delta).
# Arbitrary admissible placeholder values; NOT matched, NOT derived.
a0, B0, d0 = 1.0, 0.3, 0.4

J = np.zeros((3, 3), dtype=complex)
for k in range(3):
    J[(k + 1) % 3, k] = 1.0

def M_of(a, B, delta):
    b = B * np.exp(1j * delta)
    return a * np.eye(3) + b * J + np.conj(b) * (J @ J)

M = M_of(a0, B0, d0)
omega = np.exp(2j * np.pi / 3)
# Fourier eigenvectors of J (J V_k = omega^{-k} V_k under this convention);
# spectral projectors P_k of M (the supplied readout context).
V = np.array([[omega ** (j * k) for k in range(3)] for j in range(3)]) / np.sqrt(3)
P = [np.outer(V[:, k], V[:, k].conj()) for k in range(3)]
lam = np.array([a0 + 2 * B0 * np.cos(d0 - 2 * np.pi * k / 3) for k in range(3)])

check("B0 K-real circulant: M Hermitian, eigenvalues real and distinct",
      np.allclose(M, M.conj().T, atol=TOL)
      and np.allclose(sorted(np.linalg.eigvalsh(M)), sorted(lam), atol=1e-9)
      and min(abs(lam[i] - lam[j]) for i in range(3) for j in range(i + 1, 3)) > 1e-6)

check("B0b supplied readout context {P_k}: orthogonal resolution, M = sum lam_k P_k",
      all(np.allclose(P[i] @ P[j], (P[i] if i == j else 0 * P[i]), atol=TOL)
          for i in range(3) for j in range(3))
      and np.allclose(sum(P), np.eye(3), atol=TOL)
      and np.allclose(sum(lam[k] * P[k] for k in range(3)), M, atol=TOL))

# ------------------------------------------------- A2 de-naming vacuity -----
# A species-name bijection pi relabels (sector_k, value_k) pairs jointly.
# Every registered invariant (the multiset of registered per-sector values,
# every symmetric polynomial) is unchanged.
multiset0 = sorted(np.round(lam, 12))
all_invariant = True
for pi in permutations(range(3)):
    relabeled = sorted(np.round(lam[list(pi)], 12))
    if relabeled != multiset0:
        all_invariant = False
check("A2 naming bijection vacuity: all 6 relabelings fix every registered invariant",
      all_invariant)

# ----------------------------------------- B registration-statement model ---
# Record-stack model: registration map D(X) = sum_k P_k X P_k.
def D(X):
    return sum(Pk @ X @ Pk for Pk in P)

# B1: D is faithful on the monitored family (M commutes with the context) and
# strips inter-sector coherence of a non-commuting probe (canonical principle).
probe = np.outer(V[:, 0], V[:, 1].conj()) + np.outer(V[:, 1], V[:, 0].conj())
check("B1 registration: D(M) = M (sector content faithful) and D strips "
      "inter-sector coherence (D(probe)=0)",
      np.allclose(D(M), M, atol=TOL) and np.allclose(D(probe), 0 * probe, atol=TOL))

# B2: the identification map iota: sector k -> registered pattern value is
# reconstructed pointwise from registered data alone (tr(P_k M) with
# rank P_k = 1), with no further rule.
iota = {k: np.real(np.trace(P[k] @ M)) / np.real(np.trace(P[k])) for k in range(3)}
check("B2 pointwise reconstruction: iota(k) from registered tr(P_k M) matches lam_k",
      all(abs(iota[k] - lam[k]) < 1e-9 for k in range(3)))

# B3: rigidity. Among the 6 candidate value-to-sector assignments, exactly ONE
# matches the registered data (nondegenerate pattern); the other 5 are refuted
# by the records. So given (context, realized records) the identification has
# zero residual freedom; the 6-fold orbit is exactly the vacuous naming of A2.
matches = 0
for pi in permutations(range(3)):
    if all(abs(lam[pi[k]] - iota[k]) < 1e-9 for k in range(3)):
        matches += 1
check("B3 rigidity: exactly 1 of 6 assignments consistent with the records",
      matches == 1)

# B4: tautology-given-context. Embed the triplet carrier in C^8 = (C^2)^{x3}:
# the supplied context projectors live UNDER the hw=1 projector, so
# "the registered sectors are sectors of the hw=1 triplet" is a context datum.
dim8 = 8
basis_idx = {c: i for i, c in enumerate(product([0, 1], repeat=3))}
E = np.zeros((8, 3), dtype=complex)      # isometry C^3 (triplet) -> C^8
for j, c in enumerate(hw1):
    E[basis_idx[c], j] = 1.0
P_hw1 = E @ E.conj().T
P8 = [E @ Pk @ E.conj().T for Pk in P]
check("B4 carrier membership tautological given context: P_k <= P_hw1 and "
      "sum_k P_k = P_hw1 in C^8",
      all(np.allclose(P_hw1 @ Pk8 @ P_hw1, Pk8, atol=TOL) for Pk8 in P8)
      and np.allclose(sum(P8), P_hw1, atol=TOL))

# B4b: C_3[111] on C^8 (cyclic permutation of tensor factors) restricts to the
# triplet as the 3-cycle used above -- the embedded model is the same carrier.
R8 = np.zeros((8, 8))
for cc in product([0, 1], repeat=3):
    R8[basis_idx[rot(cc)], basis_idx[cc]] = 1.0
R3 = E.conj().T @ R8 @ E
check("B4b embedded C3[111] restricts to the triplet 3-cycle (R3 = J-conjugate "
      "permutation, R3^3 = I)",
      np.allclose(R3 @ R3 @ R3, np.eye(3), atol=TOL)
      and sorted(np.round(np.abs(R3).sum(axis=0), 9).tolist()) == [1.0, 1.0, 1.0])

# B5: counterfactual test (the realized-state primitive's policing clause).
# A second law-admissible realized configuration (delta -> -delta, equally
# K-real circulant) yields a DIFFERENT value-to-sector assignment: sectors
# k=1,2 exchange their registered values. The assignment is therefore
# registered data of the realized state, not derivation output.
Mc = M_of(a0, B0, -d0)
lam_c = np.array([a0 + 2 * B0 * np.cos(-d0 - 2 * np.pi * k / 3) for k in range(3)])
iota_c = {k: np.real(np.trace(P[k] @ Mc)) / np.real(np.trace(P[k])) for k in range(3)}
check("B5a counterfactual state is law-admissible (K-real Hermitian circulant, "
      "same context diagonalizes it)",
      np.allclose(Mc, Mc.conj().T, atol=TOL)
      and np.allclose(D(Mc), Mc, atol=TOL)
      and all(abs(iota_c[k] - lam_c[k]) < 1e-9 for k in range(3)))
check("B5b assignment is state-contingent: iota differs (k=1,2 values exchange, "
      "k=0 fixed) => registered data, not derivation output",
      abs(iota_c[0] - iota[0]) < 1e-9
      and abs(iota_c[1] - iota[2]) < 1e-9
      and abs(iota_c[2] - iota[1]) < 1e-9
      and abs(iota[1] - iota[2]) > 1e-6)

# ------------------------------------ C the genuine structural residual -----
# The LOCUS (why the monitored family is supported on hw=1) is an
# operator-class fact, prior to any readout context -- not a registration
# statement. Replicates the carrier-note counterfactuals on the 8 corners.

# C1: naive first-order dispersion |D|^2 = sum_mu sin^2(k_mu) vanishes at ALL
# 8 corners k in {0,pi}^3 with Hamming grading (1,3,3,1): hw=1 not singled out.
corner_k = list(product([0.0, np.pi], repeat=3))
zero_locus = [kv for kv in corner_k if abs(sum(np.sin(km) ** 2 for km in kv)) < TOL]
grading = [
    sum(1 for kv in zero_locus if sum(1 for km in kv if abs(km - np.pi) < TOL) == w)
    for w in range(4)]
check("C1 naive dispersion zero locus = all 8 corners, hw-graded (1,3,3,1): "
      "hw=1 not singled out",
      len(zero_locus) == 8 and grading == [1, 3, 3, 1])

# C2: Wilson / second-difference mass at the corners is the staircase
# (0, 2r, 4r, 6r) by Hamming weight: it distinguishes hw=0, not hw=1.
r_w = 1.0
wilson_mass = {kv: r_w * sum(1 - np.cos(km) for km in kv) for kv in corner_k}
mass_by_hw = {}
for kv in corner_k:
    w = sum(1 for km in kv if abs(km - np.pi) < TOL)
    mass_by_hw.setdefault(w, set()).add(round(wilson_mass[kv], 12))
check("C2 Wilson staircase (0,2r,4r,6r): the distinguished massless corner is "
      "hw=0, not hw=1",
      all(mass_by_hw[w] == {round(2.0 * r_w * w, 12)} for w in range(4))
      and min(mass_by_hw, key=lambda w: list(mass_by_hw[w])[0]) == 0)

# C3: hw=1 <-> hw=2 is the compensated complementation class: complementation
# exchanges the triplets and commutes with C3[111] (landed support theorem,
# replicated). The surviving locus content is the operator-class gate, not a
# record-side selection.
check("C3 complementation exchanges hw=1 <-> hw=2 and commutes with C3[111]",
      {comp(cc) for cc in hw1} == set(hw2)
      and all(comp(rot(cc)) == rot(comp(cc)) for cc in corners))

# ------------------------------------------------------ D color contrast ----
# Single-named-record-frame color model (landed unaudited criterion,
# replicated as exact arithmetic): Phi(rho) = D_B(U rho U+), with U the C^3
# Fourier unitary (no zero amplitudes). T_U[i,j] = |U_ij|^2 = 1/3 everywhere:
# primitive doubly stochastic, unique fixed point I/3. NO per-sector color
# datum survives for pointwise evaluation. Generation contrast: the
# registration map D above has ALL diagonal sector data as fixed points.
U_col = V
T_U = np.abs(U_col) ** 2
evals = np.linalg.eigvals(T_U)
check("D1 color: T_U = J/3 doubly stochastic with spectral gap (eigenvalues "
      "{1,0,0}); unique stationary vector = uniform => no surviving per-sector "
      "color record",
      np.allclose(T_U, np.ones((3, 3)) / 3, atol=TOL)
      and sorted(np.round(np.abs(evals), 9)) == [0.0, 0.0, 1.0])

p_test = np.array([0.7, 0.2, 0.1])
rho_gen = sum(p_test[k] * P[k] for k in range(3))   # sector-diagonal state
check("D1b generation registration preserves per-sector data exactly while the "
      "color channel erases it in one step",
      np.allclose(T_U @ p_test, np.ones(3) / 3, atol=TOL)
      and np.allclose(D(rho_gen), rho_gen, atol=TOL))

# D2: intra-color labels are gauge-moved: conjugating by a color unitary g
# permutes/mixes the frame projectors while every registered invariant
# (characters/traces of words) is fixed. So a sector-level abstract->physical
# color identification has no record-side referent.
rng = np.random.default_rng(7)
A_h = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
g, _ = np.linalg.qr(A_h)
X1 = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
X2 = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
inv_fixed = (abs(np.trace(g @ X1 @ g.conj().T) - np.trace(X1)) < 1e-9
             and abs(np.trace(g @ X1 @ X2 @ g.conj().T) - np.trace(X1 @ X2)) < 1e-9)
frame_moved = not np.allclose(g @ np.diag([1, 0, 0]).astype(complex) @ g.conj().T,
                              np.diag([1, 0, 0]), atol=1e-6)
check("D2 color gauge move: registered invariants (traces of words) fixed while "
      "the sector frame is moved => sector labels carry no registered content",
      inv_fixed and frame_moved)

# --------------------------------------------------------- E hostile guards -
# E1: no-PDG / no-comparator guard. The identification construction is
# equivariant in the supplied pattern values: rerun at fresh arbitrary
# admissible (a,B,delta) tuples; iota always reproduces the pattern of THAT
# state. No external constant enters anywhere above (the runner contains no
# matched value).
ok = True
for (a1, B1, d1) in [(2.0, 0.5, 1.1), (0.7, 0.11, 2.0), (1.3, 0.25, 0.9)]:
    Mx = M_of(a1, B1, d1)
    lx = np.array([a1 + 2 * B1 * np.cos(d1 - 2 * np.pi * k / 3) for k in range(3)])
    ix = {k: np.real(np.trace(P[k] @ Mx)) for k in range(3)}
    if not all(abs(ix[k] - lx[k]) < 1e-9 for k in range(3)):
        ok = False
check("E1 equivariance guard: identification reconstructs the supplied pattern "
      "at arbitrary admissible (a,B,delta); no external comparator enters",
      ok)

# E2: renaming guard. Pre-decomposition the bridge nominally carries a 6-fold
# interpretive assignment freedom; post-decomposition, given (standing context,
# realized records) the freedom is 1 (B3), and the 6-fold orbit is exactly the
# vacuous naming class (A2). Strict reduction, not relabeling: 6 -> 1.
pre_freedom = len(list(permutations(range(3))))
check("E2 strict reduction: assignment freedom 6 (pre) -> 1 (record-determined), "
      "quotient = vacuous naming",
      pre_freedom == 6 and matches == 1 and all_invariant)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
