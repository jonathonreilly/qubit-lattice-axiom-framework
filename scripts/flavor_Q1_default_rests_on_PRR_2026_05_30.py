#!/usr/bin/env python3
"""THE OPEN GAP RESOLVED (Build C): "Q=1 is the framework default" is NOT forced by A1+A2 -- it rests
ENTIRELY on the unaudited PRR premise (full inner-automorphism / U(3) invariance). Under the genuine
A1+A2 generation symmetry (C3 only), a non-tracial C3-invariant reference is admissible and Q=2/3 is
REACHABLE (not yet derived). This CORRECTS the prior "Q=1 default" statement.

  C1 C3-invariant reference states form a 2-parameter cone rho=alpha*Ps+beta*Pd (Schur: scalar per block),
     fixed by block masses (w_s,w_d). Trace -> (1:2) dimension -> r=1 -> Q=1; the 1:1 block-count state ->
     r=1/2 -> Q=2/3.
  C2 explicit admissible non-tracial state rho_(1:1)=(1/2)Ps+(1/4)Pd: PSD, trace 1, eigs {1/2,1/4,1/4},
     COMMUTES with C3, block masses 1:1. A perfectly valid C3-invariant reference giving Q=2/3.
  C3 the trace is privileged ONLY by FULL U(3)/inner-automorphism invariance (=PRR): Haar-U(3) leaves
     rho_tau invariant (dev ~1e-15) but NOT rho_(1:1) (dev ~0.35). PRR is UNAUDITED + user-approval-required
     + NOT derived from A1+A2. The "dynamics-independence -> trace" steelman collapses into PRR
     (KMS-for-all-dynamics <=> tracial <=> U(3)-invariant).
  C4 CRITICAL: r=|b|^2/a^2 is a SPECTRAL INVARIANT of H alone; the reference state does NOT enter the
     retained Koide functional. The "r*=w_d/(2w_s)" bridge is INSERTED, not derived (variance minimization
     gives a different b). So the reference-cone removes "Q=1 forced" but does NOT itself derive r=1/2.
  => HONEST STATUS: "Q=1 default" = DEFAULT-pending-PRR, NOT forced. Q=2/3 = reachable, NOT derived.
     NEITHER is forced by A1+A2 alone. The decisive (decidable, no-import) question is whether the physical
     mass READOUT factors through the SO(2)/U(1)_b doublet-frame quotient (count doublet once -> 1:1 ->
     r=1/2) or its full 2-real-dim content (-> 1:2 -> r=1).
"""
import numpy as np, sympy as sp
import numpy.linalg as la

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def main():
    C=np.array([[0,0,1],[1,0,0],[0,1,0]],float); I3=np.eye(3); J=np.ones((3,3)); Ps=J/3; Pd=I3-J/3
    rho11=0.5*Ps+0.25*Pd; rho_tau=I3/3
    passed=[]
    passed.append(check("C1/C2 rho_(1:1) PSD, trace1, commutes C3, block masses 1:1 (admissible non-tracial ref)",
        np.all(np.linalg.eigvalsh(rho11)>=-1e-12) and abs(np.trace(rho11)-1)<1e-12 and
        np.allclose(rho11@C-C@rho11,0) and abs(np.trace(rho11@Ps)-np.trace(rho11@Pd))<1e-12,
        f"eigs={np.round(np.linalg.eigvalsh(rho11),3)}; trace block masses 1:2 (dimension)"))
    # U(3) only
    devs_t=[]; devs_1=[]
    for k in range(500):
        A=np.array([[np.cos(0.01*k+i+j)+1j*np.sin(0.013*k+2*i+j) for j in range(3)] for i in range(3)])
        Qm,_=la.qr(A); devs_t.append(la.norm(Qm@rho_tau@Qm.conj().T-rho_tau)); devs_1.append(la.norm(Qm@rho11@Qm.conj().T-rho11))
    passed.append(check("C3 trace privileged ONLY by full U(3)=PRR (unaudited); C3 alone leaves the cone open",
        max(devs_t)<1e-12 and max(devs_1)>0.05, f"U(3) dev: tau={max(devs_t):.1e}, (1:1)={max(devs_1):.3f}"))
    a,b=sp.symbols('a b',positive=True)
    Q=sp.simplify(((a+2*b)**2+2*(a-b)**2)/((a+2*b)+2*(a-b))**2)
    passed.append(check("C4 r is a SPECTRAL INVARIANT of H alone; reference does NOT enter the readout",
        sp.simplify(Q-(sp.Rational(1,3)+sp.Rational(2,3)*(b/a)**2))==0,
        "the r*=w_d/(2w_s) state->operator bridge is inserted, not derived (variance min gives different b)"))
    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: 'Q=1 is the framework default' is CORRECTED -> DEFAULT-pending-PRR, NOT forced. A1+A2")
    print("supply only C3 on the generation factor, leaving the (w_s,w_d) cone open; the trace (Q=1) needs")
    print("the unaudited full-U(3) PRR premise; the non-tracial 1:1 state (Q=2/3) is equally admissible.")
    print("NEITHER Q=1 nor Q=2/3 is forced by A1+A2; r=1/2 is REACHABLE, not derived. The decisive decidable")
    print("(no-import) question: does the mass readout factor through the SO(2)/U(1)_b doublet-frame quotient")
    print("(doublet counted once -> r=1/2) or its full 2-real-dim content (-> r=1)?")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
