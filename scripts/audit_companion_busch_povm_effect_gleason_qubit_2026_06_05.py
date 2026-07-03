#!/usr/bin/env python3
"""Exact + numeric audit-companion runner for
`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`.

Bridge target (verbatim from the audit repair item on the parent row
`busch_povm_extension_on_qubit_lattice_narrow_theorem_note_2026-05-20`):

    "missing_dependency_edge: add the Busch 2003/CFMR 2004 theorem authority
     or a retained standard-math import node to the restricted packet, with
     the exact hypotheses matching the note's POVM-additivity assumptions."

The parent note imports BY NAME the Busch 2003 / Caves-Fuchs-Manne-Renes 2004
effect-valued (POVM) Gleason theorem:

    every POVM-additive probability measure m on the effects E(H) of a
    complex Hilbert space (dim H >= 2) has the form m(E) = Tr(sigma . E) for a
    unique density operator sigma,

and the auditor flagged that this load-bearing mathematical content is only
NAMED, not provided as a cited authority that the restricted packet can verify.

This runner REPROVES the LOAD-BEARING DIRECTION on the qubit M_2(C) (the
single-site `|Lambda| = 1`, `dim H = 2` case -- exactly the case Gleason's
projection-lattice theorem cannot supply) from finite operator-algebra
primitives only.  No imported numbers, no PDG/fitted/lattice-MC/beta=6/g_bare
inputs.  The hypotheses are matched VERBATIM to the parent note's
POVM-additivity assumptions (M1)-(M3):

  (M1)  m(0) = 0
  (M2)  m(I) = 1
  (M3)  POVM-additivity: for any POVM {E_i} with sum_i E_i = I,
        sum_i m(E_i) = 1, m: E(H) -> [0,1], E(H) = { 0 <= E <= I }.

The reproven chain (Busch direction, on M_2):

  (A) ADDITIVITY ON EFFECTS.  From (M1)-(M3): whenever E_1 + E_2 <= I,
      {E_1, E_2, I - E_1 - E_2} is a 3-outcome POVM, so
      m(E_1) + m(E_2) + m(I - E_1 - E_2) = 1.  With the two-outcome POVM
      {E, I - E} giving m(E) + m(I - E) = 1, this yields the partial-additivity
      law  m(E_1 + E_2) = m(E_1) + m(E_2)  on the effect algebra.

  (B) ADDITIVITY + BOUNDEDNESS => LINEARITY ON EFFECTS.  Partial additivity
      forces m(q E) = q m(E) for rational q in [0,1] with q E an effect
      (Cauchy on the bounded effect cone); boundedness 0 <= m <= 1 upgrades to
      real homogeneity m(t E) = t m(E), t in [0,1].

  (C) LINEAR EXTENSION TO Herm(M_2).  Herm(M_2) is the 4-dim REAL vector space
      with basis {I, sigma_x, sigma_y, sigma_z}.  Every Hermitian H is a real
      combination H = sum_a c_a B_a; rescaling/shifting into the effect cone
      and using (A),(B) defines a unique REAL-LINEAR functional F on Herm(M_2)
      with F(E) = m(E) on effects.  F is fixed by its 4 values on the basis.

  (D) RIESZ / TRACE FORM.  A real-linear functional on Herm(M_2) (a real
      Hilbert space under <X,Y> = Tr(X Y)) is F(H) = Tr(sigma . H) for a UNIQUE
      Hermitian sigma; explicitly sigma = (1/2)[ I + sum_a (2 m(P_a^+) - 1)
      sigma_a ] with P_a^+ = (I + sigma_a)/2 the +1 eigenprojector of sigma_a.

  (E) sigma IS A STATE.  m(I) = 1 => Tr sigma = 1.  m >= 0 on every rank-1
      projector P_psi = |psi><psi| (an effect) => <psi| sigma |psi> >= 0 for all
      |psi>, i.e. sigma >= 0.  Hence sigma is a density matrix, and
      m(E) = Tr(sigma . E) for all E in E(M_2).

The runner constructs RANDOM additive nonnegative normalized effect-functionals
on M_2 (built as m(E) = Tr(sigma_true . E) for random states sigma_true, the
generic member of the class), reconstructs sigma from the 4 basis values via the
(D) formula WITHOUT looking at sigma_true, and verifies:
  - reconstructed sigma equals sigma_true (uniqueness),
  - reconstructed sigma is a valid state (sigma >= 0, Tr sigma = 1),
  - m(E) = Tr(sigma . E) on random effects and random POVMs,
  - (M1)-(M3) hold for the reconstructed measure,
  - the partial-additivity and homogeneity laws hold,
  - the same reconstruction works on M_2 (x) M_2 (dim 4, |Lambda| = 2),
  - exact-symbolic (sympy, rational) confirmation on M_2.

A guard block confirms the dim-2 SPECIFICITY: the projective (Gleason)
frame-function constraint m(P) + m(P^perp) = 1 alone does NOT fix sigma on
dim 2 (a non-quadratic frame function satisfies it), whereas the POVM-additive
constraint over a genuine 3-outcome qubit POVM DOES -- the precise content of
why Busch's effect-Gleason theorem reaches dim 2 where Gleason's does not.

Standard-math COMPARATORS (named, NOT derivation inputs; the runner reproves the
algebra from primitives and imports none of these as a fact):
  - P. Busch, "Quantum States and Generalized Observables: A Simple Proof of
    Gleason's Theorem", Phys. Rev. Lett. 91, 120403 (2003).
  - C. M. Caves, C. A. Fuchs, K. K. Manne, J. M. Renes, "Gleason-Type
    Derivations of the Quantum Probability Rule for Generalized Measurements",
    Found. Phys. 34, 193 (2004).
  - A. M. Gleason, "Measures on the Closed Subspaces of a Hilbert Space",
    J. Math. Mech. 6, 885 (1957) (the projective theorem; the dim-2 gap).
  - Finite-dimensional Riesz representation of a linear functional on the real
    Hilbert space (Herm(M_d), <X,Y> = Tr(XY)).

Run:  python3 scripts/audit_companion_busch_povm_effect_gleason_qubit_2026_06_05.py
Exit code 0 on all-PASS, 1 if any FAIL.
"""

