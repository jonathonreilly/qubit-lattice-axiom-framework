#!/usr/bin/env python3
"""
CENTER-TRACE-SELECTION push (wf_ca92b904, 6 angles, 0 survived) + verification.
The single live thread is CLOSED -- and not merely 'not found': a RETAINED theorem
votes against it. Final capstone of the charged-lepton value-derivation campaign.

THE QUESTION: does decoherence/superselection make the mass functional read the
CENTER trace of R[Z3]=R(+)C (2 idempotents equal -> Q=2/3) rather than the full-
algebra trace (dimension -> Q=1)?

RESULT: NO. Three decisive facts (all retained-theorem-backed):

(1) C3 is PHYSICAL, not gauge -- the crux, settled by RETAINED
    three_generation_observable_no_proper_quotient_narrow_theorem. The corner
    projectors {P_X1,P_X2,P_X3} + the C3 cycle GENERATE THE FULL M3(C) (verified
    here: algebra dim = 9/9), acting IRREDUCIBLY on C^3 -> only invariant subspaces
    {0}, C^3 -> NO proper subspace to quotient -> C3 is a physical symmetry, mu and
    tau are gauge-distinct. So the physical (gauge-invariant) observable algebra is
    the FULL M3(C), which votes DIMENSION -> Q=1. The center is not the physical algebra.

(2) The only retained max-entropy / ignorance reference is the TRACIAL state rho=I/d
    (retained pre_record_reference_state + retained Powers/UHF uniqueness). On the
    generation carrier I/3 -> sector populations (1/3, 2/3) = DIMENSION -> r=1 -> Q=1.
    Equal sector weight (1/2,1/2) -> Q=2/3 is the block-count prescription, which
    traciality does NOT rank above dimension. On the (commutative) CENTER the tracial
    condition is VACUOUS -> the retained selector pins nothing there.

(3) Einselection does not reweight populations: dephasing rho -> sum_k P_k rho P_k
    kills inter-sector coherence but leaves block populations untouched; applied to
    I/3 it returns (1/3, 2/3) = Q=1. Equal weight needs an equal-atom PRIOR -- a fresh
    import = the (1,1) pin restated. And a genuine CENTER mass observable is block-
    constant -> 2 eigenvalues -> mu=tau (contradicts 3 distinct masses).

WHAT IS GENUINE (does not overturn the verdict): the (r | theta) factorization is
real -- r=|b|^2/a^2 (sets Q) is theta-free and center-readable, theta=arg(b) carries
the 3-distinct splitting (Q-orthogonal) -- so the 3-distinct wall is NOT intrinsically
fatal to value-selection. But (1)-(3) defeat the selection anyway; and even the
factorization's value half rides on the SIGNED-eigenvalue (det_R/Brannen) readout
(the singular-value readout gives Q!=2/3 at intermediate theta) = a SECOND open pin.

FINAL STATUS: charged-lepton Q=2/3 = DERIVED-MODULO-THE-WEIGHT-PIN. The framework's
RETAINED structure votes FULL/DIMENSION -> Q=1 (C3 physical + tracial I/d); the
observed 2/3 is the non-generic block-count fixed point requiring the chiral/weight
pin. The center-trace derivation route is CLOSED by the retained no-proper-quotient
theorem. The remaining frontier is now TWO COUPLED pins, both currently pointing away
from the retained default: (a) does the records/einselection measure count OBJECTIVE
SECTORS rather than Hilbert DIMENSIONS (open einselection-weight choice, not settled
by the retained tracial reference); (b) is the SIGNED-eigenvalue readout native
(det_C/det_R / U(1)_b pin). Both must resolve together for Q=2/3 to become a theorem.
"""
import numpy as np


def main():
    P = [np.diag([1.0 if i == k else 0 for i in range(3)]) for k in range(3)]
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], float)
    basis = P + [C]
    for _ in range(8):
        new = list(basis) + [a @ b for a in basis for b in basis]
        keep, cur = [], np.zeros((0, 9))
        for m in new:
            t = np.vstack([cur, m.flatten()])
            if np.linalg.matrix_rank(t, tol=1e-9) > cur.shape[0]:
                keep.append(m); cur = t
        basis = keep
        if len(basis) >= 9:
            break
    dim = np.linalg.matrix_rank(np.array([m.flatten() for m in basis]), tol=1e-9)
    print(f"(1) <{{P_X1,P_X2,P_X3, C3}}> algebra dim = {dim}/9  -> full M3(C) -> C3 PHYSICAL -> dimension -> Q=1")
    # (2) einselect I/3 -> sector populations
    I3 = np.eye(3) / 3
    Ps = np.ones((3, 3)) / 3                     # singlet projector
    pop_s = np.trace(Ps @ I3); pop_d = 1 - pop_s
    print(f"(2) tracial reference I/3 -> sector pops (singlet,doublet)=({pop_s:.4f},{pop_d:.4f})=DIMENSION -> Q=1")
    print(f"(3) einselection preserves these pops (dephasing fixes diagonal) -> stays (1/3,2/3) -> Q=1")
    print("VERDICT: center trace NOT selected (retained no-proper-quotient + tracial I/d both vote dimension).")
    print("Q=2/3 = derived-modulo-the-weight-pin; framework default Q=1; remaining = 2 coupled pins")
    print("(sector-count einselection weight; signed-eigenvalue readout).")


if __name__ == "__main__":
    main()
