#!/usr/bin/env python3
"""The seed-class question: every spectrally-constructed class weight is
automatically real/flip-even (the spectral data are exactly conjugation-
invariant); the pure-gauge supplied structure (fusion + spectral data) is
exactly conjugation-symmetric, so a phased seed requires conjugation-
asymmetric data the gauge surface does not carry; seed space splits under
the outer flip with the odd part exactly the theta carrier; and
conjugation-odd data live in determinant-phase (matter-side) structures.

Paired note:
docs/THETA_SEED_SPECTRAL_REALITY_CONJUGATION_SYMMETRIC_SUPPLIED_STRUCTURE_BOUNDED_THEOREM_NOTE_2026-07-02.md

Class-A finite checks only: exact rational Casimir/dimension algebra, exact
fusion combinatorics on the retained recurrence, character-sum evaluations
at deterministic points, and discriminating contrasts (the phased seed
breaks every evenness gate). Deterministic; no fits, no external
comparators, no measured values, no Monte Carlo.

Sections:
  A. Spectral data are conjugation-invariant (exact): C2(p,q) = C2(q,p) and
     d(p,q) = d(q,p) across a window; heat-kernel coefficients are real and
     conjugation-paired; Wilson coefficients are real and conjugation-paired
     (Weyl quadrature).
  B. The spectral-reality theorem, instance-verified with contrast: any real
     function of (C2, d) gives a flip-even class weight (dagger and bar);
     the phased (non-spectral) seed breaks the same gates.
  C. Fusion conjugation-symmetry (exact): the retained recurrence satisfies
     N^c_{ab} = N^{cbar}_{abar bbar} — channels of chi_F x chi_(p,q) map to
     channels of chi_Fb x chi_(q,p) under conjugation, exactly; the joint
     supplied-structure profile (C2, d, fusion multiplicities) of R equals
     that of Rbar across the window: the pure-gauge supplied structure does
     not distinguish conjugate pairs.
  D. Seed-space splitting: any class weight splits under the outer flip into
     even + odd; for the phased seed the even part is the real cos(alpha)
     weight and the odd part equals -2 c sin(alpha) Im(chi_F) — a
     REAL-VALUED per-plaquette imaginary-trace reweighting. This identifies
     the single-plaquette candidate direction; flow/source conclusions belong
     to separate campaign blocks, not this runner.
     NOT an imaginary action (design claim refuted by the computation);
     determinant phases are conjugation-ODD (arg det conj(M) = -arg det M):
     conjugation-asymmetric data of the needed type live in
     determinant-phase (matter-side) structures, not on the pure-gauge
     seed surface.

Expected close: TOTAL: PASS=10 FAIL=0
"""
from __future__ import annotations

from fractions import Fraction

import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


RNG = np.random.default_rng(7)

# ---------------------------------------------------------------------------
# Section A: spectral data are conjugation-invariant
# ---------------------------------------------------------------------------
print("Section A: conjugation-invariant spectral data")


def casimir(p: int, q: int) -> Fraction:
    # |mu|^2 - |rho|^2 with mu = (p+1, q+1), Gram = (1/3)[[2,1],[1,2]]
    a, b = p + 1, q + 1
    return Fraction(2, 3) * (a * a + a * b + b * b) - Fraction(2, 3) * 3