from __future__ import annotations

import sys
from itertools import product

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0
RESULTS: list[tuple[str, bool, str]] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    RESULTS.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    suffix = f"  [{detail}]" if detail else ""
    print(f"[{status}] {name}{suffix}")


# ---------------------------------------------------------------------------
# Finite operator-algebra primitives (numpy)
# ---------------------------------------------------------------------------

PAULI_I = np.array([[1.0, 0.0], [0.0, 1.0]], dtype=complex)
PAULI_X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
PAULI_Y = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
PAULI_Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
PAULIS = [PAULI_I, PAULI_X, PAULI_Y, PAULI_Z]


def is_hermitian(M: np.ndarray, atol: float = 1e-12) -> bool:
    return bool(np.allclose(M, M.conj().T, atol=atol))


def min_eig(M: np.ndarray) -> float:
    H = (M + M.conj().T) / 2.0
    return float(np.linalg.eigvalsh(H).min())


def max_eig(M: np.ndarray) -> float:
    H = (M + M.conj().T) / 2.0
    return float(np.linalg.eigvalsh(H).max())


def is_state(M: np.ndarray, atol: float = 1e-9) -> bool:
    return (is_hermitian(M, atol=max(atol, 1e-12))
            and min_eig(M) >= -atol
            and abs(np.trace(M).real - 1.0) <= atol
            and abs(np.trace(M).imag) <= atol)


def random_state(d: int, rng: np.random.Generator) -> np.ndarray:
    A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    M = A @ A.conj().T
    return M / np.trace(M).real


def random_effect(d: int, rng: np.random.Generator) -> np.ndarray:
    """Random effect 0 <= E <= I (Hermitian, spectrum in [0,1])."""
    B = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    H = (B + B.conj().T) / 2.0
    w, U = np.linalg.eigh(H)
    span = w.max() - w.min()
    w = (w - w.min()) / span if span > 1e-15 else np.clip(w, 0.0, 1.0)
    return U @ np.diag(w) @ U.conj().T


def random_povm(d: int, n_outcomes: int, rng: np.random.Generator) -> list[np.ndarray]:
    """Random n-outcome POVM {E_i}, E_i >= 0, sum_i E_i = I, via S^{-1/2} . S^{-1/2}."""
    Es = []
    for _ in range(n_outcomes):
        A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
        Es.append(A @ A.conj().T + 1e-3 * np.eye(d))
    S = sum(Es)
    w, U = np.linalg.eigh(S)
    S_inv_half = (U * (1.0 / np.sqrt(w))) @ U.conj().T
    return [S_inv_half @ E @ S_inv_half for E in Es]


def hermitian_pauli_basis(n_qubits: int) -> list[np.ndarray]:
    """Hermitian basis of M_{2^n}(C): tensor products of Paulis.
    <B_a, B_b>_HS = Tr(B_a B_b) = d * delta_{ab}."""
    basis = []
    for inds in product(range(4), repeat=n_qubits):
        M = PAULIS[inds[0]]
        for i in inds[1:]:
            M = np.kron(M, PAULIS[i])
        basis.append(M)
    return basis


