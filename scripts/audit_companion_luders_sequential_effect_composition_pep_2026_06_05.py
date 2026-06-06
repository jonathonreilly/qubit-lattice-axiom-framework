#!/usr/bin/env python3
"""Exact + numeric conditional finite-matrix runner for
`LUDERS_SEQUENTIAL_EFFECT_COMPOSITION_PEP_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`.

This companion checks the narrow algebraic statement left after the source note
is scoped honestly:

  * assume a finite matrix algebra `M_d(C)`;
  * assume an orthogonal projection `P`, effect `E`, density operator `rho`,
    and `Tr(rho P) > 0`;
  * assume the Lueders update `rho -> P rho P / Tr(P rho P)`;
  * assume the trace/effect pairing `(rho, E) -> Tr(rho E)`.

Under those supplied measurement-side premises, the runner verifies:

  (a) CONDITIONAL SEQUENTIAL COMPOSITION.  The two-step probability satisfies

          Tr((P rho P / Tr(P rho P)) E) = Tr(rho P E P) / Tr(rho P),

      so the pre-update effect paired against `rho` is `M_{P,E} = P E P`.
      The identity is checked exactly with sympy and numerically with numpy for
      d = 2,3,4.

  (b) VALID-EFFECT PROPERTIES.  `P E P` is positive and
      `0 <= P E P <= P <= I`, so it is a legitimate effect supported on the
      range of `P`:
        - `P E P >= 0`;
        - `P - P E P = P (I - E) P >= 0`;
        - `P <= I` for any orthogonal projection.

  (c) SUPPLIED TRACE/EFFECT PAIRING SUPPORT CHECKS.  The map
      `rho -> Tr(rho E)` is real-linear, and on states/effects takes values in
      `[0,1]`.

  (d) ASSOCIATIVE-COMPATIBILITY.  For projections `P, Q` and effect `F`,
      the supplied sequential product satisfies
      `P (Q F Q) P = (QP)† F (QP)`, matching the parent matrix composition
      expression.

Standard-math comparators, named as parallel context only:
  - G. Lueders, "Ueber die Zustandsaenderung durch den Messprozess",
    Ann. Phys. (Leipzig) 8, 322 (1951);
  - P. Busch, P. Lahti, P. Mittelstaedt, "The Quantum Theory of Measurement",
    Springer (2nd ed. 1996);
  - S. Gudder & R. Greechie, "Sequential products on effect algebras",
    Rep. Math. Phys. 49, 87 (2002).

Companion role: not a new claim row beyond the bridge source note. This runner
does not establish the Lueders update, Born rule, or trace/effect pairing as
framework-native consequences; it checks the finite algebra that follows once
those premises are supplied.

Run:  python3 scripts/audit_companion_luders_sequential_effect_composition_pep_2026_06_05.py
Exit code 0 on all-PASS, 1 if any FAIL.
"""

from __future__ import annotations

import sys

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
# Numeric helpers (finite matrix hypotheses)
# ---------------------------------------------------------------------------

def is_hermitian(M: np.ndarray, atol: float = 1e-12) -> bool:
    return bool(np.allclose(M, M.conj().T, atol=atol))


def min_eig(M: np.ndarray) -> float:
    H = (M + M.conj().T) / 2.0
    return float(np.linalg.eigvalsh(H).min())


def is_psd(M: np.ndarray, atol: float = 1e-9) -> bool:
    return is_hermitian(M, atol=max(atol, 1e-12)) and min_eig(M) >= -atol


def random_density(d: int, rng: np.random.Generator) -> np.ndarray:
    A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    M = A @ A.conj().T
    return M / np.trace(M).real


def random_projection(d: int, rng: np.random.Generator) -> np.ndarray:
    """Random orthogonal projection of random rank r in {1,...,d}."""
    A = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    Q, _ = np.linalg.qr(A)
    r = int(rng.integers(1, d + 1))
    V = Q[:, :r]
    return V @ V.conj().T


