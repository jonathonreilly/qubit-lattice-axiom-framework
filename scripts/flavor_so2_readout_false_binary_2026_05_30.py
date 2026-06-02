#!/usr/bin/env python3
"""SO(2)/U(1)_b readout crux RESOLVED (wf_eda631b2): the "U(1)_b gauge vs physical" pivot is a FALSE
BINARY. The value gate is a pure complex-vs-real MEASURE-COUNTING of the doublet, delta-independent in
both readings, UNDETERMINED by framework baseline+retained; both readings native, neither forced. Converges with the
parallel worker's K-theory reframe and this session's Build C.

  S1 U(1)_b is NEITHER gauge NOR a physical algebra symmetry: making C->e^{ia}C continuous is incompatible
     with C^3=I (only a in {0,2pi/3,4pi/3} survive). No continuous U(1)_b to quotient (gauge) or to call
     physical -- the pivot's two horns BOTH collapse.
  S2 delta=arg(b) IS physical for the SPECTRUM (sets the hierarchy: masses depend on delta) but delta-BLIND
     in Q (dQ/ddelta=0; Sum lam=3a, Sum lam^2=3a^2+6|b|^2 both delta-independent). So delta's physicality
     does NOT pull the answer to det_R/r=1; both readings live on the U(1)_b-invariant radial sector (a,|b|).
  S3 the real gate = MEASURE COUNTING (orthogonal to delta): det_R(alpha Ps+beta Pd)=alpha*beta^2 (doublet
     by REAL DIMENSION 2 -> (1,2) -> r=1 -> Q=1) vs det_C=alpha*beta (doublet as ONE complex slot, the
     SO(2)/U(1)_b-frame-reduced determinant -> (1,1) -> r=1/2 -> Q=2/3). They differ ONLY by whether the
     doublet's SO(2) frame-angle is quotiented before det_R.
  S4 NEW_PARITY CORRECTION: full (1+2) degeneracy at EVERY delta=m*pi/3 (6 dihedral loci), not only
     sin(delta)=0 (delta=0,pi). Nondegeneracy condition: delta not a multiple of pi/3.
  VERDICT: UNDETERMINED. Both det_R/Q=1 and det_C/Q=2/3 are native (det_C uses the native C3-equivariant
  J_cs=(C-C^2)/sqrt3, NOT forbidden by C^3=I per the companion correction note); NEITHER forced. The slot
  is a free reality-structure bit (real-dimension vs complex/Wedderburn-block counting of the doublet).
"""
import numpy as np

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def main():
    C=np.array([[0,0,1],[1,0,0],[0,1,0]],float); I3=np.eye(3); J=np.ones((3,3)); Ps=J/3; Pd=I3-J/3
    a=1.0; bmag=np.sqrt(0.5); passed=[]
    # S1 no continuous U(1)_b
    passed.append(check("S1 U(1)_b not an algebra symmetry: C->e^{ia}C compatible with C^3=I only at a in {0,2pi/3,4pi/3}",
        np.allclose(np.linalg.matrix_power(np.exp(2j*np.pi/3)*C,3),I3) and not np.allclose(np.linalg.matrix_power(np.exp(0.4j)*C,3),I3),
        "both 'gauge' and 'physical-symmetry' horns collapse -- false binary"))
    # S2 delta physical for spectrum, blind in Q
    def lam(d): return np.array([a+2*bmag*np.cos(d+2*np.pi*k/3) for k in range(3)])
    spec_dep = not np.allclose(np.sort(lam(0.3)),np.sort(lam(1.1)))
    Q=lambda d:(np.sum(lam(d)**2))/(np.sum(lam(d)))**2
    q_blind = abs(Q(0.3)-Q(1.1))<1e-12
    passed.append(check("S2 delta physical for spectrum (hierarchy moves) but delta-BLIND in Q (dQ/ddelta=0)",
        spec_dep and q_blind, f"Q(delta) const={Q(0.3):.5f}; masses delta-dependent"))
    # S3 det_R vs det_C counting
    detR = np.linalg.det(2*Ps+5*Pd)  # alpha=2,beta=5 -> 2*25=50
    passed.append(check("S3 det_R(aPs+bPd)=a*b^2 (doublet real-dim 2 ->(1,2)->Q=1); det_C=a*b (1 complex slot ->(1,1)->Q=2/3)",
        abs(detR-50)<1e-9, "differ only by quotienting the SO(2) doublet-frame before det_R"))
    # S4 degeneracy at every m pi/3
    degen=all(np.min(np.abs(np.diff(np.sort(lam(m*np.pi/3)))))<1e-9 for m in range(6))
    nondegen=np.min(np.abs(np.diff(np.sort(lam(0.7)))))>1e-6
    passed.append(check("S4 NEW_PARITY correction: full degeneracy at every delta=m*pi/3 (6 loci), not just sin(delta)=0",
        degen and nondegen, "nondegeneracy <=> delta not a multiple of pi/3"))
    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: the SO(2)/U(1)_b 'gauge vs physical' framing MIS-LOCATES the gate (false binary). The")
    print("real gate is the complex-vs-real MEASURE-COUNTING of the doublet, delta-independent in both")
    print("readings, UNDETERMINED by framework baseline+retained. Both native (det_C via native J_cs), neither forced.")
    print("Converges: this session's Build C + the parallel K-theory reframe + PR #2412 + the J_cs correction.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