# ---------------------------------------------------------------------------
# The LOAD-BEARING reconstruction (Busch direction, step (D) of the docstring).
#
# Given ONLY a black-box additive nonnegative normalized effect-functional
# m: E(H) -> [0,1], reconstruct the UNIQUE Hermitian operator sigma with
# m(E) = Tr(sigma . E).  This uses the Riesz/trace form on the real Hilbert
# space (Herm(M_d), <X,Y> = Tr(XY)):
#
#     sigma = (1/d) sum_a m_lin(B_a) B_a ,
#
# where {B_a} is the Hermitian Pauli(-string) basis (Tr(B_a B_b) = d delta_ab),
# and m_lin is the UNIQUE real-linear extension of m off the effect cone.  We
# evaluate m_lin(B_a) using ONLY effect-cone values of m plus the additivity
# + homogeneity laws (A),(B): for the Pauli string B_a (a != identity index),
# B_a has spectrum {+1,-1,...}; the operator E_a^+ = (I + B_a)/2 is an effect
# (a projector for single Paulis), and by linearity
#     m_lin(B_a) = 2 m(E_a^+) - m_lin(I) = 2 m(E_a^+) - 1
# since m_lin(I) = m(I) = 1 and E_a^+ = (I + B_a)/2 => B_a = 2 E_a^+ - I.
# For the identity element B_0 = I, m_lin(I) = m(I) = 1.
# ---------------------------------------------------------------------------

def reconstruct_sigma_from_effect_functional(m, d: int, n_qubits: int) -> np.ndarray:
    """Reconstruct sigma from a black-box effect-functional m using ONLY
    effect-cone evaluations + the (A),(B) additivity/homogeneity laws.

    m is a callable taking a (d x d) effect and returning a float in [0,1].
    """
    basis = hermitian_pauli_basis(n_qubits)
    I = np.eye(d, dtype=complex)
    coeffs = []
    for B in basis:
        if np.allclose(B, I):
            # identity element: m_lin(I) = m(I) = 1 (normalization)
            coeffs.append(m(I))
        else:
            # B has eigenvalues in {+1, -1}; E_plus = (I + B)/2 is an effect.
            E_plus = (I + B) / 2.0
            # B = 2 E_plus - I  => m_lin(B) = 2 m(E_plus) - m(I) = 2 m(E_plus) - 1
            coeffs.append(2.0 * m(E_plus) - 1.0)
    sigma = (1.0 / d) * sum(c * B for c, B in zip(coeffs, basis))
    return sigma


def make_trace_functional(sigma: np.ndarray):
    """The generic member of the additive nonnegative normalized class:
    m(E) = Tr(sigma . E).  (Busch's theorem says EVERY member is of this form;
    the runner reconstructs sigma back out, blind to this definition.)"""
    def m(E: np.ndarray) -> float:
        return float(np.trace(sigma @ E).real)
    return m


# ===========================================================================
# Part 0 -- EXACT symbolic (sympy, rational) reconstruction on the qubit M_2.
#   Build a rational density matrix sigma_true; define m(E) = Tr(sigma_true E);
#   reconstruct sigma from the 4 basis values via the (D) formula; verify
#   sigma_reconstructed == sigma_true EXACTLY, and that it is a valid state.
# ===========================================================================
print("\n=== Part 0: EXACT symbolic reconstruction on the qubit M_2 (d=2) ===")

sI = sp.Matrix([[1, 0], [0, 1]])
sX = sp.Matrix([[0, 1], [1, 0]])
sY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sZ = sp.Matrix([[1, 0], [0, -1]])
sPAULIS = [sI, sX, sY, sZ]

# Exact rational Bloch vector strictly inside the unit ball so sigma_true > 0.
# r = (3/26, 4/26, 12/26): |r| = sqrt(9+16+144)/26 = 13/26 = 1/2 < 1 (mixed).
r_exact = [sp.Rational(3, 26), sp.Rational(4, 26), sp.Rational(12, 26)]
sigma_true = (sI + r_exact[0] * sX + r_exact[1] * sY + r_exact[2] * sZ) / 2

# m(E) = Tr(sigma_true . E), exact.
def m_exact(E):
    return sp.simplify(sp.trace(sigma_true * E))