def random_effect(d: int, rng: np.random.Generator) -> np.ndarray:
    """Random effect 0 <= E <= I (Hermitian, spectrum in [0,1])."""
    B = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))
    H = (B + B.conj().T) / 2.0
    w, U = np.linalg.eigh(H)
    span = w.max() - w.min()
    w = (w - w.min()) / span if span > 1e-15 else np.clip(w, 0.0, 1.0)
    return U @ np.diag(w) @ U.conj().T


# ===========================================================================
# Part 0 -- exact symbolic qubit instance (d = 2): M_{P,E} = P E P under
#           supplied Lueders update + supplied trace/effect pairing.
# ===========================================================================
print("\n=== Part 0: exact symbolic d=2 -- supplied two-step prob = "
      "Tr(rho PEP)/Tr(rho P) => M_{P,E} = P E P ===")

# Rank-1 qubit projection P = |psi><psi| with |psi> an EXACT rational unit
# vector (Pythagorean (3/5, 4/5)) so every matrix entry is an exact rational
# and all positivity/eigenvalue comparisons are decidable in sympy.  An exact
# effect E = U diag(e1,e2) U† with 0 <= e1,e2 <= 1 uses an exact rational
# orthogonal U.  Use exact sympy throughout (no transcendental trig).
psi = sp.Matrix([sp.Rational(3, 5), sp.Rational(4, 5)])  # rational unit vector
P = psi * psi.T  # rank-1 real projection (psi real => P† = P)
P = sp.simplify(P)

# Effect E with exact spectrum {3/4, 1/4} in a rotated real basis (exact
# rational orthogonal U from a different Pythagorean triple (5/13, 12/13)).
U = sp.Matrix([[sp.Rational(5, 13), -sp.Rational(12, 13)],
               [sp.Rational(12, 13), sp.Rational(5, 13)]])
E = sp.simplify(U * sp.diag(sp.Rational(3, 4), sp.Rational(1, 4)) * U.T)

