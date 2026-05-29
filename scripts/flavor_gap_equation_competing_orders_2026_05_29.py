#!/usr/bin/env python3
"""
The self-consistency / gap-equation crank on r=|b|^2/a^2: does the framework's
vacuum dynamics force the off-diagonal/diagonal ratio toward 1/2 (Q=2/3)?

Setup. The diagonal generation mass 'a' is the UNIFORM condensate <psi-bar psi>
(momentum 0); the off-diagonal corner-coupling 'b' (which splits the
generations) is the STAGGERED condensate at the corner-connecting momentum
Q=(pi,pi,0). We solve the coupled density-wave mean-field gap equation on the
full Wilson-Dirac propagator on Z^3 (4x4 in the (k,k+Q) x spinor basis) with a
single g_bare coupling, and read off r and Q=1/3+(2/3)r.

FINDINGS (mean-field, density-wave NJL interaction):
 1. A single democratic coupling G: ONLY the uniform condensate forms (a != 0,
    b = 0) at every G above threshold -> r = 0 -> Q = 1/3 (DEGENERATE). The
    generation-splitting condensate does not turn on.
 2. Even ENHANCING the staggered coupling (Gs/Gu up to 4): b stays 0 -- once the
    uniform condensate gaps the spectrum it suppresses the staggered channel.
 3. The pure-staggered branch (Gu=0) does not condense either (the off-diagonal
    tadpole largely cancels over the BZ). So uniform and staggered are
    COMPETING orders: generically ONE wins (here uniform -> r=0), not coexist.
 4. Q=2/3 <=> r=1/2 <=> b/a = 1/sqrt(2) requires COEXISTENCE of the two
    condensates in a fixed ratio -- a MULTICRITICAL point, which the generic
    mean-field dynamics does NOT select.

HONEST VERDICT: self-consistency does NOT force r=1/2. At mean-field it forces
r=0 (Q=1/3, degenerate) -- the same democratic default as free+Wilson and the
Jahn-Teller generic outcome. The value Q=2/3 corresponds to a uniform-staggered
condensate COEXISTENCE (multicritical) point at b/a=1/sqrt2. The wall is not
broken but LOCATED precisely: Q=2/3 is a multicritical (coexistence) condition,
not a generic vacuum. Caveats: (i) this is mean-field; (ii) the density-wave
contact interaction is a MODEL, not the derived framework action (the
'bridge-gap'). Whether the true action / beyond-mean-field fluctuations / an
enhanced symmetry at coexistence selects b/a=1/sqrt2 is the next, concrete,
open question -- multicritical points ARE sometimes symmetry-selected.
"""

import numpy as np

s = [np.array([[0, 1], [1, 0]], complex),
     np.array([[0, -1j], [1j, 0]], complex),
     np.array([[1, 0], [0, -1]], complex)]
I2 = np.eye(2, dtype=complex)
Q = np.array([np.pi, np.pi, 0.0])


def Wfree(k, m, r):
    W = m + r * sum(1 - np.cos(kk) for kk in k)
    return W * I2 + 1j * sum(s[mu] * np.sin(k[mu]) for mu in range(3))


def gap(Gu, Gs, a0, b0, m=0.1, r=1.0, L=10, iters=250):
    ks = 2 * np.pi * np.arange(L) / L
    kl = [np.array([kx, ky, kz]) for kx in ks for ky in ks for kz in ks]
    a, b = a0, b0
    for _ in range(iters):
        sa = sb = 0.0
        for k in kl:
            Ginv = np.block([[Wfree(k, m, r) + a * I2, b * I2],
                             [b * I2, Wfree(k + Q, m, r) + a * I2]])
            S = np.linalg.inv(Ginv)
            sa += np.real(np.trace(S[:2, :2]) + np.trace(S[2:, 2:])) / 2
            sb += np.real(np.trace(S[:2, 2:]) + np.trace(S[2:, :2])) / 2
        a = 0.5 * a + 0.5 * Gu * sa / len(kl)
        b = 0.5 * b + 0.5 * Gs * sb / len(kl)
    return a, b


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    sep("(1) single democratic coupling G -> uniform-only, r=0, Q=1/3")
    print("   G      a        b        r      Q")
    for G in [1.0, 2.0, 3.0, 5.0]:
        a, b = gap(G, G, 0.5, 0.4)
        r = (b / a) ** 2 if abs(a) > 1e-5 else 0.0
        print(f"   {G:.1f}   {a:+.4f}  {b:+.4f}   {r:.3f}  {min(1/3+2/3*r,1):.4f}")

    sep("(2) enhance the staggered coupling Gs/Gu -> b still 0 (uniform suppresses it)")
    print("   Gs/Gu   a        b        r")
    for ratio in [1.0, 2.0, 4.0]:
        a, b = gap(2.0, 2.0 * ratio, 0.5, 0.4)
        r = (b / a) ** 2 if abs(a) > 1e-5 else 0.0
        print(f"   {ratio:.1f}     {a:+.4f}  {b:+.4f}   {r:.3f}")

    sep("(3) pure-staggered branch (Gu=0) -> no condensation (competing orders)")
    for Gs in [3.0, 5.0]:
        a, b = gap(0.0, Gs, 0.0, 0.6)
        print(f"   Gs={Gs:.1f}: a={a:+.4f} b={b:+.4f}")

    sep("(4) r=1/2 (Q=2/3) is a uniform-staggered COEXISTENCE / multicritical point")
    print("   Q=2/3 <=> r=|b|^2/a^2 = 1/2 <=> b/a = 1/sqrt2 = 0.7071 (both condensates ON).")
    print("   Mean-field selects uniform-only (b=0); coexistence at b/a=0.707 is NOT generic.")

    sep("VERDICT")
    print("  Self-consistency does NOT force r=1/2. Mean-field forces r=0 (Q=1/3, degenerate)")
    print("  -- the democratic default again. Q=2/3 = uniform-staggered condensate coexistence")
    print("  (multicritical) at b/a=1/sqrt2; the generic dynamics does not select it. Wall not")
    print("  broken but LOCATED: 2/3 is a multicritical condition. Caveats: mean-field; the")
    print("  density-wave contact interaction is a MODEL, not the derived (bridge-gap) action.")
    print("  Next: does the true action / fluctuations / an enhanced symmetry at coexistence")
    print("  select b/a=1/sqrt2? (multicritical points are sometimes symmetry-selected).")


if __name__ == "__main__":
    main()
