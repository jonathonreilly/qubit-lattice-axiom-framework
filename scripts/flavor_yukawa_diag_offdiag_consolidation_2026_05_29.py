#!/usr/bin/env python3
"""
Consolidation: chasing the 'e-mu splitting' gap of the Jahn-Teller route shows
it DISSOLVES, and the value question reduces (cleanly, again) to the single
retained modulus r=1/2 -- now with a concrete interpretation in the FULL
generation Yukawa.

The generation Yukawa Y on the 3 hw=1 corners decomposes into:
  - DIAGONAL part 'a'  : the corner masses (Wilson + diagonal condensate). The
    Jahn-Teller instability acts HERE (anisotropy = C3-breaking diagonal).
  - OFF-DIAGONAL part 'b' : the C3-symmetric corner<->corner coupling
    Y = a I + b C + conj(b) C^2 (C = 3-cycle).

Brannen: sqrt-mass_k = a + 2|b|cos(theta + 2pi k/3). Then
  Q = sum(m)/(sum sqrt m)^2 = 1/3 + (2/3) r,   r = |b|^2 / a^2,
EXACTLY and theta-INDEPENDENT (verified below). Consequences:

 1. The e-mu SPLITTING (the spread of the 3 sqrt-masses, i.e. which corner is
    e/mu/tau) is set by the phase theta = arg(b) -- and theta is EXACTLY
    Q-orthogonal (the retained Brannen delta). So the 'e-mu degeneracy gap'
    from the Jahn-Teller refinement is filled TRIVIALLY by the off-diagonal
    phase and does NOT advance the value question.

 2. The VALUE reduces, once more, to r = |b|^2/a^2 = 1/2  (= the retained
    biconditional koide_circulant_character_bridge, Q=2/3 <=> r=1/2). Now r has
    a concrete full-operator meaning: (off-diagonal corner-coupling)^2 /
    (diagonal corner-mass)^2.

 3. This UNIFIES the two gaps named in the Jahn-Teller note: both the 'stiffness'
    (which sets the diagonal scale a) and the off-diagonal coupling b are
    VACUUM/condensate quantities. Q=2/3 is the single statement that their
    ratio is 1/2 -- one nonperturbative target, not two.

Honest net: the Jahn-Teller (diagonal, C3-breaking) and Brannen (off-diagonal,
C3-symmetric) pictures are the diagonal and off-diagonal of the SAME Yukawa.
The value 2/3 is neither's alone: it is the off-diagonal/diagonal ratio = 1/2,
the same unforced modulus the whole campaign reduced to -- now a single ratio
of two vacuum condensates.
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def Q_signed(a, bmag, theta):
    k = np.arange(3)
    sm = a + 2 * bmag * np.cos(theta + 2 * np.pi * k / 3)  # signed Brannen sqrt-mass
    return (sm ** 2).sum() / sm.sum() ** 2, np.sort(sm)


def main():
    sep("(1) Q = 1/3 + (2/3) r EXACTLY, theta-INDEPENDENT (signed Brannen)")
    for r in [0.0, 0.25, 0.5, 1.0]:
        b = np.sqrt(r)
        qs = [Q_signed(1.0, b, th)[0] for th in np.linspace(0, 2 * np.pi, 24)]
        print(f"   r={r:.2f}: Q in [{min(qs):.4f},{max(qs):.4f}]   (1/3+2/3 r = {1/3+2/3*r:.4f})")

    sep("(2) e-mu splitting is the phase theta -- Q-orthogonal -- at r=1/2 (Q=2/3 fixed)")
    for th in [0.0, 0.3, 0.6, 1.0, 1.5]:
        q, sm = Q_signed(1.0, np.sqrt(0.5), th)
        print(f"   theta={th:.1f}: sqrt-masses={np.round(sm,3)}  Q={q:.4f}")
    print("   theta sweeps the spectrum across the full 3-distinct range; Q stays 2/3.")
    print("   => the 'e-mu degeneracy gap' is filled trivially by theta and does NOT")
    print("      help reach 2/3. The value is governed by r alone.")

    sep("(3) the value reduces to r=|b|^2/a^2 = 1/2 = (off-diag coupling)/(diag mass)^2")
    print("   matches retained biconditional koide_circulant_character_bridge.")
    print("   Jahn-Teller acts on the DIAGONAL (a, C3-breaking); the value 2/3 is the")
    print("   OFF-DIAGONAL/DIAGONAL ratio. Both a and b are vacuum/condensate quantities,")
    print("   so the 'stiffness' gap (sets a) and the coupling b are ONE nonperturbative")
    print("   target: Q=2/3 <=> their ratio is exactly 1/2.")

    sep("VERDICT")
    print("  Chasing the e-mu gap CONSOLIDATES rather than closes: e-mu splitting is the")
    print("  Q-orthogonal phase theta (dissolves the gap); the value 2/3 reduces -- cleanly,")
    print("  again -- to r=|b|^2/a^2=1/2, now interpreted as the ratio of the off-diagonal")
    print("  corner-coupling to the diagonal corner-mass in the full generation Yukawa, both")
    print("  vacuum condensates. One sharp nonperturbative target, not two gaps.")


if __name__ == "__main__":
    main()