def dim_pq(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


WINDOW = [(p, q) for p in range(6) for q in range(6)]
check("A1 C2(p,q) = C2(q,p) and d(p,q) = d(q,p) across the window:"
      " Casimir and dimension are exactly conjugation-invariant",
      all(casimir(p, q) == casimir(q, p) and dim_pq(p, q) == dim_pq(q, p)
          for (p, q) in WINDOW))

T_HK = 0.4
ok_hk = all(abs(float(dim_pq(p, q)) * np.exp(-T_HK * float(casimir(p, q)))
                - float(dim_pq(q, p)) * np.exp(-T_HK * float(casimir(q, p))))
            < 1e-15 for (p, q) in WINDOW)
check("A2 heat-kernel coefficients d_R e^{-t C2} are real and exactly"
      " conjugation-paired", ok_hk)

NQ = 160
g1 = (np.arange(NQ) + 0.31) * 2 * np.pi / NQ
g2 = (np.arange(NQ) + 0.11) * 2 * np.pi / NQ
T1G, T2G = np.meshgrid(g1, g2, indexing="ij")
Z1 = np.exp(1j * T1G)
Z2 = np.exp(1j * T2G)
Z3 = np.exp(-1j * (T1G + T2G))
DD = np.abs((Z1 - Z2) * (Z1 - Z3) * (Z2 - Z3)) ** 2
RETR = (Z1 + Z2 + Z3).real
BETA = 6.0
WGT = np.exp((BETA / 3.0) * RETR) * DD
NRM = float(np.sum(DD))


def su3_char(p: int, q: int) -> np.ndarray:
    lam = [p + q, q, 0]
    e = [lam[j] + 2 - j for j in range(3)]

    def det3(a, b, c):
        return (a[0] * (b[1] * c[2] - b[2] * c[1])
                - a[1] * (b[0] * c[2] - b[2] * c[0])
                + a[2] * (b[0] * c[1] - b[1] * c[0]))

    num = det3([Z1 ** e[0], Z1 ** e[1], Z1 ** e[2]],
               [Z2 ** e[0], Z2 ** e[1], Z2 ** e[2]],
               [Z3 ** e[0], Z3 ** e[1], Z3 ** e[2]])
    den = det3([Z1 ** 2, Z1, np.ones_like(Z1)],
               [Z2 ** 2, Z2, np.ones_like(Z2)],
               [Z3 ** 2, Z3, np.ones_like(Z3)])
    return num / den


ok_wil = True
for (p, q) in [(1, 0), (2, 0), (1, 1), (2, 1)]:
    cpq = complex(np.sum(WGT * np.conj(su3_char(p, q))) / NRM)
    cqp = complex(np.sum(WGT * np.conj(su3_char(q, p))) / NRM)
    ok_wil = ok_wil and abs(cpq.imag) < 1e-8 and abs(cpq - cqp) < 1e-8
check("A3 Wilson coefficients at beta = 6 are real and conjugation-paired"
      " (Weyl quadrature; the retained surface's own weight is spectral-"
      "even)", ok_wil)

# ---------------------------------------------------------------------------
# Section B: the spectral-reality theorem, instance-verified with contrast
# ---------------------------------------------------------------------------
print("Section B: real functions of spectral data give flip-even weights")

SAMPLE_T = [(0.37, -0.91), (1.11, 0.43), (-0.64, 1.27)]


def char_at(p: int, q: int, t1: float, t2: float) -> complex:
    z = np.array([np.exp(1j * t1), np.exp(1j * t2), np.exp(-1j * (t1 + t2))])
    lam = [p + q, q, 0]
    num = np.array([[z[i] ** (lam[j] + 2 - j) for j in range(3)]
                    for i in range(3)])
    den = np.array([[z[i] ** (2 - j) for j in range(3)] for i in range(3)])
    return complex(np.linalg.det(num) / np.linalg.det(den))


def weight_at(coeffs, t1: float, t2: float) -> complex:
    return sum(c * char_at(p, q, t1, t2) for (p, q), c in coeffs.items())


IRRWIN = [(p, q) for p in range(3) for q in range(3)]


def spectral_coeffs(f) -> dict:
    return {(p, q): f(float(casimir(p, q)), dim_pq(p, q))
            for (p, q) in IRRWIN}


ok_even = True
for f in [lambda c2, d: d * np.exp(-0.4 * c2),
          lambda c2, d: 1.0 / (1.0 + c2) ** 2,
          lambda c2, d: np.cos(0.3 * c2) / d]:
    coeffs = spectral_coeffs(f)
    for (t1, t2) in SAMPLE_T:
        w = weight_at(coeffs, t1, t2)
        w_dag = weight_at(coeffs, -t1, -t2)      # X^dag has inverse torus point
        ok_even = ok_even and abs(w.imag) < 1e-9 and abs(w_dag - w) < 1e-9
check("B1 three arbitrary real functions of (C2, d) all give real,"
      " dagger-even class weights (the spectral-reality theorem,"
      " instance-verified)", ok_even)

ALPHA = 0.7
phased = {(1, 0): 0.35 * np.exp(1j * ALPHA), (0, 1): 0.35 * np.exp(-1j * ALPHA),
          (0, 0): 1.0}
broke = False
for (t1, t2) in SAMPLE_T:
    w = weight_at(phased, t1, t2)
    w_dag = weight_at(phased, -t1, -t2)
    if abs(w_dag - w) > 1e-3:
        broke = True
check("B2 the phased (non-spectral) seed BREAKS the same gate"
      " (discriminating contrast: c_F != conj-pair)", broke)

# ---------------------------------------------------------------------------
# Section C: fusion conjugation-symmetry of the retained recurrence
# ---------------------------------------------------------------------------
print("Section C: the supplied structure is conjugation-symmetric")


def rule_F(p: int, q: int):
    return [(a, b) for (a, b) in [(p + 1, q), (p - 1, q + 1), (p, q - 1)]
            if a >= 0 and b >= 0]


def rule_Fb(p: int, q: int):
    return [(a, b) for (a, b) in [(p, q + 1), (p + 1, q - 1), (p - 1, q)]
            if a >= 0 and b >= 0]


ok_fus = True
for (p, q) in [(p, q) for p in range(5) for q in range(5)]:
    lhs = sorted((b, a) for (a, b) in rule_F(p, q))
    rhs = sorted(rule_Fb(q, p))
    ok_fus = ok_fus and (lhs == rhs)
check("C1 fusion conjugation-symmetry on the retained recurrence:"
      " channels of chi_F x chi_(p,q), conjugated, are exactly the"
      " channels of chi_Fb x chi_(q,p)", ok_fus)


def supplied_profile(p: int, q: int):
    return (casimir(p, q), dim_pq(p, q),
            sorted(rule_F(p, q)), sorted(rule_Fb(p, q)))


def conj_profile(profile):
    c2, d, rf, rfb = profile
    return (c2, d, sorted((b, a) for (a, b) in rfb),
            sorted((b, a) for (a, b) in rf))


ok_prof = all(supplied_profile(p, q) == conj_profile(supplied_profile(q, p))
              for (p, q) in [(p, q) for p in range(5) for q in range(5)])
check("C2 the joint supplied-structure profile (C2, d, fusion channels) of"
      " R equals the conjugate of Rbar's profile across the window: the"
      " pure-gauge supplied structure does not distinguish conjugate pairs",
      ok_prof)

# ---------------------------------------------------------------------------
# Section D: seed-space splitting and where conjugation-odd data live
# ---------------------------------------------------------------------------
print("Section D: outer-flip splitting; the odd part is the Im-trace direction")

ok_split = True
for (t1, t2) in SAMPLE_T:
    w = weight_at(phased, t1, t2)
    w_bar = weight_at(phased, -t1, -t2)  # conj(X): torus point negated
    even = (w + w_bar) / 2
    odd = (w - w_bar) / 2
    even_pred = (1.0 + 2 * 0.35 * np.cos(ALPHA)
                 * (char_at(1, 0, t1, t2) + char_at(0, 1, t1, t2)) / 2
                 + 0j)
    even_pred = 1.0 + 0.35 * np.cos(ALPHA) * (char_at(1, 0, t1, t2)
                                              + char_at(0, 1, t1, t2))
    odd_pred = 1j * 0.35 * np.sin(ALPHA) * (char_at(1, 0, t1, t2)
                                            - char_at(0, 1, t1, t2))
    ok_split = ok_split and abs(even - even_pred) < 1e-9 \
        and abs(odd - odd_pred) < 1e-9
check("D1 seed-space splitting: the phased seed's even part is the real"
      " cos(alpha) weight and its odd part is i c sin(alpha)(chi_F -"
      " chi_Fb) — the real Im-trace candidate direction",
      ok_split)

# the odd part i c sin(a)(chi_F - chi_Fb) = -2 c sin(a) Im(chi_F): a
# REAL-VALUED flip-odd function — the per-plaquette imaginary-trace
# direction, i.e. the naive single-plaquette lattice-theta candidate. The
# design-time claim that the odd part is an imaginary-action direction was
# REFUTED by this computation: at seed (single-plaquette) level the odd
# direction is a real reweighting. Any conclusion about sourcing a
# multi-plaquette theta phase through a flow is outside this runner.
ok_odd = True
for (t1, t2) in SAMPLE_T:
    odd = (weight_at(phased, t1, t2) - weight_at(phased, -t1, -t2)) / 2
    pred = -2 * 0.35 * np.sin(ALPHA) * char_at(1, 0, t1, t2).imag
    ok_odd = ok_odd and abs(odd - pred) < 1e-9 and abs(odd.imag) < 1e-9
check("D2 the odd seed direction is the REAL-VALUED per-plaquette"
      " imaginary-trace reweighting -2 c sin(a) Im(chi_F) — the naive"
      " single-plaquette theta candidate, NOT an imaginary action; flow"
      " sourcing of a multi-plaquette theta phase is outside this runner",
      ok_odd)

ok_det = True
for _ in range(4):
    z = RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))
    ph = np.angle(np.linalg.det(z))
    ph_bar = np.angle(np.linalg.det(np.conj(z)))
    same_mod_turn = (
        abs(ph_bar + ph) < 1e-12
        or abs(abs(ph_bar + ph) - 2 * np.pi) < 1e-12
    )
    ok_det = ok_det and same_mod_turn
check("D3 determinant phases are conjugation-ODD (arg det conj(M) ="
      " -arg det M): conjugation-asymmetric data of exactly the needed"
      " type live in determinant-phase structures — the mass side of the"
      " theta-bar assembly, not the pure-gauge seed surface", ok_det)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
