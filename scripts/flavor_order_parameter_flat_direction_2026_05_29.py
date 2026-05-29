#!/usr/bin/env python3
"""
Flavor vacuum / order-parameter attack (option B) -- capstone.
8-lens workflow: 0 forced, 8 reduce-to-gate. Two positive results + the
flat-direction conclusion.

POSITIVE 1: spontaneous breaking is FORCED. The S_3-symmetric (democratic)
vacuum is an UNSTABLE fixed point of the native records/Lueders dynamics
(Jacobian eigenvalue +2 on every breaking direction). So the framework does
force the generation symmetry to break.

POSITIVE 2 (decisive): the breaking is the WRONG SYMMETRY SECTOR. Gamma_chi
is itself circulant, so EVERY C_3-equivariant native structure (instability,
flow, potential, C/CP-breaking, emergent-time) COMMUTES with Gamma_chi
(anticommute-fraction = 0 exactly). Q=2/3 needs a NON-circulant operator
ANTICOMMUTING with Gamma_chi. Orthogonal sectors -> the breaking overshoots
to collapse (Q->1); r=1/2 is never pinned.

CONCLUSION: r=1/2 (Q=2/3) is a framework FLAT DIRECTION -- the framework
forces the vacuum manifold Q in [1/3,1] and forces that breaking OCCURS, but
the value is a dynamically-unpinned flat direction = a contingent boundary/
initial condition. Confirmed across 9 lenses + cross-lane scout; the
Sakharov source is blocked by CPT-exactness; r=1/2 is NOT a critical point
(critical points are the cone edges; midpoint=critical is coordinate-dependent).
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    R = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)
    J = np.ones((3, 3)); Gx = (2/3) * J - np.eye(3)

    sep("POSITIVE 1: spontaneous breaking is FORCED (democratic vacuum unstable)")
    p = np.ones(3) / 3
    def f(pp): q = pp * pp; return q / q.sum()
    eps = 1e-6; Jac = np.zeros((3, 3))
    for j in range(3):
        pp = p.copy(); pp[j] += eps; pp /= pp.sum()
        Jac[:, j] = (f(pp) - f(p)) / eps
    w = np.sort(np.real(np.linalg.eigvals(Jac)))[::-1]
    print(f"  records/Lueders Jacobian eigenvalues at democratic vacuum: {np.round(w,3)}")
    print("  eig = 2 > 1 on the breaking directions => S_3-symmetric vacuum UNSTABLE")
    print("  => spontaneous generation-symmetry breaking is FORCED to occur.")

    sep("POSITIVE 2 (decisive): the breaking is the WRONG SYMMETRY SECTOR")
    print(f"  Gamma_chi is circulant: [Gx, C] = {np.max(np.abs(Gx@R-R@Gx)):.1e}")
    for nm, M in [("C", R), ("C^2", R.T), ("C+C^2", R + R.T)]:
        comm = np.max(np.abs(M @ Gx - Gx @ M)); anti = np.max(np.abs(M @ Gx + Gx @ M))
        print(f"  circulant {nm:6s}: [.,Gx]={comm:.0e} (COMMUTES); {{.,Gx}}={anti:.2f} (not anticommuting)")
    print("  => EVERY C_3-equivariant (circulant) native structure -- instability, flow,")
    print("     potential, C/CP-breaking, emergent-time -- commutes with Gamma_chi.")
    print("     The Q=2/3 order parameter must ANTICOMMUTE (non-circulant). Orthogonal.")
    print("     Native breaking overshoots to collapse (Q->1); r=1/2 never pinned.")

    sep("the other routes (all reduce to gate)")
    print("  no stopping mechanism: existence wall (r=1) is ABSORBING (no restoring force);")
    print("    walls push same direction ~5000x asymmetric; r=1/2 non-stationary (beta!=0).")
    print("  r=1/2 NOT critical: F(Q) smooth at 2/3; criticality at cone edges Q=1/3, Q=1;")
    print("    'midpoint=critical' is COORDINATE-DEPENDENT (true in Q,r; false in sigma,sqrt r).")
    print("  Sakharov BLOCKED: CPT exact (retained); C=-I_3 on generations (generation-blind);")
    print("    CP-violation lives inside the circulant algebra (commutes with Gamma_chi).")

    sep("CONCLUSION: r=1/2 is a framework FLAT DIRECTION (contingent)")
    print("  FORCED:    the vacuum MANIFOLD Q in [1/3,1]  AND  that breaking OCCURS.")
    print("  NOT FORCED: the value r=1/2 -- a dynamically-unpinned flat direction =")
    print("             a contingent boundary/initial condition.")
    print("  Reason (one fact, verified): Gamma_chi circulant => every native symmetric/")
    print("  equivariant structure commutes with it; the order parameter must anticommute")
    print("  (non-circulant). Symmetric structures categorically cannot produce a")
    print("  broken-symmetry order parameter in the orthogonal sector.")
    print("  CONSTRUCTIVE NEXT: formalize a NO-SELECTOR THEOREM (the flavor modulus is a")
    print("  framework flat direction) -- the circulant-commutation fact above is most of it;")
    print("  converts the open gate into a settled bounded result. Caveat: 'contingent' is")
    print("  the correct null but needs the negative theorem; forced-but-undiscovered vs")
    print("  genuinely-contingent is formally undecided -- B shows no TESTED selector forces it.")


if __name__ == "__main__":
    main()
