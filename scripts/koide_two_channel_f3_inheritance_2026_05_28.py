#!/usr/bin/env python3
"""
Two-channel structure of the Koide F1 selection: KINEMATIC and DYNAMICAL
both reduce to the SAME dimension-counting measure and give F3 (r=1, Q=1).

Unifying insight (this runner): a free / Gaussian / quadratic dynamical
action on the generation sector IS the flat dimension-counting measure on
(a, Re b, Im b). Equipartition of that action over the 3 real modes gives
the doublet (2 real modes) twice the trivial (1 real mode) -> r=1 = F3,
EXACTLY the kinematic dimension-weighting. So DYNAMICS INHERITS the
kinematic no-go; it does not escape it. The interacting correction is
provably far too small to bridge F3 -> F1.

Consolidates: kinematic no-go (KOIDE_F1_KINEMATIC_NO_GO_NOTE_2026-05-28)
+ dynamical probes 5/21/25/28 + Z^3 scalar potential (m_V != m_*).
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def Q_of_r(r):
    return 1.0 / 3.0 + (2.0 / 3.0) * r


def main():
    sep("(1) FREE/QUADRATIC action equipartition over (a, Re b, Im b) -> F3")
    print("  Generation sector has 3 REAL modes: a (trivial), Re b, Im b (doublet).")
    print("  A free/Gaussian (quadratic) action weights each real mode equally")
    print("  (equipartition: <energy> = kT/2 per quadratic dof). With total")
    print("  energy N split equally over 3 real modes:")
    N = 1.0
    e_per_mode = N / 3
    E_plus = 1 * e_per_mode          # trivial: 1 real mode
    E_perp = 2 * e_per_mode          # doublet: 2 real modes
    # E_+ = 3 a^2, E_perp = 6 |b|^2  =>  a^2 = E_+/3, |b|^2 = E_perp/6
    a2 = E_plus / 3
    b2 = E_perp / 6
    r = b2 / a2
    print(f"    E_+ (trivial, 1 mode) = {E_plus:.4f}")
    print(f"    E_perp (doublet, 2 modes) = {E_perp:.4f}   (ratio 1:2)")
    print(f"    => r = |b|^2/a^2 = {r:.4f}   Q = {Q_of_r(r):.4f}   = F3 (Q=1)")
    print("  This is the Probe 25 result: free dynamics lands at F3, NOT F1.")
    print("  KEY: the quadratic action = the FLAT dimension measure. The")
    print("  doublet's 2 real modes each get an equal share, so it weighs 2.")
    print("  F1 (r=1/2) needs the 2 real modes to SHARE one mode's worth =")
    print("  count the complex block ONCE = the same un-supplied (1,1) primitive.")

    sep("(2) the interacting correction is far too small to reach F1")
    gap_r = abs(1.0 - 0.5)            # F3 r=1 vs F1 r=1/2
    gap_Q = abs(Q_of_r(1.0) - Q_of_r(0.5))   # Q=1 vs Q=2/3
    vertex = 0.0072                  # Probe 28 alpha_bare * alpha_LM
    print(f"  F3->F1 gap in r:  |1 - 1/2| = {gap_r:.3f}")
    print(f"  F3->F1 gap in Q:  |1 - 2/3| = {gap_Q:.4f}")
    print(f"  Probe 28 interacting vertex magnitude ~ {vertex}")
    print(f"  ratio vertex / gap_Q ~ {vertex/gap_Q:.4f}  (<< 1)")
    print("  => the perturbative interacting correction cannot move F3 to F1.")

    sep("(3) RG / lattice flow: r=1/2 is non-stationary or unselected")
    print("  Probe 5 (RG): beta(r=1/2) ~ -0.036 != 0  -> 1/2 NOT a fixed point;")
    print("                stationary points are elsewhere (e.g. r: 1.0 -> 1.0).")
    print("  Probe 21 (native lattice flow): r=1/2 IS a fixed point but is NOT")
    print("                selected ('no-selection' -- the flow is neutral on (a,b)).")
    print("  Z^3 scalar potential (2026-04-19): V_eff minimum at m_V ~ -0.433,")
    print("                physical point m_* ~ -1.161 -- minimum at the WRONG point.")

    sep("(4) TWO-CHANNEL STRUCTURE: both channels are the same measure")
    print("  KINEMATIC channel: how to COUNT the doublet irrep in the measure.")
    print("    reality/modular/Jordan all count it as 2 real dims -> F3. (no-go)")
    print("  DYNAMICAL channel: equipartition of the quadratic action over the")
    print("    real modes ALSO counts the doublet as 2 -> F3. (probes 25/28/5/21)")
    print("  These are NOT independent: a free/Gaussian action IS the flat")
    print("  dimension measure. Dynamics INHERITS the kinematic dimension-count.")
    print("  Both channels land at F3 (r=1, Q=1) and both lack the SAME single")
    print("  ingredient: the (1,1)-multiplicity / 'count the complex block once'")
    print("  primitive. It is supplied by neither kinematics nor dynamics.")

    sep("(5) POSITIVITY-CONE result: r=1/2 is STRICTLY INTERIOR (import-free)")
    print("  reality-respecting (real-b) circulant eigenvalues (sqrt-masses):")
    print("    lambda = {a+2b, a-b, a-b}  (doublet a-b is 2-fold degenerate).")
    a = 1.0
    for b in [0.0, 0.5, 1.0]:
        lam = sorted([a + 2 * b, a - b, a - b])
        r = b**2 / a**2
        print(f"    b={b:.2f} (r={r:.2f}): eigenvalues {lam}  Q={Q_of_r(r):.4f}")
    print("  positivity (sqrt-masses >= 0) boundaries: r=0 (b=0, Q=1/3) and")
    print("  r=1 (b=a, the DOUBLET mode a-b goes MASSLESS, Q=1=F3).")
    print("  => r=1/2 (Q=2/3) is STRICTLY INTERIOR to the positive cone, so NO")
    print("     reflection-positivity / unitarity / BPS SATURATION can land on")
    print("     it (saturation hits a boundary). Import-free; points AWAY from F1.")

    sep("VERDICT (two-channel hunt complete: 0/5 dynamical corners reach F1)")
    print("  On A1+A2+retained the charged-lepton generation carrier natively")
    print("  selects F3 (r=1, Q=1), NOT F1 (r=1/2, Q=2/3), on BOTH channels:")
    print("   KINEMATIC: settled no-go (modular trivial, EJA rank-3, reality")
    print("     keeps {w,wbar} two equal modes).")
    print("   DYNAMICAL: free/Gaussian determinant (1/2)logdet K = (1/2)[1*logE+")
    print("     + 2*logE_perp] IS the dimension measure -> F3; interacting too")
    print("     small; theta only rotates arg(b); instanton fugacity sweeps r->1;")
    print("     gap-eqn democratic kernel -> r=1; positivity saturates on the")
    print("     boundary, never the interior r=1/2; index quantizes the COUNT")
    print("     (d=3) not the ratio r.")
    print("  THEOREM: dynamics INHERITS the kinematic dimension-count (the")
    print("  quadratic action = the dimension measure) -- not two chances at F1,")
    print("  one chance counted twice. Q=2/3 needs the (1,1) complex-multiplicity")
    print("  primitive, supplied by NEITHER channel.")
    print("  SINGLE UNCOVERED ESCAPE (non-fitting): A1 = M_2(C) = Cl(3,0) is a")
    print("  COMPLEX algebra; the campaign assumed the REAL measure throughout.")
    print("  Open question = does A1's intrinsic complex structure J CANONICALLY")
    print("  FORCE the holomorphic/Kahler measure that counts the doublet as ONE")
    print("  complex unit (collapsing U(1)_b as a complex-structure gauge)? If")
    print("  yes -> F1; if no -> framework is F3-native. (= ND4 of the sister")
    print("  weight-audit; the two lanes converge on the SAME residual.)")


if __name__ == "__main__":
    main()
