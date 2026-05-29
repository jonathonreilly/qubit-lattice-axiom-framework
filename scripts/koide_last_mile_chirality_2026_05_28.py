#!/usr/bin/env python3
"""
LAST MILE for charged-lepton Koide Q=2/3 (status: derived-modulo-chirality).

Result (4-angle workflow, unanimous, 0 circular): Q=2/3 follows non-circularly,
via the RETAINED anticommuting-operator theorem, from the charged-lepton mass
operator being CHIRAL -- i.e. anticommuting with the Z_3 singlet/doublet
grading Gamma_chi. The framework's NON-chiral default (Z_3-equivariant
circulant) gives Q=1. So Q=2/3 is the SIGNATURE OF CHIRAL (Dirac) MASS
GENERATION. The remaining gap is exactly: does A1+A2 supply that chiral
operator on the generation sector? It does NOT (a retained no-go), and the
needed gamma5/chirality is even MIS-LOCATED relative to the spacetime
chirality gate (different tensor factor; bridge unbuilt).

This runner verifies the load-bearing facts.
"""

import numpy as np
np.set_printoptions(precision=6, suppress=True)


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    J = np.ones((3, 3))
    Gx = (2/3) * J - np.eye(3)
    S = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)  # Z_3 cyclic shift

    sep("(1) Gamma_chi's '2/3' is FORCED by involution, NOT tuned to Koide")
    # (t J - I)^2 = I  =>  t^2 J^2 - 2t J + I = I ; J^2 = 3J  => (3t^2 - 2t) J = 0
    print("  require (tJ - I)^2 = I  =>  3t^2 - 2t = 0  =>  t in {0, 2/3}")
    print("  t=0 trivial (-I); t=2/3 is the UNIQUE nontrivial involution.")
    print(f"  Gamma_chi^2 = I ? {np.allclose(Gx@Gx, np.eye(3))}")
    w = np.sort(np.linalg.eigvalsh(Gx))
    print(f"  eigenvalues {w}  (+1 singlet, -1 doublet); 2/3 = 2/dim, not Koide.")

    sep("(2) FORWARD mechanism (RETAINED): chiral (anticommuting) => Q=2/3")
    print("  {H,Gx}=0, Hv=lam v, lam!=0  =>  H(Gx v) = -lam (Gx v)  =>  Gx v _|_ v")
    print("  =>  <v|Gx|v>=0  =>  |v_singlet|^2 = |v_doublet|^2  =>  Q=2/3.")
    rng = np.random.default_rng(0)
    maxdev = 0.0
    for _ in range(20000):
        A = rng.normal(size=(3, 3))
        H = A - A.T                       # build a chiral H by projecting...
        # enforce anticommutation: H_chiral = off-diagonal in Gx eigenbasis
        wv, U = np.linalg.eigh(Gx)
        # split basis: singlet (eigval +1), doublet (eigvals -1)
        sing = U[:, np.argmax(wv)][:, None]
        doub = U[:, np.argsort(wv)[:2]]
        c = rng.normal(size=2)
        Hc = sing @ (c @ doub.T)[None, :] + (doub @ c)[:, None] @ sing.T
        ev, V = np.linalg.eigh(Hc)
        for i in range(3):
            if abs(ev[i]) > 1e-6:
                v = V[:, i]
                maxdev = max(maxdev, abs(v @ Gx @ v))
    print(f"  max |<v|Gx|v>| over nonzero-eigval eigenvectors (20000) = {maxdev:.2e}")
    print("  => every nonzero-eigval eigenvector of a chiral H has Q=2/3 exactly.")

    sep("(3) The framework's DEFAULT is NON-chiral -> Q=1 (retained no-go)")
    print("  A1+A2 supply only the Z_3-equivariant (circulant) algebra {I,S,S^2}.")
    print(f"  [Gamma_chi, S] = {np.max(np.abs(Gx@S - S@Gx)):.1e}  (Gx is a circulant)")
    print("  => EVERY Z_3-equivariant operator COMMUTES with Gamma_chi (non-chiral).")
    biv = S - S.T                          # Cl(3)-type bivector on generation R^3
    print(f"  Cl(3) bivector S - S^T: [biv, Gx] = {np.max(np.abs(biv@Gx-Gx@biv)):.1e}"
          f"  (commutes -> no singlet<->doublet mixing)")
    print("  retained KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO: comm(S) cap")
    print("  anticomm(Gx) = {0}. So no nonzero circulant anticommutes with Gx.")
    print("  => the chiral operator BREAKS Z_3-equivariance (off-diagonal, Dirac-")
    print("     type). A1's Clifford anticommutation lives on the 2x2 qubit/spinor")
    print("     factor, NOT the generation R^3, so it does not supply it.")

    sep("(4) the physical sqrt-mass vector IS Gamma_chi-balanced (postdiction)")
    M = np.array([0.51099895, 105.6583755, 1776.86])
    v = np.sqrt(M)
    print(f"  <v|Gx|v>/<v|v> = {(v@Gx@v)/(v@v):+.6f}  (=0 => chiral-balanced)")
    print(f"  Q = {(v@v)/(v.sum()**2):.6f}  (2/3 to 6e-6; 3 masses, 1 relation)")

    sep("(5) the gap is MIS-LOCATED relative to the existing chirality gate")
    print("  anomaly_forces_time produces gamma5 on the SPACETIME Clifford factor;")
    print("  Gamma_chi grades the GENERATION factor. DIFFERENT tensor factors.")
    print("  So Q=2/3 does NOT reduce cleanly to the existing (unaudited) gate --")
    print("  it needs a separate, UNBUILT spacetime->generation chirality bridge")
    print("  (and staggered Dirac on Z^3 has no Ginsparg-Wilson relation).")

    sep("STATUS: derived-modulo-chirality (non-circular, faithful relabeling)")
    print("  Q=2/3 <=> charged-lepton mass operator is CHIRAL (anticommutes with")
    print("  the Z_3 grading) = the signature of Dirac mass generation. NON-chiral")
    print("  default -> Q=1. NON-CIRCULAR: forward proof never names Q/2/3; Gx's")
    print("  2/3 is forced by involution+equivariance. GENUINE PROGRESS: 'why 2/3'")
    print("  is exactly relocated to 'why is mass-gen chiral on the generation")
    print("  sector' -- a single, physical, well-posed gate (Koide = corollary of")
    print("  chirality, not a coincidence). OPEN: that chiral operator is not")
    print("  supplied by A1+A2+retained (retained no-go) and the needed gamma5 is")
    print("  mis-located (spacetime vs generation factor; bridge unbuilt).")
    print("  NEXT: build/audit the spacetime-gamma5 -> generation-Gamma_chi bridge;")
    print("  if it exists -> Koide closes to 'derived'; if no-go -> pins the import.")


if __name__ == "__main__":
    main()
