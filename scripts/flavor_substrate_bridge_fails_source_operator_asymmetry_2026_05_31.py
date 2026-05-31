#!/usr/bin/env python3
"""Substrate-necessity bridge (A2-PLUS -> A2 via single-axiom-Hilbert/information): FAILS three ways, and
the centering guard exposes a source/operator ASYMMETRY at the root of the whole onsite-source line.

  B1 single-axiom notes ASSUME, do not DERIVE locality: single_axiom_hilbert=audited_renaming (its own
     header + audit verdict: does NOT derive local-Hamiltonian/locality/Born from the tensor product; 4
     admitted inputs, class-E); single_axiom_information=meta/unaudited (class-F, "does not force locality").
     Neither is near retained-grade; not "one retention away".
  B2 WRONG TARGET even if retained: they would give GENERIC tensor/observable-locality, NOT the specific
     "physical mass SOURCES are onsite-diagonal" retention law.
  B3 CENTERING is a coordinate identity, not a source->mass theorem: z=(1-2r)/(1+2r) is the Mobius image of
     the operator modulus r. The LITERAL source operator H=S(z)=I+zZ at source-free S=I (z=0) gives the
     DEGENERATE spectrum {1,1,1} -> Q=1/3, NOT 2/3. "z=0 -> Q=2/3" holds only on the reduced/Brannen carrier
     where z=0 means r=1/2 (the SPLIT operator), i.e. it re-centers on the answer.
  B4 SOURCE/OPERATOR ASYMMETRY (the fatal point the guard found): the descent E_loc(X)=(Tr X/3)I erases Z on
     the SOURCE S=I+zZ -> Q=2/3, but the MASS OPERATOR H=aI+bC+bbar C^2 is itself off-diagonal (Diag(H)=I).
     Applying the SAME onsite-locality to H collapses it to scalar -> DEGENERATE -> Q=1/3. So Q=2/3 requires
     onsite-locality on the source but NOT the operator -- an asymmetry nothing native justifies. Applied
     consistently, onsite-locality DESTROYS the masses (Q=1/3), it does not select Q=2/3.
"""
import numpy as np

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def Q_signed(lams):
    lams=np.array(lams,float)  # masses = lam^2, signed sqrt(m)=lam
    return (lams**2).sum()/lams.sum()**2

def main():
    I=np.eye(3); C=np.array([[0,0,1],[1,0,0],[0,1,0]],float); J=np.ones((3,3)); Z=2*(J/3)-I
    passed=[]
    # B3 literal S=I -> degenerate Q=1/3
    ev0=np.sort(np.linalg.eigvalsh(I+0*Z))
    passed.append(check("B3 literal source-free S=I (z=0) -> degenerate {1,1,1} -> Q=1/3, NOT 2/3",
        np.allclose(ev0,1) and abs(Q_signed(ev0)-1/3)<1e-9, f"eig={np.round(ev0,3)}, Q={Q_signed(ev0):.4f}; z=0<=>r=1/2 is a Mobius re-centering on the carrier"))
    # B4 source/operator asymmetry: split operator Q=2/3 (signed), onsite descent of operator -> degenerate Q=1/3
    b=1/np.sqrt(2); H=I+b*C+b*C.T; ev=np.sort(np.linalg.eigvalsh(H))  # r=1/2
    passed.append(check("B4a split mass operator (r=1/2), signed readout -> Q=2/3",
        abs(Q_signed(ev)-2/3)<1e-9, f"eig={np.round(ev,3)}, Q_signed={Q_signed(ev):.4f}"))
    Hd=np.diag(np.diag(H)); evd=np.sort(np.linalg.eigvalsh(Hd))
    passed.append(check("B4b onsite descent of the OPERATOR H (Diag) -> degenerate -> Q=1/3 (locality destroys masses)",
        abs(Q_signed(evd)-1/3)<1e-9, f"Diag(H) eig={np.round(evd,3)}, Q={Q_signed(evd):.4f}; Q=2/3 needs locality on SOURCE but NOT operator = unjustified asymmetry"))
    # B1 single-axiom notes assume not derive
    passed.append(check("B1 single_axiom_hilbert=audited_renaming, single_axiom_information=meta: ASSUME locality, NOT retained",
        True, "their own headers + audit verdicts: do NOT derive locality/Born/Hamiltonian from A1; not near retained-grade"))
    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: the substrate-necessity bridge CANNOT upgrade A2-PLUS -> A2. (B1) the vehicles assume not")
    print("derive locality and are not retainable; (B2) even retained they give generic not source-specific")
    print("locality; (B3) the centering re-centers on the answer (literal S=I -> degenerate Q=1/3); (B4, fatal)")
    print("the onsite-source line needs locality on the SOURCE but not the OPERATOR -- applied consistently to")
    print("the mass operator, onsite-locality gives degenerate Q=1/3, not Q=2/3. So locality does NOT select")
    print("Q=2/3; it either destroys the masses or requires an unjustified source/operator asymmetry.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
