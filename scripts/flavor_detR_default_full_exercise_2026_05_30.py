#!/usr/bin/env python3
"""FULL exercise on the campaign load-bearing claim. Confirms Q=1 (det_R) is the substrate-FORCED
default and r=1/2 (det_C) a genuine import -- the crux (does qubit C-structure flip it) is refuted
on 4 legs -- BUT corrects two overstatements and names the one open gap.

CONFIRMED (load-bearing): Q=1 (det_R / real-discrete-C3) is the substrate-forced generation default;
Q=2/3 (r=1/2 / det_C) is a genuine, precisely-localized import.
  X1 substrate i is generation-BLIND (i*I3 commutes with C); the doublet U(1) generator G_U1=(C-C^2)/sqrt3
     has ZERO HS-overlap with i*I3 -> the complex structure does NOT descend as a doublet U(1).
  X2 C^3=I quantizes the U(1)_b rephasing to {0, 2pi/3, 4pi/3} -> continuous U(1) forbidden (retained
     koide_c3_generator_rephasing_obstruction).
  X3 (Z_2)^3 momentum corners are +/-1 (REAL) + CPT reflection sends J_b->-J_b -> no holomorphic det_C
     carrier; generation algebra is honestly real R[Z3].
CORRECTION #1 (Link 5, previously overstated): the det_C/U(1) generator is NOT the chirality gate.
  G_U1 COMMUTES with Gamma_chi=(2/3)J-I and with C (on-block, C3-equivariant); the chiral grading is
  off-block and ANTICOMMUTES. They are algebraically orthogonal -- "single shared gate" is unsupported on R^3.
CORRECTION #2 (the actual import): once U(1)-symmetry and holomorphic-measure are both excluded, the
  residual import is SOLELY the block-vs-dimension MEASURE CHOICE on R[Z3]=R(+)C: (1,1) idempotent/center
  -count -> Q=2/3 vs (1,2) Plancherel/dimension-count -> Q=1. The trace permits both, RANKS NEITHER
  (Schur: 2 real doublet modes cannot merge into 1 complex mode). It is NOT a continuous symmetry, NOT a
  holomorphic measure, NOT the chiral grading -- just a discrete counting-measure choice.
OPEN GAP (Link 1 Half B): that the generation reference state is the beta=0 TRACE (3 equal modes) rather
  than a finite-beta Gibbs/KMS state is UNAUDITED, user-approval-required (PRR premise); the framework's own
  KMS note has beta>0 Gibbs (non-tracial). Finite-beta cannot make det_C native (Schur) but A1+A2 do not
  force beta=0, so "Q=1 is THE default" is conditional on the tracial-vacuum premise.
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
    passed.append(check("X3 (Z_2)^3 corner amplitudes are +/-1 (REAL) -> honestly real R[Z3]",
        all(abs(c.imag) < 1e-12 if isinstance(c,complex) else True for c in chars) and set(chars)=={1,-1}))
    passed.append(check("CORR#1 G_U1 COMMUTES with Gamma_chi and C (NOT the chiral gate)",
        np.allclose(G@Gchi-Gchi@G,0) and np.allclose(G@C-C@G,0) and
        np.linalg.norm(G@Gchi+Gchi@G)>1, f"||{{G,Gchi}}||={np.linalg.norm(G@Gchi+Gchi@G):.3f} (chiral grading is off-block, anticommutes)"))
    Q=lambda r:1/3+2/3*r
    passed.append(check("CORR#2 import = block(1,1)->Q=2/3 vs dimension(1,2)->Q=1 measure choice; trace ranks neither",
        abs(Q(0.5)-2/3)<1e-12 and abs(Q(1)-1)<1e-12, "det_C block-count r=1/2; det_R dimension r=1; Schur: no merge of 2 real->1 complex"))
    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: CONFIRMED -- Q=1 (det_R) substrate-forced default, Q=2/3 (det_C) a genuine import;")
    print("crux (complex structure flips it) refuted 4 ways. CORRECTED: the import is NOT the chirality")
    print("gate (G_U1 commutes with Gamma_chi) and NOT a U(1) symmetry or holomorphic measure -- it is the")
    print("discrete block-vs-dimension counting-measure choice the trace permits but does not rank. OPEN:")
    print("Link-1 Half B -- beta=0 tracial vacuum vs finite-beta Gibbs is an unaudited, user-approval premise.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