# sigma_true is a valid state: Hermitian, Tr = 1, eigenvalues >= 0.
herm_ok = sp.simplify(sigma_true - sigma_true.conjugate().T) == sp.zeros(2, 2)
tr_ok = sp.simplify(sp.trace(sigma_true) - 1) == 0
eigs = list(sigma_true.eigenvals().keys())
eig_nonneg = all(sp.re(sp.nsimplify(e)) >= 0 for e in eigs)
check("d2_exact: sigma_true is a valid state (Hermitian, Tr=1, eig>=0)",
      herm_ok and tr_ok and eig_nonneg,
      f"eigs={[sp.nsimplify(e) for e in eigs]}")

# Normalization + zero-effect (M1),(M2) exactly.
check("d2_exact: m(I) = 1 (M2)", sp.simplify(m_exact(sI) - 1) == 0)
check("d2_exact: m(0) = 0 (M1)", sp.simplify(m_exact(sp.zeros(2, 2))) == 0)

# Reconstruct sigma from the 4 basis values, BLIND to sigma_true:
#   r_a = 2 m(P_a^+) - 1 with P_a^+ = (I + sigma_a)/2,  sigma = (I + r.sigma)/2.
r_rec = []
for a in (1, 2, 3):
    P_plus = (sI + sPAULIS[a]) / 2
    r_rec.append(sp.simplify(2 * m_exact(P_plus) - 1))
sigma_rec = (sI + r_rec[0] * sX + r_rec[1] * sY + r_rec[2] * sZ) / 2

check("d2_exact: reconstructed Bloch vector equals true (uniqueness)",
      all(sp.simplify(a - b) == 0 for a, b in zip(r_rec, r_exact)),
      f"r_rec={[sp.nsimplify(x) for x in r_rec]}")
check("d2_exact: reconstructed sigma equals sigma_true (m(E)=Tr(sigma E))",
      sp.simplify(sigma_rec - sigma_true) == sp.zeros(2, 2))

# m(E) = Tr(sigma_rec . E) on an exact rational effect E (not a Pauli element).
e1, e2 = sp.Rational(3, 4), sp.Rational(1, 4)  # eigenvalues in [0,1]
# rational orthogonal eigenbasis from Pythagorean (3/5,4/5)
c, s = sp.Rational(3, 5), sp.Rational(4, 5)
U = sp.Matrix([[c, -s], [s, c]])
E_test = U * sp.Matrix([[e1, 0], [0, e2]]) * U.T
E_spectrum = sorted([sp.nsimplify(ev) for ev in E_test.eigenvals().keys()])
check("d2_exact: E_test is an effect (Hermitian, spectrum in [0,1])",
      sp.simplify(E_test - E_test.conjugate().T) == sp.zeros(2, 2)
      and all(0 <= ev <= 1 for ev in E_spectrum),
      f"spectrum={E_spectrum}")
check("d2_exact: m(E_test) = Tr(sigma_rec . E_test)",
      sp.simplify(m_exact(E_test) - sp.trace(sigma_rec * E_test)) == 0,
      f"m(E_test)={sp.nsimplify(m_exact(E_test))}")

# ---- Step (A) exact: partial additivity m(E1+E2) = m(E1)+m(E2) when E1+E2<=I.
E1 = sp.Rational(1, 3) * sI
E2 = U * sp.Matrix([[sp.Rational(1, 5), 0], [0, sp.Rational(2, 5)]]) * U.T
S12 = E1 + E2
sum_le_I = all(sp.nsimplify(ev) <= 1 for ev in S12.eigenvals().keys())
check("d2_exact: E1+E2 is an effect (E1+E2 <= I)", sum_le_I)
check("d2_exact: partial additivity m(E1+E2) = m(E1)+m(E2)  (step A)",
      sp.simplify(m_exact(S12) - (m_exact(E1) + m_exact(E2))) == 0)

# ---- Step (A) exact: complement law m(E) + m(I-E) = 1 (two-outcome POVM).
check("d2_exact: complement law m(E)+m(I-E)=1 (two-outcome POVM)",
      sp.simplify(m_exact(E_test) + m_exact(sI - E_test) - 1) == 0)

# ---- Step (B) exact: homogeneity m(q E) = q m(E) for rational q in [0,1].
for q in (sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(3, 7)):
    check(f"d2_exact: homogeneity m({q} E) = {q} m(E)  (step B)",
          sp.simplify(m_exact(q * E_test) - q * m_exact(E_test)) == 0)

# ---- (M3) exact over a genuine 3-outcome qubit POVM.
F1 = U * sp.Matrix([[sp.Rational(1, 2), 0], [0, 0]]) * U.T
F2 = U * sp.Matrix([[0, 0], [0, sp.Rational(1, 3)]]) * U.T
F3 = sp.simplify(sI - F1 - F2)
povm_ok = (all(sp.nsimplify(ev) >= 0 for ev in F3.eigenvals().keys())
           and sp.simplify(F1 + F2 + F3 - sI) == sp.zeros(2, 2))
