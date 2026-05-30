#!/usr/bin/env python3
"""
Bridge-gap attack, move 4: does the g_bare=1 matter DYNAMICS preserve the
covariant block-count measure (move 3, -> Q=2/3) or collapse it (-> Q=1/3)?
Separate the loop into its two effects.

RESULT: the one-loop fermion correction PRESERVES the block-count measure; the
collapse to Q=1/3 is a SEPARATE effect (the VEV/tadpole), which is suppressed for
LIGHT fermions -- and leptons are light.

(A) THE MEASURE (quadratic / polarization) -- PRESERVED.
The one-loop correction to the mass-operator measure in channel X is the bubble
Pi_X = Tr[G0 X G0 X], G0 = free generation propagator on the hw=1 corners. At free
level the three corners are DEGENERATE (same Wilson mass) so G0 = c*I_3, giving
    Pi_X = c^2 Tr(X^2)   =>   Pi_I : Pi_{J-I} = 3 : 6 = 1 : 2 = the bare HS ratio.
So the loop has the SAME channel ratio as the bare covariant Tr(M^2) measure:
    K_X^eff = Tr(X^2) (1 + g c^2) ∝ Tr(X^2)   =>   r^eff = 3/6 = 1/2 -> Q=2/3,
RG-STABLE for ANY coupling g, as long as G0 stays (near-)degenerate. The block-
count lean is preserved by the dynamics at the measure level -- NOT collapsed.

(B) THE VEV (linear / tadpole) -- the SEPARATE collapse.
The loop's LINEAR term (tadpole) drives the uniform condensate: b_VEV -> 0 (the
competing-orders / effective-potential result, 3 computations this session). So
the physical mass operator is M = a_VEV*I (uniform VEV) + dM (block-count
fluctuations). Eigenvalues of M:
   large a_VEV (HEAVY)  -> M ~ a_VEV*I + small dM -> nearly degenerate -> Q ~ 1/3
   small a_VEV (LIGHT)  -> M ~ dM (fluctuation-dominated) -> block-count -> Q ~ 2/3
Charged leptons are LIGHT (near-critical, small uniform VEV) -> fluctuation-
dominated -> the block-count measure governs -> Q ~ 2/3. (Heavier sectors -- up
quarks -- are more VEV-dominated, consistent with their weaker Koide adherence.)

HONEST CAVEATS: (1) the VEV-vs-fluctuation crossover is qualitative here; the
quantitative threshold needs the actual VEV and fluctuation scales from the
g_bare=1 matter action (open). (2) block-count is the EXPECTED/typical measure,
not a per-operator forcing. (3) one-loop, valid while G0 ~ degenerate. NET: the
move-3 lean (Q=2/3) SURVIVES the leading dynamics at the measure level, and the
lightness of the leptons is exactly the regime where the block-count measure --
not the uniform VEV -- sets the spectrum. A genuine, coherent native mechanism
connecting 'leptons are light' to 'leptons are Koide-perfect (Q=2/3)'.
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    J = np.ones((3, 3)); I = np.eye(3); B = J - I

    sep("(A) one-loop polarization preserves the block-count ratio (degenerate G0)")
    print("  G0 = c*I_3 (free corners degenerate) -> Pi_X = c^2 Tr(X^2):")
    print(f"    Pi_I (uniform)    = c^2 * {np.trace(I@I):.0f}")
    print(f"    Pi_(J-I) (stagg.) = c^2 * {np.trace(B@B):.0f}")
    print("    ratio 3:6 = 1:2 = bare HS ratio -> K^eff ∝ Tr(X^2) -> r^eff=1/2 -> Q=2/3 (RG-stable).")
    print("  near-degenerate G0=diag(1,1,1+d): ratio stays ~2 (block-count robust):")
    for d in [0.0, 0.1, 0.3]:
        G0 = np.diag([1, 1, 1 + d])
        pa, pb = np.trace(G0 @ I @ G0 @ I), np.trace(G0 @ B @ G0 @ B)
        print(f"    d={d}: Pi_b/Pi_a = {pb/pa:.4f}")

    sep("(B) the VEV/tadpole is the separate collapse; LIGHT -> fluctuation-dominated -> 2/3")
    print("  M = a_VEV*I (uniform condensate, b_VEV->0) + dM (block-count fluctuations).")
    print("  HEAVY (large a_VEV): M ~ a_VEV*I -> nearly degenerate -> Q~1/3.")
    print("  LIGHT (small a_VEV): M ~ dM (fluctuations) -> block-count -> Q~2/3.")
    # illustrate: Q as the uniform VEV shrinks relative to a fixed block-count fluctuation.
    # ev = sqrt-masses (Yukawa eigenvalues); masses = ev^2; Q = sum(masses)/(sum sqrt-masses)^2.
    print("  illustration: block-count fluctuation (a_f=1, b_f=1/sqrt2) on a uniform VEV v:")
    for v in [4.0, 1.0, 0.2, 0.0]:
        a, b = v + 1.0, 1 / np.sqrt(2)
        ev = np.array([a + 2 * b, a - b, a - b])   # sqrt-masses
        Q = (ev ** 2).sum() / ev.sum() ** 2
        print(f"    VEV v={v:.1f}: sqrt-masses {np.round(ev,3)}  Q={Q:.4f}")

    sep("VERDICT")
    print("  The loop PRESERVES the block-count measure (Q=2/3) at the quadratic level (degenerate")
    print("  G0 -> Pi ∝ Tr X^2). The collapse to Q=1/3 is the SEPARATE uniform-VEV/tadpole, which")
    print("  dominates only for HEAVY fermions. Leptons are LIGHT -> fluctuation-dominated -> the")
    print("  block-count measure sets Q -> 2/3. Native mechanism linking lepton lightness to Koide")
    print("  Q=2/3. Caveats: qualitative crossover (needs matter-action scales); expected measure;")
    print("  one-loop. The move-3 lean survives the dynamics; the open piece is the VEV/fluctuation")
    print("  scale ratio from the g_bare=1 matter action.")


if __name__ == "__main__":
    main()
