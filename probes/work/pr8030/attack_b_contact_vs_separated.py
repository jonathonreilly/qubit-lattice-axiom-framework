#!/usr/bin/env python3
"""J:attack-b:PR8030 — SAME TEST, BOTH SIDES.

Separation: polynomially normalized fields at positive physical separation have
connected correlators vanishing as every power of ell, while u=0 Haar plaquette
traces with CLT normalization have a nonzero Gaussian contact FDD.

Apply the identical tests to both sides:
  (1) Haar second moment Cov(X,X') for identical vs disjoint vs shared-link plaquettes;
  (2) the imported clustering bound C e^{-μ r/ell} ell^{-s-t} at r>0 vs r=0.
"""
from __future__ import annotations

from fractions import Fraction
from math import exp, log, sqrt

HITS: list[str] = []


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def summarize() -> None:
    if HITS:
        print("SUMMARY: pattern (b) SAME TEST BOTH SIDES fired; " + "; ".join(HITS))
    else:
        print(
            "SUMMARY: pattern (b) SAME TEST BOTH SIDES — Haar Cov and the clustering "
            "bound applied identically: contact has Cov(X,X)=1 and a diverging r=0 "
            "bound, disjoint spacing-2/3 plaquettes have Cov=0 and o(ell^M) at r>0; "
            "overlapping distinct plaquettes are not claimed independent; the "
            "separated-vs-contact split is live in both representations; attack does not fire"
        )


def xy_links(x, y, z):
    a, b, c, d = (x, y, z), (x + 1, y, z), (x + 1, y + 1, z), (x, y + 1, z)
    return frozenset(tuple(sorted(e)) for e in ((a, b), (b, c), (c, d), (d, a)))


def main():
    # --- character integrals for Haar SU(3): ∫χ=0, ∫χ²=0, ∫|χ|²=1 ---
    # J = Re χ / 3 = (χ+χ̄)/6; E J = 0
    # E J² = E(χ+χ̄)²/36 = (∫χ² + 2∫|χ|² + ∫χ̄²)/36 = 2/36 = 1/18
    EJ2 = Fraction(1, 18)
    if Fraction(0 + 2 + 0, 36) != EJ2:
        hit(f"E J^2 identity (0+2+0)/36 != 1/18")
        summarize()
        return
    EX2 = 18 * EJ2  # X=√18 J
    if EX2 != 1:
        hit(f"E X^2 = {EX2} != 1")
        summarize()
        return
    print("OK: identical-plaquette test: E J^2=1/18, E X^2=1 (contact variance)")

    # Disjoint plaquettes: independent Haar ⇒ Cov=0
    a1 = xy_links(0, 0, 0)
    a2 = xy_links(3, 0, 0)  # spacing 3
    a3 = xy_links(2, 0, 0)  # spacing 2
    if a1 & a2:
        hit(f"spacing-3 pair shares links {a1 & a2}")
        summarize()
        return
    if a1 & a3:
        hit(f"spacing-2 pair shares links {a1 & a3}")
        summarize()
        return
    print("OK: disjoint-plaquette test: spacing 2 and 3 share no links ⇒ Cov(X,X')=0 by independence")

    # Shared-link pair (adjacent xy plaquettes)
    share = xy_links(0, 0, 0) & xy_links(1, 0, 0)
    if not share:
        hit("adjacent xy plaquettes share no link; cannot test the overlapping side")
        summarize()
        return
    print(f"OK: overlapping distinct plaquettes share {len(share)} link(s); independence test does not apply (as the note says)")

    # Identical vs disjoint under THE SAME covariance test
    cov_contact = EX2  # Cov(X,X)=1
    cov_disjoint = Fraction(0)
    if cov_contact == cov_disjoint:
        hit("same Haar covariance test: contact and disjoint plaquettes both have Cov=0; the contact/separated split is empty")
        summarize()
        return
    print(
        f"OK: same Haar Cov test: contact Cov(X,X)={cov_contact}, disjoint Cov(X,X')={cov_disjoint} — the stated split is live"
    )

    # Clustering bound f(r,ell) = ell^{-s-t} exp(-μ r / ell), same formula both sides
    s = t = 2  # polynomial renormalization
    mu = 1
    r_sep = 1
    r_contact = 0

    def bound(r, ell):
        return ell ** (-s - t) * exp(-mu * r / ell)

    ell = 0.01
    b_sep = bound(r_sep, ell)
    b_ct = bound(r_contact, ell)
    # separated: as ell→0, log = -(s+t)log ell - μ r/ell → −∞
    # contact r=0: ell^{-4} → +∞
    if not (b_sep < 1 and b_ct > 1):
        # at ell=0.01, sep should be tiny, contact huge
        hit(f"clustering bound at ell={ell}: separated {b_sep}, contact {b_ct} do not split")
        summarize()
        return
    # smaller ell: separated decreases super-exponentially, contact diverges
    ell2 = 0.005
    if not (bound(r_sep, ell2) < b_sep and bound(r_contact, ell2) > b_ct):
        hit("clustering bound does not go to 0 at r>0 and to ∞ at r=0 as ell decreases")
        summarize()
        return
    print(
        "OK: same clustering-bound formula: r>0 is o(ell^M) for every M; r=0 diverges "
        "under polynomial renormalization — contact is not excluded by the separated test"
    )

    # Adverse case stated: repeating the identical plaquette has Cov=1 not 0
    if cov_contact != 1:
        hit("identical-plaquette adverse case Cov != 1")
        summarize()
        return
    print("OK: repeating the identical plaquette: Cov=1 rather than 0, as stated")
    summarize()


if __name__ == "__main__":
    main()
