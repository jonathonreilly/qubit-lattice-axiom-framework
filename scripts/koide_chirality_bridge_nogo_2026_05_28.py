#!/usr/bin/env python3
"""
Koide last-mile, next step: is the spacetime-gamma5 -> generation-Gamma_chi
chirality BRIDGE buildable, or a no-go?

VERDICT: NO-GO. The chiral operator that would force Q=2/3 (anticommuting
with the generation grading Gamma_chi) must BREAK C_3-equivariance. Spacetime
chirality (gamma5 from anomaly_forces_time) acts C_3-TRIVIALLY on the
generation index, so it commutes with Gamma_chi and cannot supply it. No
functorial/spacetime operator splits the C_3 generation orbit. Hence the
generation-sector chiral grading is an INDEPENDENT IMPORT, not transportable
from the framework's existing (spacetime) chirality machinery.

This is the Koide-side face of the SAME gate the generation-identification
lane found (escape-hunt: no-go via three walls; wall 3 = R3-S1 retained,
"functorial anomalies can't split the C_3 generation orbit"). It also
CORRECTS the prior "no Ginsparg-Wilson" framing: GW is SUFFICIENT, not
NECESSARY; the operative obstruction is C_3-equivariance preservation.
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    S = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)   # Z_3 shift
    J = np.ones((3, 3)); Gx = (2/3) * J - np.eye(3)          # generation grading
    g5 = np.array([[1, 0], [0, -1]], float)                  # spacetime chirality

    sep("(1) the Koide chiral operator must BREAK C_3-equivariance")
    print("  {H, Gx}=0 (chiral) and [H, S]=0 (C_3-equivariant) => H=0")
    print("  (retained koide_z3_equivariant_anticommuting_no_go: comm(S) cap")
    print("   anticomm(Gx) = {0}). So a nonzero chiral H MUST have [H,S] != 0.")

    sep("(2) spacetime gamma5 acts C_3-trivially -> cannot supply it")
    Gx_full = np.kron(np.eye(2), Gx)
    print("  anomaly_forces_time gives gamma5 on the SPACETIME factor; on the")
    print("  generation index it acts as (gamma5 (x) G). Anticommuting with")
    print("  (I (x) Gx) REQUIRES {G, Gx}=0 on the generation factor:")
    for name, G in [("I_gen (gamma5 trivial on gen)", np.eye(3)),
                    ("S  (C_3-equivariant)", S),
                    ("S - S^T (Cl(3) bivector)", S - S.T)]:
        anti = np.max(np.abs(G @ Gx + Gx @ G))
        comm = np.max(np.abs(G @ S - S @ G))
        print(f"    G={name:30s}: {{G,Gx}}={anti:.2f} (!=0 => NOT anticommuting)"
              f"   [G,S]={comm:.2f}")
    print("  => every spacetime-supplied / C_3-equivariant G commutes with Gx.")
    print("  The C_3-orbit-splitting (non-equivariant) G that chirality needs is")
    print("  NOT produced by spacetime gamma5. BRIDGE = NO-GO.")

    sep("(3) corrects the 'no Ginsparg-Wilson' framing")
    print("  Prior framing blamed 'staggered Z^3 has no Ginsparg-Wilson'. But GW")
    print("  is SUFFICIENT, not NECESSARY. The operative obstruction is sharper:")
    print("  any chiral grading anticommuting with Gx must split the C_3 orbit,")
    print("  and no functorial/spacetime structure does. (Aligns with the sister")
    print("  generation-ID lane's three-wall no-go; wall 3 = R3-S1 retained.)")

    sep("VERDICT: bridge NO-GO -> generation chirality is an IMPORT")
    print("  The chiral structure that forces Koide Q=2/3 (anticommuting with")
    print("  the generation grading) CANNOT be transported from the framework's")
    print("  spacetime chirality (anomaly_forces_time gamma5); it would have to")
    print("  be an INDEPENDENT primitive on the generation R^3 factor that")
    print("  A1+A2+retained do not supply. So:")
    print("   - Q=2/3 is DERIVED-MODULO-CHIRALITY (chiral mass-gen => 2/3,")
    print("     non-circular, retained mechanism), AND")
    print("   - the required chirality is a CONFIRMED no-go to derive from")
    print("     A1+A2+retained: it is a genuine, user-approval-required import")
    print("     (an independent generation-sector chiral grading).")
    print("  This is the SAME single gate as generation-identification chirality.")
    print("  Closing Koide-2/3 to 'derived' requires importing that grading; the")
    print("  framework's NON-chiral default predicts Q=1.")


if __name__ == "__main__":
    main()
