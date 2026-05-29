#!/usr/bin/env python3
"""
Re-attack (A1+A2-internal): does VACUUM-SELECTION via the framework's native
RECORDS (Lueders) + PRE-RECORD reference (rho_ref democratic) + PERSISTENCE
(self-maintaining) primitives select the charged-lepton mass pattern to
Q = 2/3 (r = |b|^2/a^2 = 1/2)?

Q = purity of the sqrt-mass-fraction distribution p (Q = sum_k p_k^2).
Endpoints fixed by the framework:
  pre-record (rho_ref, democratic) p=(1/3,1/3,1/3) -> Q = 1/3 (Q_min)
  full record (collapse to one generation)         -> Q = 1   (Q_max)

VERDICT: reduces to the SAME gap. The record dynamics has fixed points at
Q=1/3 (democratic, UNSTABLE) and Q=1 (collapse, STABLE). Q=2/3 is the
intermediate record-amount t = 1/sqrt(2) (= r=1/2 in disguise), NOT a fixed
point and NOT forced; A1-balanced (equal record/relax) gives Q=1/2, not 2/3.
"""

import numpy as np


def purity(p):
    p = np.array(p, float); p = p / p.sum()
    return float((p * p).sum())


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    sep("(1) record-mixture: pre-record (democratic) <-> full collapse")
    print("  p(t) = (1-t)*(1/3,1/3,1/3) + t*(1,0,0);  Q(t) = purity(p) = (1+2t^2)/3")
    for t in [0, 0.25, 0.5, 1/np.sqrt(2), 1.0]:
        p = (1 - t) * np.array([1, 1, 1]) / 3 + t * np.array([1., 0, 0])
        flag = "  <-- Q=2/3" if abs(purity(p) - 2/3) < 1e-3 else ""
        print(f"    t={t:.4f}: Q={purity(p):.4f}{flag}")
    print("  Q=2/3 <=> t=1/sqrt(2): the same sqrt2 / r=1/2 number, unforced.")

    sep("(2) fixed-point structure of the record (sharpening) map p -> p^2/Z")
    print("  Lueders sharpening drives purity UP. Fixed points & stability:")
    # democratic is a fixed point; perturb to show instability
    for label, p0 in [("democratic (exact)", [1/3, 1/3, 1/3]),
                      ("democratic + tiny tilt", [0.34, 0.33, 0.33])]:
        p = np.array(p0, float); p /= p.sum()
        traj = [purity(p)]
        for _ in range(40):
            p = p * p; p /= p.sum()
            traj.append(purity(p))
        print(f"    {label:24s}: Q {traj[0]:.4f} -> {traj[-1]:.4f}")
    print("  => Q=1/3 (democratic) is an UNSTABLE fixed point; any tilt flows to")
    print("     Q=1 (collapse, STABLE). Q=2/3 is NEITHER a fixed point. No native")
    print("     record dynamics parks the pattern at 2/3.")

    sep("(3) A1-balanced record (equal record vs relax-to-rho_ref) -> Q=1/2")
    p = 0.5 * np.array([1, 1, 1]) / 3 + 0.5 * np.array([1., 0, 0])
    print(f"    balanced t=1/2: Q={purity(p):.4f}  (=1/2, NOT 2/3)")
    print("  One qubit / one bit of record (the A1-natural 'balance') gives 1/2,")
    print("  not 2/3. Reaching 2/3 needs the special t=1/sqrt(2) record-amount.")

    sep("VERDICT: records/persistence reduces to the SAME gap")
    print("  Vacuum-selection via rho_ref + Lueders records + persistence drives")
    print("  Q to 1/3 (no record) or 1 (full record); 2/3 is the intermediate")
    print("  record-amount t=1/sqrt(2) = r=1/2, which is NOT a fixed point and is")
    print("  NOT forced by A1+A2 (A1-balanced records give 1/2). So the 5th lens")
    print("  (records/persistence) joins kinematic/dynamical/quantum/chiral: all")
    print("  reduce to the single unforced number r=1/2. The gap is unchanged.")


if __name__ == "__main__":
    main()
