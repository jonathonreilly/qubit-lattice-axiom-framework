#!/usr/bin/env python3
"""
Refinement of the Jahn-Teller route: what Q does the cubic-breaking actually
produce, and with what mass SPECTRUM? (Corrects an over-rosy 'passes 2/3'
reading: 2/3 is in the range but the natural patterns do NOT robustly deliver
the observed 3-distinct spectrum at 2/3.)

Setup: the cubic-breaking is TRACELESS (sum d_mu = 0), so the three generation
corner masses M_mu = M0 + d_mu always have FIXED MEAN M0. Then
Q = 3*M0 / (sum sqrt(M_mu))^2, and the full reachable range is [1/3, 1].

FINDINGS:
 (A) Energetically-preferred direction (one-axis-out, from the E_vac angular
     scan: minima at the 'A' = one-distinct directions): masses (M0+2a,M0-a,
     M0-a) -> TWO DEGENERATE generations. Sweeping toward criticality gives
     the GROSS lepton structure '1 heavy + 2 light' and passes Q=2/3 -- but
     at LEADING ORDER the two light generations are DEGENERATE (e=mu), which
     is NOT observed. The e-mu splitting needs a secondary, subleading breaking.
 (B) The simplest 3-DISTINCT pattern (M0+d, M0, M0-d) CAPS at Q=0.5 as the
     lightest -> 0. It does NOT reach 2/3. (This corrects a prior 'passes 2/3'
     claim that was actually reading off Q_max=0.515 for this pattern.)
 (C) A genuinely 3-distinct, steeply-hierarchical spectrum (~(2.85,0.15,~0))
     CAN give Q=2/3, but it is a FINE point in the traceless plane, NOT the
     energetically-cheapest direction.

HONEST NET: the Jahn-Teller instability is real and gives Q in [1/3,1], but
the value is NOT pinned to 2/3 -- it needs (i) the stiffness magnitude (the
fermion sea alone runs to maximal anisotropy) AND (ii) a pattern selection.
The cheapest pattern matches the gross '1 heavy + 2 light' structure and can
hit 2/3, but predicts degenerate light generations at leading order. So this
is a structural HINT with two concrete gaps (stiffness, e-mu splitting), not a
derivation of 2/3.
"""

import numpy as np
from scipy.optimize import brentq


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def Q(M):
    M = np.array(M, float)
    if M.min() < -1e-9:
        return np.nan
    return M.sum() / np.sqrt(np.abs(M)).sum() ** 2


def main():
    M0 = 1.0
    sep("(A) preferred 'one-axis-out' direction -> TWO DEGENERATE generations")
    print("    masses (M0+2a, M0-a, M0-a); sweep a/M0 -> criticality:")
    for x in [0.0, 0.3, 0.6, 0.9, 0.99, 1.0]:
        a = x * M0; M = np.array([M0 + 2 * a, M0 - a, M0 - a])
        deg = "  (two light DEGENERATE -- not e,mu,tau)" if x > 0 else ""
        print(f"      a/M0={x:.2f}: masses {np.round(M,3)}  Q={Q(M):.4f}{deg}")
    f = lambda x: (np.array([M0 + 2 * x, M0 - x, M0 - x]).sum()
                   / np.sqrt(np.array([M0 + 2 * x, M0 - x, M0 - x])).sum() ** 2 - 2 / 3)
    xs = brentq(f, 0.5, 0.999)
    Ms = np.array([M0 + 2 * xs, M0 - xs, M0 - xs])
    print(f"    Q=2/3 at a/M0={xs:.4f}: masses {np.round(Ms,4)} -- but the two light are EQUAL.")
    print("    => gross '1 heavy + 2 light' matches leptons; e-mu split needs secondary breaking.")

    sep("(B) simplest 3-DISTINCT pattern (M0+d,M0,M0-d) CAPS at Q=0.5 (not 2/3)")
    for x in [0.3, 0.6, 0.9, 1.0]:
        M = np.array([M0 + x, M0, M0 - x]); print(f"      d/M0={x:.2f}: masses {np.round(M,3)}  Q={Q(M):.4f}")
    print("    Q_max = 0.5147 as lightest -> 0. Corrects a prior 'passes 2/3' misread.")

    sep("(C) max Q over all traceless splits, requiring 3 DISTINCT (min gap g)")
    for g in [0.0, 0.05, 0.15]:
        bestQ, bestM = 0, None
        for d1 in np.linspace(-1, 2, 220):
            for d2 in np.linspace(-1, 2, 220):
                M = np.array([1 + d1, 1 + d2, 1 - d1 - d2])
                if M.min() < 0:
                    continue
                s = np.sort(M)
                if s[1] - s[0] < g or s[2] - s[1] < g:
                    continue
                q = Q(M)
                if q > bestQ:
                    bestQ, bestM = q, M
        print(f"      min-gap g={g:.2f}: max Q={bestQ:.4f} at masses {np.round(np.sort(bestM),3)}")
    print("    => 2/3 with a strict 3-distinct hierarchy is reachable but a FINE point.")

    sep("VERDICT (corrected, honest)")
    print("  Jahn-Teller instability is real; Q in [1/3,1]; value NOT pinned to 2/3.")
    print("  Needs (i) the stiffness magnitude (fermion sea alone -> maximal anisotropy)")
    print("  and (ii) a pattern selection. Cheapest pattern = '1 heavy + 2 light' (matches")
    print("  the GROSS lepton structure, passes 2/3) but gives DEGENERATE light gens at")
    print("  leading order (e=mu); simplest 3-distinct caps at 0.5. So: a structural HINT")
    print("  with two concrete gaps (stiffness; e-mu splitting), NOT a derivation of 2/3.")


if __name__ == "__main__":
    main()
