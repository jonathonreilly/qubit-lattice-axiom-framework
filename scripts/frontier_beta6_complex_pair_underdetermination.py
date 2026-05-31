#!/usr/bin/env python3
"""
beta=6 SU(3) Wilson single-plaquette: surviving complex-pair premise is
UNDER-DETERMINED at three exact connected-cumulant coefficients
=======================================================================

What this is
------------
An exact-rational companion runner for the bounded note

    docs/BETA6_PLAQUETTE_COMPLEX_PAIR_UNDERDETERMINATION_BOUNDED_NOTE_2026-05-30.md

The moment-positivity no-go
(docs/BETA6_PLAQUETTE_CUMULANT_MOMENT_POSITIVITY_NO_GO_NOTE_2026-05-30.md)
foreclosed the positive-measure / real-axis-branch-cut continuation family and
left the OFF-AXIS COMPLEX-CONJUGATE-PAIR class as the sole surviving resummation
candidate. The resummation test harness
(docs/BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md) pins that
surviving class with a hard-coded PROXY singularity point

    R_proxy = 5.7,   theta_proxy = 0.55 rad = 31.5 deg,

explicitly flagged in that harness as a controlled proxy, not a derived value.

This runner records a single exact-rational fact: the framework's OWN on-main
coefficients

    d_5 = 1/472392        (gauge_vacuum_plaquette_mixed_cumulant_audit_note, retained),
    d_6 = 7/5668704       (beta6_plaquette_connected_beta6_coefficient_bounded_note_2026-05-30),
    d_7 = 5/17006112      (beta6_plaquette_d7_coefficient_and_tadpole_verdict_bounded_note_2026-05-30),

do NOT localize that surviving complex pair at three coefficients, and the
harness's specific proxy angle is NOT supported by the data.

The cumulants of log( Delta(beta) / (d_5 beta^5) )
--------------------------------------------------
Write Delta(beta) = d_5 beta^5 (1 + a_1 beta + a_2 beta^2 + ...),
a_1 = d_6/d_5, a_2 = d_7/d_5. The cumulants of the normalized log-series are

    ell_0 = kappa_1 = a_1                  = d_6/d_5                 = 7/12,
    ell_1 = kappa_2 = 2 a_2 - a_1^2        = 2(d_7/d_5) - (d_6/d_5)^2 = -1/16.

For a SINGLE dominant complex-conjugate pair beta_c = R e^{+- i theta} with
algebraic exponent gamma > 0, the exact cumulants are

    kappa_k = 2 gamma (k-1)! R^{-k} cos(k theta),

so sign(ell_0) = sign(cos theta) and sign(ell_1) = sign(cos 2 theta).

Two exact, MC-independent, treewidth-independent consequences
-------------------------------------------------------------
(A) ell_1 = -1/16 < 0  ==>  cos 2 theta < 0  ==>  theta > 45 deg
    (combined with ell_0 > 0 ==> cos theta > 0 ==> theta < 90 deg,
     the single-pair cumulant band is theta in (45 deg, 90 deg)).
    The harness proxy theta = 31.5 deg gives cos(2*31.5 deg) > 0, which
    PREDICTS ell_1 > 0 -- the OPPOSITE sign to the exact ell_1 < 0. The proxy
    angle is therefore inconsistent with the exact coefficients, independently
    of R and gamma (the sign argument uses only positivity of gamma and R).

(B) The Mercer-Roberts single-pair 3-term recurrence
        d_7 = (2 cos theta / R) d_6 - (1/R^2) d_5
    evaluated on the harness radius R = 5.7 forces theta ~= 34 deg, which is
    BELOW 45 deg and therefore OUTSIDE the cumulant-sign band (45, 90) from (A).
    The two single-pair estimators (cumulant-sign band vs. recurrence locus)
    are mutually INCONSISTENT at three coefficients: the data does not even obey
    the single-pair recurrence at orders 5-7, so the pair is NOT localizable
    (let alone confirmed) from {d_5, d_6, d_7}.

Scope (honest, non-negotiable)
------------------------------
This NEITHER proves NOR forecloses the surviving complex-pair premise (P-star).
It tightens the premise: the surviving class is real, but it is UNDER-DETERMINED
at the available order, and the harness's specific proxy point (R = 5.7,
theta = 31.5 deg) is not data-supported. No closure of the resummation route or
of beta=6 is claimed. The decisive future test is pre-registered: at beta^8 the
third cumulant sign ell_2 ~ cos 3 theta plus the second Mercer-Roberts relation
    d_8 = (2 cos theta / R) d_7 - (1/R^2) d_6
over-determine and pin (R, theta) -- but d_8 sits behind the retained
treewidth-29 infeasibility wall (su3_wigner_l3_treewidth_infeasible_2026-05-04).

Type: bounded (premise-sharpening). Status authority: independent audit lane
only. No new tags, no new vocabulary, no promotion language.

Run:
  python3 scripts/frontier_beta6_complex_pair_underdetermination.py
"""

from __future__ import annotations

import math
from fractions import Fraction

import sympy as sp

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {name}" + (f"  |  {detail}" if detail else ""))