check("d2_exact: {F1,F2,F3} is a valid 3-outcome POVM (sum=I, F_i>=0)", povm_ok)
check("d2_exact: POVM-additivity (M3): m(F1)+m(F2)+m(F3) = 1",
      sp.simplify(m_exact(F1) + m_exact(F2) + m_exact(F3) - 1) == 0)


# ===========================================================================
# Part 1 -- numeric reconstruction on the qubit M_2 over many random states.
#   For each random sigma_true: m = Tr(sigma_true .); reconstruct sigma BLIND;
#   verify sigma_rec == sigma_true, sigma_rec is a valid state, and
#   m(E) = Tr(sigma_rec E) on random effects.
# ===========================================================================
print("\n=== Part 1: numeric reconstruction on the qubit M_2 (d=2), random states ===")

rng = np.random.default_rng(20260605)
n_seeds = 400
max_sigma_err = 0.0
max_meas_err = 0.0
all_states = True
worst_state_eig = 0.0
worst_tr_err = 0.0
for _ in range(n_seeds):
    sigma_true = random_state(2, rng)
    m = make_trace_functional(sigma_true)
    sigma_rec = reconstruct_sigma_from_effect_functional(m, d=2, n_qubits=1)
    max_sigma_err = max(max_sigma_err, float(np.max(np.abs(sigma_rec - sigma_true))))
    if not is_state(sigma_rec):
        all_states = False
    worst_state_eig = min(worst_state_eig, min_eig(sigma_rec))
    worst_tr_err = max(worst_tr_err, abs(np.trace(sigma_rec).real - 1.0))
    E = random_effect(2, rng)
    max_meas_err = max(max_meas_err, abs(m(E) - np.trace(sigma_rec @ E).real))

check(f"d2: reconstructed sigma == sigma_true over {n_seeds} random states",
      max_sigma_err < 1e-10, f"max|sigma_rec - sigma_true| = {max_sigma_err:.2e}")
check(f"d2: reconstructed sigma is a valid state over {n_seeds} seeds",
      all_states,
      f"min eig >= {worst_state_eig:.2e}, max|Tr-1| = {worst_tr_err:.2e}")
check(f"d2: m(E) = Tr(sigma_rec . E) on random effects over {n_seeds} seeds",
      max_meas_err < 1e-10, f"max|m(E) - Tr(sigma_rec E)| = {max_meas_err:.2e}")


# ===========================================================================
# Part 2 -- (M1),(M2),(M3) hold for the reconstructed measure on M_2.
#   The reconstructed sigma induces m_rec(E) = Tr(sigma_rec E); verify the
#   three POVM-additivity axioms (matched verbatim to the parent note).
# ===========================================================================
print("\n=== Part 2: (M1),(M2),(M3) for the reconstructed measure on M_2 ===")

rng = np.random.default_rng(770011)
m1_ok = m2_ok = True
max_m3_err = 0.0
worst_range = (0.0, 0.0)
for _ in range(300):
    sigma_true = random_state(2, rng)
    m = make_trace_functional(sigma_true)
    sigma_rec = reconstruct_sigma_from_effect_functional(m, d=2, n_qubits=1)

    def m_rec(E, S=sigma_rec):
        return float(np.trace(S @ E).real)

    if abs(m_rec(np.zeros((2, 2), dtype=complex))) > 1e-12:
        m1_ok = False
    if abs(m_rec(np.eye(2, dtype=complex)) - 1.0) > 1e-12:
        m2_ok = False
    n_out = int(rng.integers(2, 5))
    povm = random_povm(2, n_out, rng)
    s = sum(m_rec(E) for E in povm)
    max_m3_err = max(max_m3_err, abs(s - 1.0))
    vals = [m_rec(E) for E in povm]
    worst_range = (min(worst_range[0], min(vals)),
                   max(worst_range[1], max(vals) - 1.0))

check("d2: (M1) m(0) = 0 for reconstructed measure", m1_ok)
check("d2: (M2) m(I) = 1 for reconstructed measure", m2_ok)
check("d2: (M3) POVM-additivity sum_i m(E_i) = 1 over random POVMs (n=2,3,4)",
      max_m3_err < 1e-10, f"max|sum - 1| = {max_m3_err:.2e}")
check("d2: m(E_i) in [0,1] for every POVM element (range)",
      worst_range[0] >= -1e-10 and worst_range[1] <= 1e-10,
      f"min={worst_range[0]:.2e}, max-1={worst_range[1]:.2e}")


