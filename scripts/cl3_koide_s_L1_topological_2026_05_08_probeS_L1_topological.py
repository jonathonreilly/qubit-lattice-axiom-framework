#!/usr/bin/env python3
"""Finite supplied CS/knot comparisons and corrected character-domain controls.
No general CS-to-beta impossibility theorem. Full superseded argument and
literal-True documentary checks are preserved in the cited recovery archive.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ('docs/KOIDE_A1_O13_CHEEGER_SIMONS_RZ_NO_GO_NOTE_2026-04-24.md', 'docs/KOIDE_S_L1_TOPOLOGICAL_CHERN_SIMONS_NOTE_2026-05-08_probeS_L1_topological.md')


import cmath

import math

import sys

from fractions import Fraction

from math import comb

class Counter:
    """Simple counter for PASS / FAIL / bounded-import outcomes."""

    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.admitted = 0
        self.failures: list[str] = []

    def record(self, name: str, ok: bool, detail: str = "") -> None:
        tag = "PASS" if ok else "FAIL"
        if detail:
            print(f"  [{tag}] {name} | {detail}")
        else:
            print(f"  [{tag}] {name}")
        if ok:
            self.passed += 1
        else:
            self.failed += 1
            self.failures.append(name)

    def admit(self, name: str, detail: str = "") -> None:
        if detail:
            print(f"  [BOUNDED-IMPORT] {name} | {detail}")
        else:
            print(f"  [BOUNDED-IMPORT] {name}")
        self.admitted += 1

    def summary(self) -> None:
        print()
        print(
            f"SUMMARY: PASS={self.passed} FAIL={self.failed} "
            f"BOUNDED_IMPORT={self.admitted}"
        )
        if self.failed:
            print(f"FAILURES: {', '.join(self.failures)}")

N_COLOR = 3

C_F = Fraction(N_COLOR ** 2 - 1, 2 * N_COLOR)  # 4/3

C_A = Fraction(N_COLOR)  # 3

T_F = Fraction(1, 2)

N_F = 6  # n_f above all SM thresholds

H_VEE_SU3 = N_COLOR  # = 3 (standard Lie-algebra topological number)

BETA_0_QCD_NF6 = Fraction(11, 3) * N_COLOR - Fraction(2, 3) * N_F

BETA_1_QCD_NF6 = (
    Fraction(34, 3) * N_COLOR ** 2
    - (Fraction(10, 3) * N_COLOR + 2 * C_F) * N_F
)

BETA_2_QCD_NF6 = (
    Fraction(2857, 2)
    - Fraction(5033, 18) * N_F
    + Fraction(325, 54) * N_F ** 2
)

TVZ_CHANNEL_WEIGHTS = {
    "C_A^3":            Fraction(2857, 54),
    "C_A^2 * (T_F n_f)": Fraction(-1415, 54),
    "C_F C_A * (T_F n_f)": Fraction(-205, 18),
    "C_A * (T_F n_f)^2": Fraction(79, 54),
    "C_F * (T_F n_f)^2": Fraction(11, 9),
    "C_F^2 * (T_F n_f)": Fraction(1, 2),
}

def section1_cs_partition_function_T3(c: Counter) -> None:
    """The Chern-Simons partition function on T^3 for SU(N) at level k
    equals the number of integrable level-k representations of the
    affine Lie algebra (after Reshetikhin-Turaev 1991). For SU(3),
    this is the number of pairs (lambda_1, lambda_2) of non-negative
    integer Dynkin labels with lambda_1 + lambda_2 <= k:

        Z(T^3, SU(3)_k) = (k+1)(k+2)/2.

    This is a single positive integer per level. Pure topology — no
    metric, no scheme, no regulator.
    """
    print("Section 1 — SUPPORT: CS partition function on T^3 for SU(3)")

    for k in (1, 2, 3, 5, 10):
        # Standard Reshetikhin-Turaev formula
        n_reps = (k + 1) * (k + 2) // 2
        # Cross-check by enumeration
        enum_count = sum(
            1
            for l1 in range(k + 1)
            for l2 in range(k + 1)
            if l1 + l2 <= k
        )
        ok = (n_reps == enum_count)
        c.record(
            f"Z(T^3, SU(3)_{k}) = (k+1)(k+2)/2 reproduced",
            ok,
            f"= {n_reps} (enumerated {enum_count})",
        )

    print("    -> CS partition function on T^3 is a single positive integer per (G, k).")
    print("    -> Pure topology: no metric, no scheme, no regulator dependence.")
    print("    -> No map to the supplied beta_n comparison vector is constructed here.")

def quantum_dim(q: complex, n: int) -> complex:
    """Quantum integer [n]_q = (q^{n/2} - q^{-n/2}) / (q^{1/2} - q^{-1/2})."""
    num = q ** (n / 2) - q ** (-n / 2)
    den = q ** 0.5 - q ** (-0.5)
    return num / den

def section2_quantum_dimension(c: Counter) -> None:
    """The SU(3) quantum dimension of the fundamental representation
    at level k is the quantum integer [3]_q with q = exp(2*pi*i/(k+h^vee))
    = exp(2*pi*i/(k+3)).

    At various levels:
        k = 1: q = exp(2*pi*i/4), [3]_q = 1
        k = 2: q = exp(2*pi*i/5), [3]_q = phi (golden ratio)
        k = 3: q = exp(2*pi*i/6), [3]_q = 2
        k = 5: q = exp(2*pi*i/8), [3]_q = 1 + sqrt(2)
        k -> infinity: [3]_q -> 3 (classical Casimir-skeleton dim)

    Some tested values are irrational (k=2 and k=5), while others are
    rational (k=1 gives 1; k=3 gives 2). Cyclotomic membership alone
    excludes neither rational numbers nor irrational algebraic values.
    """
    print()
    print("Section 2 — SUPPORT: SU(3) quantum dimension [3]_q at CS root-of-unity")

    # Reference values to floating-point tolerance.
    phi = (1 + math.sqrt(5)) / 2  # golden ratio
    sqrt2_plus_1 = 1 + math.sqrt(2)

    test_cases = [
        (1, 1.0,            "[3]_q = 1",                       1e-9),
        (2, phi,             "[3]_q = phi = (1+sqrt(5))/2",     1e-9),
        (3, 2.0,             "[3]_q = 2",                       1e-9),
        (5, sqrt2_plus_1,    "[3]_q = 1+sqrt(2)",               1e-9),
        (10, None,           "[3]_q approaches 3 (classical limit)", 0.3),
        (100, None,          "[3]_q -> 3 as k -> inf",          0.01),
    ]

    for k, expected, label, tol in test_cases:
        q = cmath.exp(2j * math.pi / (k + H_VEE_SU3))
        dq = quantum_dim(q, 3)
        if expected is not None:
            ok = abs(dq.real - expected) < tol and abs(dq.imag) < 1e-9
            c.record(
                f"SU(3) [3]_q at k={k} matches {label}",
                ok,
                f"computed {dq.real:.6f}+{dq.imag:.2e}i; expected {expected:.6f}",
            )
        else:
            # Just verify it's close to the classical limit 3 at large k
            ok = abs(dq.real - 3) < tol and abs(dq.imag) < 1e-9
            c.record(
                f"SU(3) [3]_q at k={k} {label}",
                ok,
                f"computed {dq.real:.6f}+{dq.imag:.2e}i; expected ~3 (tol {tol})",
            )

    print("    -> [3]_q is a cyclotomic algebraic integer in Q(zeta_(k+3)).")
    print("    -> Some tested values are irrational (k=2: phi; k=5: 1+sqrt(2));")
    print("       others are rational (k=1: 1; k=3: 2).")
    print("    -> Classical limit k->inf reproduces only the Casimir-skeleton")
    print("       dimension 3 — already supported, NOT new information.")

def jones_trefoil(q: complex) -> complex:
    """Jones polynomial of the (right-handed) trefoil knot:
        V(3_1)(q) = -q^{-4} + q^{-3} + q^{-1}
    """
    return -q ** (-4) + q ** (-3) + q ** (-1)

def section3_jones_polynomial_trefoil(c: Counter) -> None:
    """The Jones polynomial of the trefoil is a standard knot invariant
    encoding the Wilson loop expectation value in CS theory with the
    trefoil-knot Wilson loop (after Witten 1989).

    Symbolic form: V(3_1)(q) = -q^(-4) + q^(-3) + q^(-1).

    Evaluated at CS levels q = exp(2*pi*i/(k+2)) for SU(2)_k (the
    standard simplest case), the output is a cyclotomic algebraic
    number, generally COMPLEX at non-trivial levels. The output field
    is Q(zeta_(k+2)) for SU(2)_k, generally with non-real values.

    The beta_n channel weights in MSbar are PURE REAL RATIONALS at
    beta_2 and RATIONALS PLUS REAL zeta_3 at beta_3. These finite evaluations do not supply a physical matching map.
    """
    print()
    print("Section 3 — SUPPORT: Jones polynomial of trefoil (CS Wilson loop)")

    # Evaluate at SU(2)_k for k = 1, 2, 3, 4 (the standard simplest cases
    # where the formula is well-tested). Note SU(2) here is for the simplest
    # Jones polynomial setting; SU(3) Wilson loops give HOMFLY rather than
    # Jones, but the structural point (cyclotomic algebraic output) is the
    # same and easier to see in the SU(2) case.

    for k in (1, 2, 3, 4):
        # SU(2) level shift is +2 = h^vee(SU(2))
        q = cmath.exp(2j * math.pi / (k + 2))
        val = jones_trefoil(q)
        is_real = abs(val.imag) < 1e-9
        c.record(
            f"Jones(trefoil) at SU(2)_{k}: q = exp(2*pi*i/{k+2}) finite supplied-polynomial evaluation",
            math.isfinite(val.real) and math.isfinite(val.imag),  # finite evaluated output only
            f"V = {val.real:.4f}+{val.imag:.4f}i (real? {is_real})",
        )

    # Symbolic verification: the coefficients of V(3_1) are {-1, +1, +1}
    # at q-powers {-4, -3, -1}. These are integers from the bracket
    # polynomial computation, NOT framework-derived rationals.
    c.record(
        "Supplied Jones polynomial has V(1)=1",
        jones_trefoil(1) == 1,
        "checks the supplied polynomial only; no skein derivation",
    )

    print("    -> Jones polynomial is a Laurent polynomial in q with INTEGER coefs.")
    print("    -> Evaluated at CS roots of unity gives cyclotomic algebraic values.")
    print("    -> Rational numbers are contained in cyclotomic fields; field membership is no obstruction.")
    print("    -> Generally complex; beta_n channel weights are real rationals + real zeta_3.")

def section5_level_shift_vs_beta_0(c: Counter) -> None:
    """Test the conjecture in the probe-scope memo:
       "Does the level shift k -> k + 3 in CS give beta_0 = 7?"

    Numerical check:
      h^vee(SU(3)) = 3 (dual Coxeter number)
      beta_0(QCD, N_f=6) = 11/3 * N_c - 2/3 * N_f = 11 - 4 = 7

    These are different integers. Moreover beta_0 is matter-content
    dependent (depends on n_f), while h^vee is pure gauge topology
    (depends only on SU(N)). Varying n_f:
      n_f = 0: beta_0 = 11
      n_f = 6: beta_0 = 7
      n_f = 11: beta_0 = 11/3
    NONE equal h^vee = 3.
    """
    print()
    print("Section 5 — NEGATIVE: numerical h^vee != beta_0 mismatch")

    c.record(
        "h^vee(SU(3)) = 3",
        H_VEE_SU3 == 3,
        f"dual Coxeter number for SU(3) = {H_VEE_SU3}",
    )

    c.record(
        "beta_0(QCD, N_f=6) = 7",
        BETA_0_QCD_NF6 == Fraction(7),
        f"= 11/3 * 3 - 2/3 * 6 = {BETA_0_QCD_NF6}",
    )

    c.record(
        "h^vee != beta_0 at N_f=6 (3 != 7)",
        H_VEE_SU3 != BETA_0_QCD_NF6,
        "the conjectured identification k+h^vee = beta_0 is numerically false",
    )

    # Show beta_0 varies with n_f but h^vee does not
    for n_f in (0, 3, 6, 11, 16):
        b0 = Fraction(11, 3) * N_COLOR - Fraction(2, 3) * n_f
        c.record(
            f"beta_0(N_f={n_f}) = {b0} (h^vee remains {H_VEE_SU3})",
            b0 != H_VEE_SU3,
            f"matter-content dependent; CS h^vee is matter-blind",
        )

    print("    -> h^vee(SU(3)) = 3 is a PURE GAUGE-TOPOLOGY number (depends only on SU(N)).")
    print("    -> beta_0(QCD, N_f) is MATTER-CONTENT-DEPENDENT (varies with N_f).")
    print("    -> The tested N_f values differ; N_f=12 gives beta_0=3, so no all-N_f mismatch is claimed.")

def character_domain_controls(c):
    # A flat character on Z is specified by any a in R/Z; no torsion constraint.
    a = 1 / (9 * math.pi)
    phase = cmath.exp(2j * math.pi * a)
    target = cmath.exp(2j / 9)
    c.record('free-cycle character a=1/(9pi) realizes exp(i2/9)',
             abs(phase - target) < 1e-14,
             'supplied character, not physical selection')
    c.record('integer lift leaves the R/Z phase unchanged',
             abs(cmath.exp(2j * math.pi * (a + 1)) - phase) < 1e-14)
    torsion = [Fraction(j, 3) for j in range(3)]
    c.record('order-three values obey 3c=0 modulo1',
             all((3 * v).denominator == 1 for v in torsion))
    c.record('candidate c=2/9 fails the order-three relation',
             (3 * Fraction(2, 9)).denominator != 1)
    c.record('six supplied TVZ weights are nonzero rational comparators',
             len(TVZ_CHANNEL_WEIGHTS) == 6 and all(isinstance(v, Fraction) and v != 0 for v in TVZ_CHANNEL_WEIGHTS.values()))
    print('Order-three torsion restricts c; arbitrary free-cycle classes do not.')
    print('No universal rational-angle obstruction and no CS-to-beta impossibility follows.')

def main():
    c = Counter()
    section1_cs_partition_function_T3(c)
    section2_quantum_dimension(c)
    section3_jones_polynomial_trefoil(c)
    section5_level_shift_vs_beta_0(c)
    character_domain_controls(c)
    c.admit('physical CS/knot-to-beta map', 'not constructed; absence is not impossibility')
    c.admit('scheme, metric and source identification', 'separate required data for a physical matching claim')
    print('Historical cardinality, dimensional and universal phase no-go claims are withdrawn.')
    print('Original finite constants/formulas and negative comparisons are preserved; no arbitrary PASS quota.')
    c.summary()
    return 1 if c.failed else 0
if __name__ == '__main__':
    sys.exit(main())
