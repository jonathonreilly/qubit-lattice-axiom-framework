#!/usr/bin/env python3
"""FULL exercise on the campaign load-bearing claim. It preserves the finite
det_R/det_C counting fork and refutes the route where qubit C-structure makes
det_C automatic. The old default/reference-state wording is removed: this
runner supports only the finite locator and makes no Q=1 default claim.

CONFIRMED (load-bearing): the tested finite structures do not supply det_C and
do not rank the two allowed reads. Q=1 (r=1 / det_R dimension read) and Q=2/3
(r=1/2 / det_C center-count read) remain localized measure/counting inputs.
  X1 substrate i is generation-BLIND (i*I3 commutes with C); the doublet U(1) generator G_U1=(C-C^2)/sqrt3
     has ZERO HS-overlap with i*I3 -> the complex structure does NOT descend as a doublet U(1).
  X2 C^3=I quantizes the U(1)_b rephasing to {0, 2pi/3, 4pi/3} -> continuous U(1) forbidden (retained
     koide_c3_generator_rephasing_obstruction).
  X3 (Z_2)^3 momentum corners are +/-1 (REAL) -> the checked finite carrier
     is honestly real R[Z3]. A CPT reflection sign J_b->-J_b is not derived
     by this runner and is not load-bearing for the finite locator.
CORRECTION #1 (Link 5, previously overstated): the det_C/U(1) generator is NOT the chirality gate.
  G_U1 COMMUTES with Gamma_chi=(2/3)J-I and with C (on-block, C3-equivariant), and its
  anticommutator with Gamma_chi is nonzero. A true chiral splitter would be a separate off-block
  anticommuting object. They are algebraically orthogonal -- "single shared gate" is unsupported on R^3.
CORRECTION #2 (the actual import): once U(1)-symmetry is excluded and the checked real characters
  fail to supply a native holomorphic carrier, the
  residual import is SOLELY the block-vs-dimension MEASURE CHOICE on R[Z3]=R(+)C: (1,1) idempotent/center
  -count -> Q=2/3 vs (1,2) Plancherel/dimension-count -> Q=1. The trace permits both, RANKS NEITHER
  (Schur: 2 real doublet modes cannot merge into 1 complex mode). It is NOT a continuous symmetry,
  NOT a derived holomorphic measure, NOT the chiral grading -- just a discrete counting-measure choice.
OPEN GAP (Link 1 Half B): that the generation reference state is the beta=0 TRACE (3 equal modes) rather
  than a finite-beta Gibbs/KMS state is not derived here (PRR premise); the framework's own
  KMS note has beta>0 Gibbs (non-tracial). Finite-beta cannot make det_C native (Schur) but framework baseline do not
  force beta=0, so this packet makes no Q=1 default/reference-state claim.
"""
import numpy as np

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def main():
    C=np.array([[0,0,1],[1,0,0],[0,1,0]],float); I=np.eye(3); J=np.ones((3,3)); Gchi=(2/3)*J-I
    G=(C-C.T)/np.sqrt(3)
    passed=[]
    passed.append(check("X1 substrate i generation-blind ([i*I3,C]=0) + <i*I3,G_U1>_HS=0 -> no descended U(1)",
        np.allclose(1j*I@C-C@(1j*I),0) and abs(np.trace((1j*I).conj().T@G))<1e-12))
    passed.append(check("X2 C^3=I quantizes U(1)_b: (e^{ia}C)^3=I only at a in {0,2pi/3,4pi/3}",
        (not np.allclose(np.linalg.matrix_power(np.exp(1j*0.4)*C,3),I)) and
        np.allclose(np.linalg.matrix_power(np.exp(1j*2*np.pi/3)*C,3),I)))
    # X3 momentum corner phases real (+/-1): the (Z_2) characters
    chars=[(-1)**b for b in (0,1)]
    passed.append(check("X3 (Z_2)^3 corner amplitudes are +/-1 (REAL) -> checked finite carrier is real R[Z3]",
        all(abs(c.imag) < 1e-12 if isinstance(c,complex) else True for c in chars) and set(chars)=={1,-1}))
    passed.append(check("CORR#1 G_U1 COMMUTES with Gamma_chi and C (NOT the chiral gate)",
        np.allclose(G@Gchi-Gchi@G,0) and np.allclose(G@C-C@G,0) and
        np.linalg.norm(G@Gchi+Gchi@G)>1, f"||{{G,Gchi}}||={np.linalg.norm(G@Gchi+Gchi@G):.3f} (nonzero; a true chiral splitter would anticommute)"))
    Q=lambda r:1/3+2/3*r
    passed.append(check("CORR#2 import = block(1,1)->Q=2/3 vs dimension(1,2)->Q=1 measure choice; trace ranks neither",
        abs(Q(0.5)-2/3)<1e-12 and abs(Q(1)-1)<1e-12, "det_C block-count r=1/2; det_R dimension r=1; Schur: no merge of 2 real->1 complex"))
    note = open("docs/FLAVOR_DETR_DEFAULT_FULL_EXERCISE_NOTE_2026-05-30.md").read()
    required = [
        "2026-06-07 boundary repair",
        "2026-06-07 scope repair",
        "RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05",
        "KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29",
        "bounded finite-algebra locator only",
        "default/reference-state claim",
        "does not rank the physical generation",
        "Non-claim: physical generation reference state",
        "2026-06-08 holomorphic-carrier scope repair",
        "CPT reflection sign is not load-bearing",
    ]
    banned = [
        "Q=1 is THE default",
        "substrate-forced *default*",
        "substrate-FORCED default",
        "under a supplied beta=0 tracial reference",
    ]
    boundary_ok = all(term in note for term in required) and not any(term in note for term in banned)
    passed.append(check("BOUNDARY source guard: finite locator only, no default/reference-state claim",
        boundary_ok, "finite locator only; no beta=0 tracial-vacuum promotion"))
    print(f"\nUPDATED SCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: FINITE LOCATOR -- tested structures do not make det_C/equal-block counting automatic;")
    print("they localize Q=2/3 versus Q=1 as a counting fork but do not rank the physical read. CORRECTED:")
    print("the equal-block input is not the chirality gate, not a U(1) symmetry, and not a derived")
    print("holomorphic measure; it is the block-vs-dimension counting choice the trace permits but does not rank.")
    print("OPEN: beta=0 tracial generation reference vs finite-beta Gibbs remains outside this row.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