# An exact density operator rho = (I + r.sigma)/2 with a real Bloch vector
# inside the unit ball: r = (rx, 0, rz), rx^2 + rz^2 < 1.
rx, rz = sp.Rational(2, 5), sp.Rational(1, 3)
sx = sp.Matrix([[0, 1], [1, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
rho = sp.simplify((sp.eye(2) + rx * sx + rz * sz) / 2)

# P is a projection (exact): P^2 = P, P† = P.
check("d2_exact P is projection (P^2 = P, P† = P)",
      sp.simplify(P * P - P) == sp.zeros(2, 2)
      and sp.simplify(P - P.conjugate().T) == sp.zeros(2, 2),
      "rank-1 |psi><psi|, psi real")

# E is an effect (exact): E = E†, 0 <= E <= I (spectrum {3/4,1/4} by construction).
E_eigs = sorted(sp.simplify(E).eigenvals().keys())
check("d2_exact E is an effect (E† = E, spectrum in [0,1])",
      sp.simplify(E - E.conjugate().T) == sp.zeros(2, 2)
      and all(sp.simplify(ev) >= 0 and sp.simplify(ev) <= 1 for ev in E_eigs),
      f"spectrum = {[sp.nsimplify(ev) for ev in E_eigs]}")

# rho is a state (exact): rho = rho†, rho >= 0, Tr rho = 1.
rho_eigs = sorted(sp.simplify(rho).eigenvals().keys())
check("d2_exact rho is a state (rho† = rho, rho >= 0, Tr rho = 1)",
      sp.simplify(rho - rho.conjugate().T) == sp.zeros(2, 2)
      and all(sp.simplify(ev) >= 0 for ev in rho_eigs)
      and sp.simplify(sp.trace(rho)) == 1,
      f"eigs = {[sp.nsimplify(ev) for ev in rho_eigs]}")

# CORE BRIDGE (exact): Tr(rho PEP)/Tr(rho P) == Tr( (P rho P/Tr(P rho P)) E ).
trP = sp.simplify(sp.trace(rho * P))
lhs0 = sp.simplify(sp.trace(rho * (P * E * P)) / trP)          # via M_{P,E}=PEP
post = sp.simplify((P * rho * P) / sp.simplify(sp.trace(P * rho * P)))
rhs0 = sp.simplify(sp.trace(post * E))                          # two-step defn
check("d2_exact: Tr(rho PEP)/Tr(rho P) = Tr(rho|_P E) (M_{P,E}=PEP, EXACT)",
      sp.simplify(lhs0 - rhs0) == 0,
      f"common value = {sp.nsimplify(lhs0)}")

# Equivalent factorized statement: Tr(rho PEP) = Tr(rho P) * Tr(rho|_P E).
check("d2_exact: Tr(rho PEP) = Tr(rho P) * Tr(rho|_P E) (factorized chain, EXACT)",
      sp.simplify(sp.trace(rho * (P * E * P)) - trP * rhs0) == 0,
      "p(P then E) = p(P) * p(E|P)")

# Trace cyclicity used to land PEP on the updated state: Tr(rho PEP) = Tr(P rho P E).
check("d2_exact: Tr(rho P E P) = Tr(P rho P E) (trace cyclicity, EXACT)",
      sp.simplify(sp.trace(rho * P * E * P) - sp.trace(P * rho * P * E)) == 0,
      "cyclicity moves PEP -> P rho P")

# Boundary conditions selecting PEP: M_{P,I}=P and M_{I,E}=E (exact).
check("d2_exact boundary: M_{P,I} = P E P|_{E=I} = P",
      sp.simplify(P * sp.eye(2) * P - P) == sp.zeros(2, 2),
      "P I P = P^2 = P")
check("d2_exact boundary: M_{I,E} = I E I = E",
      sp.simplify(sp.eye(2) * E * sp.eye(2) - E) == sp.zeros(2, 2),
      "I E I = E")

# Valid-effect properties (exact): 0 <= PEP <= P <= I.
PEP = sp.simplify(P * E * P)
PEP_eigs = sorted(sp.simplify(PEP).eigenvals().keys())
check("d2_exact: P E P >= 0 (spectrum >= 0, EXACT)",
      all(sp.simplify(ev) >= 0 for ev in PEP_eigs),
      f"spectrum(PEP) = {[sp.nsimplify(ev) for ev in PEP_eigs]}")
P_minus_PEP = sp.simplify(P - PEP)
PmP_eigs = sorted(sp.simplify(P_minus_PEP).eigenvals().keys())
check("d2_exact: P - P E P = P(I-E)P >= 0  (so PEP <= P, EXACT)",
      sp.simplify(P_minus_PEP - sp.simplify(P * (sp.eye(2) - E) * P)) == sp.zeros(2, 2)
      and all(sp.simplify(ev) >= 0 for ev in PmP_eigs),
      f"spectrum(P-PEP) = {[sp.nsimplify(ev) for ev in PmP_eigs]}")
I_minus_P = sp.simplify(sp.eye(2) - P)
ImP_eigs = sorted(sp.simplify(I_minus_P).eigenvals().keys())
check("d2_exact: I - P >= 0  (P <= I, EXACT)",
      all(sp.simplify(ev) >= 0 for ev in ImP_eigs),
      f"spectrum(I-P) = {[sp.nsimplify(ev) for ev in ImP_eigs]}")


# ===========================================================================
# Part 1 -- core bridge identity Tr(rho PEP)/Tr(rho P) = two-step prob,
#           numeric over d = 2,3,4 (qubit + tensor-power carriers)
# ===========================================================================
print("\n=== Part 1: numeric d=2,3,4 -- two-step probability = Tr(rho PEP)/Tr(rho P) ===")

for d in (2, 3, 4):
    rng = np.random.default_rng(20260605 + d)
    worst = 0.0
    n_used = 0
    for _ in range(400):
        rho = random_density(d, rng)
        P = random_projection(d, rng)
        E = random_effect(d, rng)
        pP = float(np.trace(rho @ P).real)
        if pP < 1e-6:
            continue
        n_used += 1
        # Effective two-step operator M_{P,E} = P E P:
        lhs = float(np.trace(rho @ (P @ E @ P)).real) / pP
        # Two-step definition: update by the supplied Lueders map, then pair with E.
        post = (P @ rho @ P) / pP
        rhs = float(np.trace(post @ E).real)
        worst = max(worst, abs(lhs - rhs))
    check(f"d{d}: Tr(rho PEP)/Tr(rho P) = Tr(rho|_P E) over {n_used} seeds",
          worst < 1e-9,
          f"max |LHS - RHS| = {worst:.2e}")


# ===========================================================================
# Part 2 -- valid-effect properties of PEP: 0 <= PEP <= P <= I, numeric d=2,3,4
# ===========================================================================
print("\n=== Part 2: numeric d=2,3,4 -- 0 <= P E P <= P <= I (PEP is a valid effect) ===")

for d in (2, 3, 4):
    rng = np.random.default_rng(770011 + d)
    worst_pep = 0.0       # most-negative eig of PEP
    worst_p_minus = 0.0   # most-negative eig of P - PEP
    worst_i_minus = 0.0   # most-negative eig of I - P
    cong_resid = 0.0      # ||(P - PEP) - P(I-E)P||
    for _ in range(400):
        P = random_projection(d, rng)
        E = random_effect(d, rng)
        PEP = P @ E @ P
        worst_pep = min(worst_pep, min_eig(PEP))
        worst_p_minus = min(worst_p_minus, min_eig(P - PEP))
        worst_i_minus = min(worst_i_minus, min_eig(np.eye(d) - P))
        cong_resid = max(
            cong_resid,
            float(np.linalg.norm((P - PEP) - P @ (np.eye(d) - E) @ P)),
        )
    check(f"d{d}: P E P >= 0 over 400 seeds",
          worst_pep > -1e-9, f"min eig(PEP) = {worst_pep:+.2e}")
    check(f"d{d}: P - P E P = P(I-E)P (congruence identity) over 400 seeds",
          cong_resid < 1e-9, f"max ||(P-PEP)-P(I-E)P|| = {cong_resid:.2e}")
    check(f"d{d}: P E P <= P over 400 seeds",
          worst_p_minus > -1e-9, f"min eig(P-PEP) = {worst_p_minus:+.2e}")
    check(f"d{d}: P <= I over 400 seeds",
          worst_i_minus > -1e-9, f"min eig(I-P) = {worst_i_minus:+.2e}")


# ===========================================================================
# Part 3 -- supplied trace/effect pairing: real-linear, maps states to [0,1]
# ===========================================================================
print("\n=== Part 3: numeric d=2,3,4 -- trace pairing rho -> Tr(rho E) is "
      "real-linear and maps states to [0,1] ===")

for d in (2, 3, 4):
    rng = np.random.default_rng(990022 + d)
    lin_resid = 0.0
    real_resid = 0.0
    worst_lo = 1.0
    worst_hi = 0.0
    for _ in range(400):
        E = random_effect(d, rng)
        r1 = random_density(d, rng)
        r2 = random_density(d, rng)
        a = float(rng.uniform(0.1, 0.9))  # convex weight => state mixture
        mix = a * r1 + (1.0 - a) * r2  # a state (convex combo of states)
        # linearity: Tr((a r1 + (1-a) r2) E) = a Tr(r1 E) + (1-a) Tr(r2 E)
        lhs = complex(np.trace(mix @ E))
        rhs = a * complex(np.trace(r1 @ E)) + (1.0 - a) * complex(np.trace(r2 @ E))
        lin_resid = max(lin_resid, abs(lhs - rhs))
        # value on a state is real and in [0,1]
        val = complex(np.trace(r1 @ E))
        real_resid = max(real_resid, abs(val.imag))
        worst_lo = min(worst_lo, val.real)
        worst_hi = max(worst_hi, val.real)
    check(f"d{d}: trace pairing is linear (Tr((a r1+(1-a)r2)E) = a Tr(r1 E)+(1-a)Tr(r2 E))",
          lin_resid < 1e-10, f"max linearity residual = {lin_resid:.2e}")
    check(f"d{d}: Tr(rho E) is real on states/effects",
          real_resid < 1e-12, f"max |Im Tr(rho E)| = {real_resid:.2e}")
    check(f"d{d}: 0 <= Tr(rho E) <= 1 on states/effects over 400 seeds",
          worst_lo > -1e-12 and worst_hi < 1.0 + 1e-12,
          f"range = [{worst_lo:.6f}, {worst_hi:.6f}]")


# ===========================================================================
# Part 4 -- associative-consistency of the sequential product (P then Q then F)
# ===========================================================================
print("\n=== Part 4: numeric d=2,3,4 -- associative-consistency: "
      "'P then Q then F' effective operator = P (Q F Q) P = (QP)† F (QP) ===")

for d in (2, 3, 4):
    rng = np.random.default_rng(330044 + d)
    nest_resid = 0.0
    comp_resid = 0.0
    valid_resid = 0.0
    for _ in range(400):
        P = random_projection(d, rng)
        Q = random_projection(d, rng)
        F = random_effect(d, rng)
        # The 'P then Q then F' sequential effect operator: first compose
        # 'Q then F' into M_{Q,F} = Q F Q, then compose 'P then (that)':
        M_QF = Q @ F @ Q
        seq_P_Q_F = P @ M_QF @ P                  # P (Q F Q) P
        # Compositional form via the (U4) composite Kraus operator K = Q P:
        K = Q @ P
        comp = K.conj().T @ F @ K                 # (QP)† F (QP) = P Q F Q P
        nest_resid = max(nest_resid, float(np.linalg.norm(seq_P_Q_F - comp)))
        # M_QF is itself a valid effect (0 <= M_QF <= Q <= I), so the outer
        # 'P then M_QF' = P M_QF P is again a valid effect (0 <= . <= P).
        outer = P @ M_QF @ P
        valid_resid = max(valid_resid, max(0.0, -min_eig(outer)),
                          max(0.0, -min_eig(P - outer)))
        # Boundary-condition consistency of the composite at F = I:
        # 'P then Q then I' = P Q I Q P = P Q P  (= M_{P,Q} with effect Q).
        comp_I = P @ Q @ np.eye(d) @ Q @ P
        comp_resid = max(comp_resid, float(np.linalg.norm(comp_I - P @ Q @ P)))
    check(f"d{d}: P(QFQ)P = (QP)† F (QP) (sequential = compositional) over 400 seeds",
          nest_resid < 1e-9, f"max ||P(QFQ)P - (QP)†F(QP)|| = {nest_resid:.2e}")
    check(f"d{d}: outer 'P then (QFQ)' stays a valid effect (0 <= . <= P)",
          valid_resid < 1e-9, f"max boundary violation = {valid_resid:.2e}")
    check(f"d{d}: composite at F=I gives P Q P (boundary-consistent) over 400 seeds",
          comp_resid < 1e-9, f"max ||P Q I Q P - P Q P|| = {comp_resid:.2e}")


# ===========================================================================
# Part 5 -- exact nested case (commuting projections): PEP collapses correctly
# ===========================================================================
print("\n=== Part 5: exact -- commuting/nested projections collapse PEP as expected ===")

# Two commuting diagonal projections on d=3 and a diagonal effect; the
# sequential product P E P must reduce to the entrywise-supported effect.
P1 = sp.diag(1, 1, 0)       # rank-2 projection
P2 = sp.diag(1, 0, 1)       # rank-2 projection, commutes with P1
Ediag = sp.diag(sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(3, 4))
check("d3_exact: commuting projections [P1,P2] = 0",
      sp.simplify(P1 * P2 - P2 * P1) == sp.zeros(3, 3),
      "diagonal => commute")
# M_{P1,E} = P1 E P1 supported on range(P1): zeroes the 3rd diagonal entry.
M1 = sp.simplify(P1 * Ediag * P1)
check("d3_exact: P1 E P1 = diag(1/2, 1/3, 0)  (supported on range P1)",
      sp.simplify(M1 - sp.diag(sp.Rational(1, 2), sp.Rational(1, 3), 0)) == sp.zeros(3, 3),
      f"M_{{P1,E}} = {(sp.nsimplify(M1[0,0]), sp.nsimplify(M1[1,1]), sp.nsimplify(M1[2,2]))}")
# Sequential P1 then P2 then E: P1 (P2 E P2) P1 supported on range(P1 ∧ P2).
seq = sp.simplify(P1 * (P2 * Ediag * P2) * P1)
comp_QP = sp.simplify((P2 * P1).T * Ediag * (P2 * P1))  # (QP)† E (QP), real => transpose
check("d3_exact: P1(P2 E P2)P1 = (P2 P1)† E (P2 P1) (sequential = compositional)",
      sp.simplify(seq - comp_QP) == sp.zeros(3, 3),
      f"common = diag {tuple(sp.nsimplify(seq[i, i]) for i in range(3))}")
check("d3_exact: nested commuting product = diag(1/2, 0, 0) on range(P1∧P2)",
      sp.simplify(seq - sp.diag(sp.Rational(1, 2), 0, 0)) == sp.zeros(3, 3),
      "only common-support entry survives")


# ===========================================================================
# Part 6 -- counter-direction guard: a NON-PEP candidate breaks the
#           boundary/positivity conditions and the supplied two-step identity
# ===========================================================================
print("\n=== Part 6: guard -- a non-PEP sequential candidate fails positivity "
      "and the supplied two-step identity ===")

# Candidate "symmetrized" alternative  M' = (P E + E P)/2  (the Jordan product).
# It satisfies the boundary conditions M'_{P,I}=P, M'_{I,E}=E but is NOT
# guaranteed positive, and does NOT reproduce the Lueders two-step probability.
# Exhibit an explicit witness on d=2 (exact, rational) where M' is indefinite
# and the two-step probability identity fails, whereas PEP passes.
psi2 = sp.Matrix([sp.Rational(3, 5), sp.Rational(4, 5)])  # exact rational unit vector
Pg = sp.simplify(psi2 * psi2.T)
Eg = sp.simplify(U * sp.diag(1, 0) * U.T)        # E = rank-1 projection (an effect)
rho_g = sp.simplify((sp.eye(2) + sp.Rational(2, 5) * sx + sp.Rational(1, 3) * sz) / 2)

Mprime = sp.simplify((Pg * Eg + Eg * Pg) / 2)    # Jordan product candidate
# Boundary conditions still hold for the Jordan product:
check("d2_exact: Jordan candidate satisfies boundaries M'_{P,I}=P, M'_{I,E}=E",
      sp.simplify((Pg * sp.eye(2) + sp.eye(2) * Pg) / 2 - Pg) == sp.zeros(2, 2)
      and sp.simplify((sp.eye(2) * Eg + Eg * sp.eye(2)) / 2 - Eg) == sp.zeros(2, 2),
      "boundaries alone do not single out PEP vs Jordan")
# ... but the Jordan candidate is indefinite (not a valid effect):
Mp_eigs = sorted(sp.simplify(Mprime).eigenvals().keys())
mp_min = min(sp.simplify(ev) for ev in Mp_eigs)
check("d2_exact: Jordan candidate (PE+EP)/2 is INDEFINITE (some eig < 0)",
      mp_min < 0,
      f"min eig(M') = {sp.nsimplify(mp_min)} < 0  => not a valid effect")
# ... and it does NOT reproduce the Lueders two-step probability:
trPg = sp.simplify(sp.trace(rho_g * Pg))
two_step = sp.simplify(sp.trace((Pg * rho_g * Pg) / sp.trace(Pg * rho_g * Pg) * Eg))
jordan_step = sp.simplify(sp.trace(rho_g * Mprime) / trPg)
pep_step = sp.simplify(sp.trace(rho_g * (Pg * Eg * Pg)) / trPg)
check("d2_exact: PEP reproduces two-step prob; Jordan candidate does NOT",
      sp.simplify(pep_step - two_step) == 0 and sp.simplify(jordan_step - two_step) != 0,
      f"two-step={sp.nsimplify(two_step)}, PEP={sp.nsimplify(pep_step)}, "
      f"Jordan={sp.nsimplify(jordan_step)}")


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

print("\nAll checks passed under the supplied measurement-side premises: "
      "M_{P,E} = P E P is the pre-update effect for the supplied two-step "
      "probability [Tr(rho PEP)/Tr(rho P) = Tr(rho|_P E)], it is a valid effect "
      "[0 <= PEP <= P <= I], the supplied trace/effect pairing is real-linear "
      "and maps states/effects to [0,1], and the sequential product is "
      "associative-compatible with composition. The runner does not establish "
      "the Lueders update, Born rule, or trace/effect pairing as framework-native.")
sys.exit(0)
