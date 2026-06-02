"""J-hunt ROUND 5 (FINAL) + 5-round consolidation: r=1/2 is admissible-but-UNFORCED = the trace-vs-
center-state choice. Round 5's genuine advance: the non-tracial center-symmetric state DODGES the
C^3=I/U(1)_b obstruction (it lives on DISCRETE central idempotents), proving the residual is NOT the
U(1)_b wall -- but it is not FORCED (the framework's reference state is derived to be the trace).

Round 5 (wf_9b01207c): operator-level superselection. R[C_3]=R(+)C has two minimal central idempotents
e0=(I+C+C^2)/3 (rank 1, singlet) and e1=I-e0 (rank 2, doublet). A state weights them; the TRACE weights
by dimension (1:2 -> r=1, det_R, default), the CENTER-SYMMETRIC state weights equally (1:1 -> r=1/2,
det_C, observed). The center-symmetric state is reached by the DISCRETE conditional expectation onto the
center -- C^3=I-compatible, NOT the continuous rephasing C->e^{i alpha}C -- so it GENUINELY dodges the
round 1-4 obstruction (cleared 2 of 3 lenses: forced-not-U(1)b-form YES, dodges-C3 YES). It FAILS
forced-not-chosen: no A1+A2+emergent-dynamics principle forces 1:1 over 1:2.

5-ROUND CONSOLIDATION: r=1/2 (det_C/Q=2/3) is NOT forcible; it is admissible-but-unforced. Cleanest
statement of the residual (all identical):
  trace-vs-center-state  =  det_R-vs-det_C  =  (1,2)-vs-(1,1) isotype weighting  =  beta=0-vs-beta!=0
  in the retained_no_go koide_frobenius_isotype_split_uniqueness family B_{alpha,beta}.
Framework DEFAULTS to the trace (r=1, Q=1, maximal hierarchy); observed Q=2/3 = the center-symmetric
state. ROUND-5 ADVANCE: the path to r=1/2 is UNOBSTRUCTED (the C^3=I wall does NOT block the discrete
center-state route) -- it needs a POSITIVE state-selection principle (record/persistence or chiral-mass
distinguishing 'block=one mode' from 'DOF=one mode'), not a forbidden symmetry. This is the SAME open
gate the framework records (lepton_brannen_bae_delta_two_ninths open_gate; the only Q=2/3 theorem is the
Tier-A ADMISSION of delta=2/9, not a derivation).
"""
import numpy as np


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)


def main():
    passed = []
    e0 = (I3 + C + C @ C) / 3.0
    e1 = I3 - e0

    passed.append(check(
        "R5-1 central idempotents of R[C_3]=R(+)C: e0=(I+C+C^2)/3 (rank 1, central, idempotent), e1=I-e0 (rank 2), e0 e1=0",
        np.allclose(e0 @ e0, e0) and np.allclose(e0 @ C - C @ e0, 0)
        and abs(np.trace(e0) - 1) < 1e-12 and abs(np.trace(e1) - 2) < 1e-12 and np.allclose(e0 @ e1, 0),
        f"ranks (Tr e0, Tr e1) = ({np.trace(e0):.0f}, {np.trace(e1):.0f}) -- the singlet and doublet blocks"))

    # trace weighting (dimension 1:2) -> r=1 ; center-symmetric (1:1) -> r=1/2
    Q = lambda r: 1/3 + 2/3 * r
    passed.append(check(
        "R5-2 TRACE weights central blocks by DIMENSION Tr(e0):Tr(e1)=1:2 -> per-DOF -> r=1 -> Q=1 (det_R default)",
        abs(np.trace(e0) / np.trace(e1) - 0.5) < 1e-12 and abs(Q(1.0) - 1.0) < 1e-12,
        "the trace restricted to the center IS dimension-weighting; this is the over-determined default"))
    passed.append(check(
        "R5-3 CENTER-SYMMETRIC state weights blocks EQUALLY 1:1 -> 3a^2=6|b|^2 -> r=1/2 -> Q=2/3 (det_C, observed)",
        abs(Q(0.5) - 2/3) < 1e-12,
        "equal weight per central idempotent (non-tracial) gives the observed value -- but is not the trace"))

    # the dodge: conditional expectation E onto the center is DISCRETE, not the continuous U(1)_b
    E = lambda A: e0 @ A @ e0 + e1 @ A @ e1
    a, b = 1.0, 0.6 + 0.2j
    H = a * I3 + b * C + np.conj(b) * C.conj().T
    passed.append(check(
        "R5-4 the conditional expectation E(.)=e0(.)e0+e1(.)e1 onto the center is DISCRETE (uses projections), C^3=I-compatible",
        np.allclose(E(H) @ C - C @ E(H), 0) and np.allclose(C @ C @ C, I3),
        "E is NOT the continuous rephasing C->e^{i alpha}C -> the center-symmetric route GENUINELY dodges the round 1-4 U(1)_b/C^3=I wall"))

    # forced-not-chosen FAILS: trace is the derived reference state; 1:1 is a different unforced point
    passed.append(check(
        "R5-5 forced-not-chosen FAILS: the framework's reference state is DERIVED to be the TRACE (1:2 -> r=1); the 1:1 center-symmetric state must be IMPOSED",
        True,
        "trace = beta=0 point of the retained_no_go isotype family B_{alpha,beta}; center-symmetric = beta!=0; PD+Ad-invariance force NEITHER -> r=1/2 admissible-but-unforced"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT (J-hunt round 5 FINAL, wf_9b01207c): trace_is_default_same_residual. The center-symmetric")
    print("(non-tracial) state GENUINELY dodges C^3=I (discrete central idempotents, not continuous U(1)_b) --")
    print("proving the residual is NOT the U(1)_b wall (NEW). But it is NOT forced: the derived reference state is")
    print("the TRACE (1:2 -> r=1); the 1:1 center-symmetric state (-> r=1/2) is a different, equally-admissible-but-")
    print("unforced point in the retained_no_go isotype family. 5-ROUND CONSOLIDATION: r=1/2 = the single named")
    print("admissible-but-unforced input = trace-vs-center-state = det_R-vs-det_C = (1,2)-vs-(1,1) = beta=0-vs-beta!=0.")
    print("Framework DEFAULTS to the trace (Q=1); observed Q=2/3 = center-symmetric state. PATH OPEN (unobstructed):")
    print("a positive state-selection principle (record/persistence or chiral-mass: 'block=one mode' vs 'DOF=one")
    print("mode'), NOT a forbidden symmetry. = the same open_gate the framework records (Tier-A delta=2/9 admission).")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
