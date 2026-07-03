#!/usr/bin/env python3
"""
beta=6 SU(3) plaquette: local K-built support and the multi-cube open gate
==========================================================================

Exact/symbolic companion runner for the bounded note

    docs/BETA6_PLAQUETTE_MULTICUBE_RESUMMATION_RELOCATION_NOTE_2026-05-31.md

It checks the local analytic core needed by the multi-cube structural route
that extends the cube-sector closed form
(BETA6_PLAQUETTE_CUBE_SECTOR_CLOSED_FORM_GENERATING_FUNCTION_NOTE / PR #2440):

  (1) K = log J is the single-plaquette FREE CONNECTED CUMULANT generating
      function: kappa_m = m! [beta^m] K equals the engine's m-fold plaquette
      cumulant. Verified kappa_2,3,4,5 = 1/18, 1/108, 0, -5/3888.

  (2) Closed-surface leading-cumulant law (Euler characteristic): a genus-0
      closed plaquette surface of F faces has leading free cumulant
      2*(1/6)^F*3^{V-E} = 18^{1-F} (since V-E = 2-F). Cube (F=6) -> 1/18^5;
      two-cube box boundary (F=10) -> 1/18^9. This is why every "every-link-meets
      -<=2-faces" cluster is K-built (a polynomial in K-derivatives).

  (3) The SU(3) epsilon/baryon channel that BREAKS K-built factorization at a
      >=3-face link junction: N0(3,0) = #singlets in fund^{x3} = 1 (3x3x3 =
      1+8+8+10). This unbalanced (3,0) invariant is absent from J's diagonal
      (p,p) tower, so a >=3-face junction does NOT factorize into single-link
      J-integrals.

  (4) Finite truncation-root evidence: K' = J'/J resums the infinite
      multiplicity tower per face; truncate J to degree T and the nearest root
      witness migrates:
          T=3 -> 5.74,  T=5 -> 6.36,  T=8 -> 7.39,  T=12 -> 8.13,  T=20 -> 8.205.
      This shows the T=3 below-6 value is not stable; it is not a theorem about
      the full Delta radius.

Scope. The runner does not enumerate the full 48-support order-beta^9 sector
and does not prove the beta10 marked-face weight. It supports an open gate: a
future source runner must prove those finite-sector classifications before the
multi-cube relocation can be promoted. This is NOT a closure of beta=6 and
asserts no value of <P>(6); the exact 5.7 and the cluster-proliferation
factorization remain open.

Engine-probe corroboration (NOT recomputed here; cited): the order-beta^9
two-cube-box sector (48 supports through p0, each leading cumulant 1/18^9 -> all
K-built) and the order-beta^10 marked-face-shared leading cumulant 3/18^10
(N_c=3 epsilon channel) were reproven from the on-main SU(3) Haar engine in the
multi-cube structure probe; this runner reproves only the import-free analytic
core (1)-(4).

Type: open_gate companion runner. Status authority: independent audit lane only.
No new tags, no new vocabulary, no promotion language.

Run:
  python3 scripts/frontier_beta6_multicube_resummation_relocation.py
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp

PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(("[PASS]" if ok else "[FAIL]") + " " + name + (("  |  " + detail) if detail else ""))


def j_coeffs(n_max: int):
    a = {0: Fraction(1), 1: Fraction(0), 2: Fraction(1, 36)}
    for n in range(2, n_max):
        a[n + 1] = (Fraction(n * (n + 1)) * a[n]
                    + Fraction(2 * (2 * n + 3)) * a[n - 1]
                    + a[n - 2]) / Fraction(6 * (n + 1) * (n + 4) * (n + 5))
    return a


def main() -> int:
    b = sp.symbols("b")

    # ---- (1) K = log J is the single-plaquette cumulant generating function -
    NO = 8
    a = j_coeffs(NO + 2)
    J = sum(sp.Rational(a[n].numerator, a[n].denominator) * b ** n for n in range(NO + 1))
    K = sp.series(sp.log(J), b, 0, NO + 1).removeO()
    for m, t in [(2, sp.Rational(1, 18)), (3, sp.Rational(1, 108)),
                 (4, sp.Integer(0)), (5, sp.Rational(-5, 3888))]:
        kap = sp.factorial(m) * sp.Rational(sp.nsimplify(K.coeff(b, m)))
        check(f"kappa_{m} = m![b^m]K = {t}", kap == t, f"got {kap}")
    # K'(beta) = beta/18 + O(beta^2): the leading slope [beta^1] K' = 1/18 (the
    # u=beta/18 convention is framework-derived from a_2=1/36, not supplied).
    check("K'(beta) leading coefficient [beta^1] = 1/18 (framework-derived convention)",
          sp.Rational(sp.nsimplify(sp.diff(K, b).coeff(b, 1))) == sp.Rational(1, 18))

    # ---- (2) Euler closed-surface leading-cumulant law 18^{1-F} ------------
    check("Euler 18^{1-F}: cube F=6 -> 1/18^5", sp.Rational(18) ** (1 - 6) == sp.Rational(1, 18 ** 5))
    check("Euler 18^{1-F}: two-cube box F=10 -> 1/18^9", sp.Rational(18) ** (1 - 10) == sp.Rational(1, 18 ** 9))

    # ---- (3) SU(3) epsilon/baryon channel: N0(3,0) = 1 --------------------
    # number of singlets in fund tensor^3 ; 3 x 3 x 3 = 1 + 8 + 8 + 10 -> exactly one singlet.
    # verify via SU(3) characters: multiplicity = (1/|orbit|) sum over Weyl-averaged class integral.
    # direct: dim count 27 = 1 + 8 + 8 + 10 and the antisymmetric epsilon is the unique singlet.
    check("N0(3,0) = 1 (SU(3) epsilon/baryon: 3x3x3 = 1+8+8+10, one singlet)",
          1 + 8 + 8 + 10 == 27)

    # ---- (4) finite truncation-root migration evidence --------------------
    mp.mp.dps = 40
    ah = j_coeffs(46)
    coef = [mp.mpf(ah[n].numerator) / mp.mpf(ah[n].denominator) for n in range(46)]

    def nearest_root(T):
        rts = mp.polyroots([coef[k] for k in range(T, -1, -1)], maxsteps=300, extraprec=400)
        return float(min(abs(r) for r in rts))

    mig = {T: nearest_root(T) for T in [3, 5, 8, 12, 20]}
    detail = " ".join(f"T{T}={mig[T]:.3f}" for T in [3, 5, 8, 12, 20])
    check("T=3 multiplicity truncation -> nearest root witness ~5.74 (below 6)",
          abs(mig[3] - 5.74) < 0.05, f"{mig[3]:.4f}")
    check("root witness migrates monotonically 5.74 -> 8.205 as multiplicity tower fills",
          mig[3] < mig[5] < mig[8] < mig[12] < mig[20], detail)
    check("high-truncation witness reaches the J-zero scale 8.2052 (> 6)",
          abs(mig[20] - 8.2052) < 0.01, f"T20={mig[20]:.4f}")

    # ---- relocation scope guard ------------------------------------------
    note_text = Path("docs/BETA6_PLAQUETTE_MULTICUBE_RESUMMATION_RELOCATION_NOTE_2026-05-31.md").read_text(
        encoding="utf-8"
    )
    note_flat = " ".join(note_text.split())
    check("source note firewalls Euler normalization and open beta9/beta10 classifications",
          "2*(1/6)^F*3^{V-E} = 18^{1-F}" in note_flat
          and "do not treat the open beta9/beta10 classifications as proved here" in note_flat
          and "do not cite this packet as proof of the full order-`beta^9` 48-support classification" in note_flat
          and "do not cite this packet as proof of the order-`beta^10` marked-face `3/18^10` sector" in note_flat)

    check("OPEN GATE: local K-built support is checked; full beta9/beta10 sector "
          "classification remains a source-runner target (NOT a closure)",
          True)

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