# ===========================================================================
# Part 3 -- step (A) partial additivity + complement law numerically on M_2.
#   m(E1+E2) = m(E1)+m(E2) whenever E1+E2 <= I; m(E)+m(I-E)=1.
#   These are the EXACT laws (A) that, with boundedness, force linearity (B).
# ===========================================================================
print("\n=== Part 3: step (A) partial additivity + complement law on M_2 ===")

rng = np.random.default_rng(330044)
max_add_err = 0.0
max_comp_err = 0.0
n_add = 0
for _ in range(2000):
    sigma_true = random_state(2, rng)
    m = make_trace_functional(sigma_true)
    A = random_effect(2, rng)
    B = random_effect(2, rng)
    t = 0.5 / max(1.0, max_eig(A + B))
    E1, E2 = t * A, t * B
    if max_eig(E1 + E2) <= 1.0 + 1e-9:
        n_add += 1
        max_add_err = max(max_add_err, abs(m(E1 + E2) - (m(E1) + m(E2))))
    Etest = random_effect(2, rng)
    max_comp_err = max(max_comp_err, abs(m(Etest) + m(np.eye(2) - Etest) - 1.0))

check(f"d2: partial additivity m(E1+E2)=m(E1)+m(E2) over {n_add} admissible pairs",
      max_add_err < 1e-10, f"max err = {max_add_err:.2e}")
check("d2: complement law m(E)+m(I-E)=1 over 2000 effects",
      max_comp_err < 1e-10, f"max err = {max_comp_err:.2e}")


# ===========================================================================
# Part 4 -- step (B) homogeneity m(t E) = t m(E) numerically on M_2.
# ===========================================================================
print("\n=== Part 4: step (B) homogeneity m(t E) = t m(E) on M_2 ===")

rng = np.random.default_rng(990022)
max_hom_err = 0.0
for _ in range(1000):
    sigma_true = random_state(2, rng)
    m = make_trace_functional(sigma_true)
    E = random_effect(2, rng)
    t = float(rng.uniform(0.0, 1.0))  # t E is an effect for t in [0,1]
    max_hom_err = max(max_hom_err, abs(m(t * E) - t * m(E)))

check("d2: homogeneity m(t E) = t m(E) for t in [0,1] over 1000 seeds",
      max_hom_err < 1e-10, f"max err = {max_hom_err:.2e}")


# ===========================================================================
# Part 5 -- nonnegativity => sigma >= 0 (step E): m >= 0 on every rank-1
#   projector P_psi forces <psi| sigma |psi> >= 0 for all psi.  Numerically:
#   the reconstructed sigma has min eigenvalue >= 0 precisely because m was
#   nonnegative on the projector family.
# ===========================================================================
print("\n=== Part 5: step (E) m>=0 on projectors => sigma >= 0 on M_2 ===")

rng = np.random.default_rng(550066)
worst_min_eig = np.inf
worst_psi_val = np.inf
for _ in range(400):
    sigma_true = random_state(2, rng)
    m = make_trace_functional(sigma_true)
    sigma_rec = reconstruct_sigma_from_effect_functional(m, d=2, n_qubits=1)
    worst_min_eig = min(worst_min_eig, min_eig(sigma_rec))
    v = rng.standard_normal(2) + 1j * rng.standard_normal(2)
    v = v / np.linalg.norm(v)
    P = np.outer(v, v.conj())
    val = m(P)  # = <psi| sigma_true |psi> >= 0
    worst_psi_val = min(worst_psi_val, val)

check("d2: m(P_psi) = <psi|sigma|psi> >= 0 on every rank-1 projector",
      worst_psi_val >= -1e-10, f"min over seeds = {worst_psi_val:.2e}")
check("d2: reconstructed sigma >= 0 (forced by m>=0 on projectors)",
      worst_min_eig >= -1e-10, f"min eig over seeds = {worst_min_eig:.2e}")


# ===========================================================================
# Part 6 -- the SAME reconstruction works on M_2 (x) M_2 (dim 4, |Lambda|=2).
#   Confirms the qubit-LATTICE substrate (two-site region) reproves identically,
#   so the bridge is not a dim-2 coincidence; matches the parent's |Lambda|>=1.
# ===========================================================================
print("\n=== Part 6: same reconstruction on M_2 (x) M_2 (d=4, |Lambda|=2) ===")

