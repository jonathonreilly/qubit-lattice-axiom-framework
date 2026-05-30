#!/usr/bin/env python3
"""
Route-2 full-court-press verdict (workflow wf_4e4fcccb) + corrections to this
session's moves 4 and 6, all verified independently here.

ROUTE 2 (is the light-lepton sector dynamically at the chiral-critical point ->
a_VEV->0 -> Q=2/3, import-free?) -> REFUTED as a route to the VALUE, with one
genuine new positive. Three verified facts:

(KILL 1) The chiral-critical endpoint a_VEV->0 does NOT give Q=2/3 -- it gives
Q->infinity. In the physical signed-eigenvalue (Brannen) readout, M=aI+b(J-I) has
sqrt-masses {a+2b, a-b, a-b} with sum = 3a; as a->0 the signed sum ->0 and
Q = sum(m)/(sum sqrt-m)^2 -> infinity (verified: a=1e-4, b=1/sqrt2 -> Q~3e7).
Q=2/3 sits at the FINITE INTERIOR ratio b/a=1/sqrt2 (r=1/2), which NO chiral
symmetry protects. => my move-6 capstone CONFLATED two decompositions: 'a_VEV=0
=> Q=2/3' holds only where a is the zero-MEAN chiral order parameter
(a=(1/3)Tr M, gated by the generation Gamma_chi import), NOT where a is the
uniform sqrt-mass (eigenvalue readout). RETRACTED.

(KILL 2) Koide Q is SCALE-INVARIANT: Q(c*m)=Q(m) for all c. So lepton lightness
(an overall-scale fact, m_e/M_Pl~1e-23) cannot move Q at all. => my move-4
'leptons light -> fluctuation-dominated -> Q->2/3' mechanism is WRONG. RETRACTED.
(The move-3 result that the covariant Tr(M^2) measure realizes the block-count/
SECTOR measure -> r=1/2 stands as a MEASURE statement; only the lightness/VEV
*dynamical application* in moves 4 & 6 is retracted.)

(POSITIVE, genuinely new) The framework's NATIVE fermion operator is STAGGERED,
not Wilson: it carries the exact spacetime sublattice chiral grading
eps(x)=(-1)^(x+y+z) with {eps,D}=0 (retained cpt_exact_note) + emergent gamma5 at
d=3+1 (retained clifford_volume_chirality). The native staggered condensate is
EXACTLY ODD in the mass (chiral-critical at m=0, NO tuning); the Wilson condensate
has an additive piece (needs m->kappa_c tuning). This chiral symmetry is SPACETIME
(native), genuinely DISTINCT from the generation-Gamma_chi import -- so Route 2 is
import-free ON THE CHIRALITY AXIS (new). BUT eps is generation-BLIND (S3-invariant
on the hw=1 orbit) so it cannot split the C3 orbit to select a vs b; and (Kill 1)
the value isn't at the critical endpoint anyway. METHODOLOGICAL FLAG: this
session's three 'vacuum -> Q=1/3' computations used the WILSON propagator (the
wrong, chiral-breaking operator class) and should be re-run on the staggered
operator before any broken-phase no-go stands.

CLEAN RELOCATION (the value question, sharpened): Q=2/3 is the interior ratio
b/a=1/sqrt2 = r=1/2, and lightness / criticality / the uniform VEV are all RED
HERRINGS (Q scale-invariant; criticality gives Q->inf). The ONLY thing that sets
the value is whether mass generation weights the C3 isotypes by TRACE (->Q=1) or
SECTOR-count (->Q=2/3) at the operator level. Move 3 (covariant matrix-field
measure -> SECTOR/block-count -> 2/3) is the live native lean on exactly this
gate; it is the surviving core, untouched by the corrections.
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def Q_signed(a, b):
    ev = np.array([a + 2 * b, a - b, a - b])
    return (ev ** 2).sum() / ev.sum() ** 2


def main():
    sep("(KILL 1) a_VEV->0 gives Q->infinity, NOT 2/3 (move-6 conflation retracted)")
    for a in [1.0, 0.5, 0.1, 1e-2, 1e-4]:
        ev = np.array([a + 2 / np.sqrt(2), a - 1 / np.sqrt(2), a - 1 / np.sqrt(2)])
        print(f"   a={a:.0e}: sum sqrt-m={ev.sum():.4f}  Q={Q_signed(a,1/np.sqrt(2)):.4g}")
    print("   Q=2/3 only at finite a with b/a=1/sqrt2; a->0 -> Q->inf (signed cancellation).")

    sep("(KILL 2) Koide Q is scale-invariant (move-4 lightness mechanism retracted)")
    m = np.array([0.511, 105.66, 1776.86])
    Qm = lambda mass: mass.sum() / np.sqrt(mass).sum() ** 2
    for c in [1e-20, 1.0, 1e10]:
        print(f"   masses x {c:.0e}: Q={Qm(m*c):.8f}")
    print("   identical -> lightness (overall scale) cannot move Q.")

    sep("(POSITIVE) native STAGGERED condensate is odd (critical at m=0); Wilson is not")
    L = 16; ks = 2 * np.pi * np.arange(L) / L
    KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing="ij")
    s2 = np.sin(KX) ** 2 + np.sin(KY) ** 2 + np.sin(KZ) ** 2
    for mm in [0.1, -0.1]:
        cond_s = (mm / (mm ** 2 + s2)).mean()
        W = mm + ((1 - np.cos(KX)) + (1 - np.cos(KY)) + (1 - np.cos(KZ)))
        cond_w = (W / (W ** 2 + s2)).mean()
        print(f"   m={mm:+.1f}: staggered={cond_s:+.4f} (odd)   Wilson={cond_w:+.4f} (additive)")
    print("   => the 3 session 'vacuum->Q=1/3' computations used Wilson; re-run on staggered.")

    sep("VERDICT")
    print("  Route 2 REFUTED as a route to the value: the chiral-critical endpoint (a->0)")
    print("  gives Q->inf, and Q is scale-invariant so lightness is irrelevant. The chiral")
    print("  symmetry is native SPACETIME (new, import-free) but generation-blind and the")
    print("  wrong coordinate. CORRECTIONS: moves 4 (lightness) & 6 (a_VEV=0->2/3) RETRACTED;")
    print("  the 3 Q=1/3 computations are Wilson-based (suspect). CLEAN RELOCATION: the value")
    print("  is the interior ratio b/a=1/sqrt2 = the TRACE-vs-SECTOR measure question; move 3")
    print("  (covariant measure -> SECTOR -> 2/3) is the surviving live lean on it.")


if __name__ == "__main__":
    main()