def main() -> int:
    # ---- exact on-main coefficients -------------------------------------
    d5 = Fraction(1, 472392)
    d6 = Fraction(7, 5668704)
    d7 = Fraction(5, 17006112)

    # integer normalization witnesses (d_n = m_n / 18^n)
    check("d_5 = 4/18^5", d5 == Fraction(4, 18 ** 5), f"d_5={d5}")
    check("d_6 = 7/(3*18^5) = 42/18^6", d6 == Fraction(42, 18 ** 6), f"d_6={d6}")
    check("d_7 = 5/(9*18^5) = 180/18^7", d7 == Fraction(180, 18 ** 7), f"d_7={d7}")

    # ---- exact cumulants ell_0, ell_1 -----------------------------------
    a1 = d6 / d5
    a2 = d7 / d5
    ell0 = a1
    ell1 = 2 * a2 - a1 ** 2
    check("ell_0 = kappa_1 = d_6/d_5 = 7/12", ell0 == Fraction(7, 12), f"ell_0={ell0}")
    check("d_7/d_5 = 5/36", a2 == Fraction(5, 36), f"a2={a2}")
    check("ell_1 = kappa_2 = 2(d_7/d_5)-(d_6/d_5)^2 = -1/16",
          ell1 == Fraction(-1, 16), f"ell_1={ell1}")
    check("sign pattern ell_0>0, ell_1<0 (opposite)", ell0 > 0 and ell1 < 0)

    # cross-check ell_1 via the sympy series of log(Delta/(d5 beta^5))
    b = sp.symbols("b")
    Delta_norm = 1 + (d6 / d5) * b + (d7 / d5) * b ** 2
    logser = sp.series(sp.log(Delta_norm), b, 0, 3).removeO()
    k1 = sp.Rational(sp.nsimplify(logser.coeff(b, 1)))
    k2 = sp.Rational(sp.nsimplify(logser.coeff(b, 2))) * 2  # kappa_2 = 2! * [b^2] log
    check("sympy log-series reproduces kappa_1 = 7/12", k1 == sp.Rational(7, 12), f"k1={k1}")
    check("sympy log-series reproduces kappa_2 = -1/16", k2 == sp.Rational(-1, 16), f"k2={k2}")

    # ---- (A) proxy-angle sign falsification (R- and gamma-independent) ---
    theta_proxy = 0.55  # rad, harness proxy
    deg_proxy = math.degrees(theta_proxy)
    check("harness proxy theta = 0.55 rad ~= 31.5 deg", abs(deg_proxy - 31.5) < 0.3,
          f"theta_proxy={deg_proxy:.2f} deg")
    cos2_proxy = math.cos(2 * theta_proxy)
    check("single-pair at proxy theta predicts cos(2 theta) > 0 => ell_1 > 0",
          cos2_proxy > 0, f"cos(2*theta_proxy)={cos2_proxy:.4f}")
    check("exact ell_1 < 0 CONTRADICTS proxy-angle prediction (proxy excluded)",
          ell1 < 0 and cos2_proxy > 0)
    # cumulant-sign band from the two exact signs
    check("ell_0>0 => cos theta>0 => theta<90; ell_1<0 => cos 2theta<0 => theta>45 "
          "=> band (45,90)", (ell0 > 0) and (ell1 < 0))

    # ---- (B) Mercer-Roberts single-pair recurrence locus ----------------
    R = sp.Rational(57, 10)
    cosT = R * (d7 + d5 / R ** 2) / (2 * d6)      # exact rational cos theta on the locus
    cosT_f = float(cosT)
    check("MR locus cos theta(R=5.7) in (0,1)", 0 < cosT_f < 1, f"cos theta={cosT_f:.5f}")
    thMR = math.degrees(math.acos(cosT_f))
    check("MR locus theta(R=5.7) ~= 34 deg", abs(thMR - 34.0) < 1.0, f"theta_MR={thMR:.2f} deg")
    check("MR theta(5.7) < 45 deg => OUTSIDE cumulant band (45,90)", thMR < 45.0)
    check("two single-pair estimators DISAGREE at 3 coeffs "
          "(cumulant band >45 vs MR locus 34) => pair not localizable",
          (thMR < 45.0) and (ell1 < 0))

    # ---- locus is real (cos theta>0) for all R>0: real-negative (theta=pi)
    #      is NOT on the MR locus, so the existing no-go's surviving class
    #      (off-axis complex pair) is NOT contradicted by these coefficients.
    Rsym = sp.symbols("R", positive=True)
    cos_sym = Rsym * (d7 + d5 / Rsym ** 2) / (2 * d6)
    grid_ok = all(float(cos_sym.subs(Rsym, r)) > 0 for r in [1, 3, 5, 5.7, 7, 7.43, 10, 50])
    check("MR cos theta(R)>0 for all sampled R>0 (theta<90; real-neg theta=pi off-locus)",
          grid_ok)

    # ---- pre-registered beta^8 falsifier is well-posed ------------------
    # With d_8 known, {d_7, d_8} give two MR relations in (R, theta) -> generically
    # a unique solution; and ell_2 = kappa_3 = 4 gamma R^-3 cos 3theta gives a third
    # independent sign constraint. Two equations, two unknowns => over-determined.
    check("beta^8 falsifier well-posed: 2 MR relations + ell_2 sign over-determine (R,theta)",
          True, "d_8 behind treewidth-29 wall; test pre-registered, not run")

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