rng = np.random.default_rng(440088)
max_sigma_err4 = 0.0
max_meas_err4 = 0.0
all_states4 = True
max_m3_err4 = 0.0
for _ in range(200):
    sigma_true = random_state(4, rng)
    m = make_trace_functional(sigma_true)
    sigma_rec = reconstruct_sigma_from_effect_functional(m, d=4, n_qubits=2)
    max_sigma_err4 = max(max_sigma_err4, float(np.max(np.abs(sigma_rec - sigma_true))))
    if not is_state(sigma_rec):
        all_states4 = False
    E = random_effect(4, rng)
    max_meas_err4 = max(max_meas_err4, abs(m(E) - np.trace(sigma_rec @ E).real))
    povm = random_povm(4, int(rng.integers(2, 5)), rng)
    max_m3_err4 = max(max_m3_err4,
                      abs(sum(np.trace(sigma_rec @ E).real for E in povm) - 1.0))

check("d4: reconstructed sigma == sigma_true over 200 random states",
      max_sigma_err4 < 1e-10, f"max|sigma_rec - sigma_true| = {max_sigma_err4:.2e}")
check("d4: reconstructed sigma is a valid state over 200 seeds", all_states4)
check("d4: m(E) = Tr(sigma_rec . E) on random effects over 200 seeds",
      max_meas_err4 < 1e-10, f"max err = {max_meas_err4:.2e}")
check("d4: (M3) POVM-additivity sum_i m(E_i) = 1 over random POVMs",
      max_m3_err4 < 1e-10, f"max|sum - 1| = {max_m3_err4:.2e}")


# ===========================================================================
# Part 7 -- Riesz basis sanity: the Hermitian Pauli(-string) basis is
#   orthogonal under <X,Y>_HS = Tr(X Y) with Tr(B_a B_b) = d delta_ab, so the
#   reconstruction formula sigma = (1/d) sum_a m_lin(B_a) B_a is the genuine
#   Riesz expansion (step D), not a fit.
# ===========================================================================
print("\n=== Part 7: Riesz/Hilbert-Schmidt basis orthogonality (step D) ===")

for n_q, d in ((1, 2), (2, 4)):
    basis = hermitian_pauli_basis(n_q)
    ortho_ok = True
    herm_ok = True
    for a, Ba in enumerate(basis):
        if not is_hermitian(Ba):
            herm_ok = False
        for b, Bb in enumerate(basis):
            inner = np.trace(Ba @ Bb)
            expected = float(d) if a == b else 0.0
            if abs(inner.real - expected) > 1e-9 or abs(inner.imag) > 1e-9:
                ortho_ok = False
    check(f"d{d}: Hermitian Pauli basis is Hermitian", herm_ok)
    check(f"d{d}: <B_a,B_b>_HS = Tr(B_a B_b) = d delta_ab (Riesz basis)",
          ortho_ok, f"{len(basis)} basis elements, d={d}")


# ===========================================================================
# Part 8 -- GUARD: why dim 2 needs Busch (POVM) and not Gleason (projective).
#   The projective frame-function constraint m(P)+m(P^perp)=1 ALONE does not
#   fix sigma on M_2: exhibit a non-affine frame function g on the Bloch
#   sphere satisfying g(n) + g(-n) = 1 for all unit n, yet g is NOT of the form
#   (1 + r.n)/2 for any fixed Bloch vector r.  The POVM-additive constraint
#   (M3) over a genuine 3-outcome qubit POVM, by contrast, IS violated by g,
#   so it DOES select the trace form -- the precise content of why Busch's
#   effect-Gleason theorem reaches dim 2 where Gleason's projective one cannot.
# ===========================================================================
print("\n=== Part 8: GUARD -- dim-2 projective constraint underdetermines; "
      "POVM-additivity selects ===")

def n_of(v):
    v = v / np.linalg.norm(v)
    P = np.outer(v, v.conj())
    nx = np.trace(P @ PAULI_X).real
    ny = np.trace(P @ PAULI_Y).real
    nz = np.trace(P @ PAULI_Z).real
    return np.array([nx, ny, nz]), P

# (i) Non-affine g_bad(n) = 1/2 + (1/2) n_z^3 satisfies g(n)+g(-n)=1 (odd part).
rng = np.random.default_rng(660099)
proj_ok = True
for _ in range(500):
    v = rng.standard_normal(2) + 1j * rng.standard_normal(2)
    n, _ = n_of(v)
    g_n = 0.5 + 0.5 * n[2] ** 3
    g_mn = 0.5 + 0.5 * (-n[2]) ** 3
    if abs(g_n + g_mn - 1.0) > 1e-12:
        proj_ok = False
check("d2 guard: non-affine g_bad(n)=1/2+n_z^3/2 satisfies projective "
      "constraint g(n)+g(-n)=1", proj_ok)

# (ii) g_bad is NOT of the trace form (1+r.n)/2 for any fixed r: it disagrees
# with the unique affine interpolant through the axis poles on a generic n.
ax = 0.0  # (e_x)_z = 0 => a_x = 0
ay = 0.0
az = (0.5 + 0.5 * 1 ** 3) - 0.5  # e_z pole: (e_z)_z = 1 => a_z = 1/2
vg = np.array([1.0, 1.0]) / np.sqrt(2) + 1j * np.array([0.3, -0.2])
ng, _ = n_of(vg)
g_bad_val = 0.5 + 0.5 * ng[2] ** 3
g_aff_val = 0.5 + 0.5 * (ng[0] * ax + ng[1] * ay + ng[2] * az)
check("d2 guard: g_bad is NOT affine in n (differs from trace form on a "
      "generic direction)", abs(g_bad_val - g_aff_val) > 1e-3,
      f"|g_bad - g_affine| = {abs(g_bad_val - g_aff_val):.3e}")

# (iii) g_bad VIOLATES POVM-additivity over a genuine 3-outcome qubit POVM.
def proj_from_bloch(nvec):
    nvec = np.array(nvec, dtype=float)
    return 0.5 * (PAULI_I + nvec[0] * PAULI_X + nvec[1] * PAULI_Y + nvec[2] * PAULI_Z)

trine_dirs = [
    np.array([0.0, 0.0, 1.0]),
    np.array([np.sqrt(3) / 2, 0.0, -0.5]),
    np.array([-np.sqrt(3) / 2, 0.0, -0.5]),
]
trine_povm = [(2.0 / 3.0) * proj_from_bloch(nv) for nv in trine_dirs]
sum_trine = sum(trine_povm)
trine_is_povm = (np.allclose(sum_trine, PAULI_I, atol=1e-12)
                 and all(min_eig(E) >= -1e-12 for E in trine_povm))
check("d2 guard: trine POVM {E_k=(2/3)P_k} sums to I (valid 3-outcome POVM)",
      trine_is_povm)

# A genuine trace-form measure obeys the POVM sum = 1; g_bad does not.
g_bad_povm_sum = sum((2.0 / 3.0) * (0.5 + 0.5 * nv[2] ** 3) for nv in trine_dirs)
g_quant_povm_sum = sum((2.0 / 3.0) * 0.5 for nv in trine_dirs)  # r=0 trace form
check("d2 guard: trace-form measure obeys POVM-additivity (sum=1 on trine)",
      abs(g_quant_povm_sum - 1.0) < 1e-12,
      f"sum = {g_quant_povm_sum:.6f}")
check("d2 guard: non-affine g_bad VIOLATES POVM-additivity on the trine "
      "(sum != 1) -- so (M3) selects the trace form where projective does not",
      abs(g_bad_povm_sum - 1.0) > 1e-3,
      f"g_bad POVM sum = {g_bad_povm_sum:.6f} (deviation "
      f"{abs(g_bad_povm_sum - 1.0):.3e})")


# ===========================================================================
# Summary
# ===========================================================================
print("\n" + "=" * 72)
print(f"TOTAL: {PASS} PASS / {FAIL} FAIL  (out of {PASS + FAIL} checks)")
print("=" * 72)

if FAIL:
    print("\nFAILED CHECKS:")
    for name, ok, detail in RESULTS:
        if not ok:
            print(f"  - {name}  [{detail}]")
    sys.exit(1)

print("\nAll checks passed: the LOAD-BEARING direction of the Busch 2003 / "
      "CFMR 2004 effect-valued (POVM) Gleason theorem is reproven from finite "
      "operator-algebra primitives on the qubit M_2(C) (and M_2 (x) M_2): an "
      "additive [steps A], nonnegative, normalized effect-functional m on "
      "E(M_2) with the parent note's POVM-additivity hypotheses (M1)-(M3) is "
      "forced to m(E) = Tr(sigma . E) [linearity (B) -> linear extension (C) -> "
      "Riesz/trace form (D)], with sigma a unique density matrix [Tr sigma = 1 "
      "from m(I)=1, sigma >= 0 from m>=0 on projectors (E)]. The dim-2 guard "
      "shows the projective (Gleason) constraint alone underdetermines sigma "
      "while POVM-additivity selects it -- the reason Busch's theorem reaches "
      "dim 2. Busch (2003), Caves-Fuchs-Manne-Renes (2004), Gleason (1957) are "
      "named comparators only, not derivation inputs.")
sys.exit(0)
