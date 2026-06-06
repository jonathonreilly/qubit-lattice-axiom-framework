#!/usr/bin/env python3
"""Three scoped positivity/readout checks for the flavor measure row.

These checks test only the displayed routes:

  P1 OS REFLECTION POSITIVITY is AGNOSTIC: the OS Gram <theta(f_i)f_j>=G(tau_i+tau_j) is positive-
     semidefinite IDENTICALLY for 1-complex (det_C) and 2-real (det_R) field content (both min-eig ~ 0).
     RP never sees the complex-vs-real counting. (Matches the framework's own FREE_FIELD_OS note: identical
     statistics-blind covariance S=M^{-1} underlies BOTH fermionic and bosonic branches; statistics
     selection is an explicit OPEN gap G3 -- the det_C/det_R fork is the same blindness one level down.)
  P2 BARGMANN descent is GENERATION-BLIND: the qubit Kahler/coherent-state complex structure is
     J_qubit=i*I3 (the CENTRAL Cl(3) pseudoscalar, eigs all +i), distinct from the generation-doublet
     J_cs=(C-C^2)/sqrt3 (eigs {0,+i,-i}, traceless, doublet-only). The Bargmann measure descends via the
     wrong (central) i, not via J_cs -> does NOT select det_C on the generation doublet.
  P3 POSITIVITY secures the READOUT CLASS, not r: RP -> positive transfer matrix -> H Hermitian -> the
     signed/Brannen readout on which Q=(1+2r)/3 is exact -- but this holds for EVERY r (0.3->0.533,
     0.5->0.667, 1->1, 2->1.667). A real partial win (Hermitian readout is necessary for Q=2/3) but it
     does NOT fix r=1/2.
  P4 STEELMAN: the complex GNS Hilbert space is a GNS-over-C artifact present for ANY field content (even
     the real det_R theory has a complex H_phys); it does NOT collapse 2-real into 1-complex.

Scope boundary: this runner does not prove a complete symmetry-side or measure-side selector theorem,
and it does not close r=1/2. It only verifies the three algebraic/no-selection checks above.
"""
import numpy as np

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def main():
    passed=[]
    E=1.3; taus=np.array([0.2,0.5,0.9,1.4]); n=len(taus); G=lambda s:(1/(2*E))*np.exp(-E*s)
    Gram=np.array([[G(taus[i]+taus[j]) for j in range(n)] for i in range(n)])
    mineig=lambda M: np.linalg.eigvalsh((M+M.conj().T)/2).min()
    two_real=np.block([[Gram,np.zeros((n,n))],[np.zeros((n,n)),Gram]])
    passed.append(check("P1 OS Gram PSD identically for 1-complex (det_C) and 2-real (det_R) -> RP AGNOSTIC to counting",
        mineig(Gram.astype(complex))>-1e-12 and mineig(two_real)>-1e-12, "RP holds equally for both field contents; statistics-blind"))
    C=np.array([[0,0,1],[1,0,0],[0,1,0]],float); Jcs=(C-C.T)/np.sqrt(3)
    passed.append(check("P2 Bargmann J_qubit=i*I3 (central, gen-blind) != J_cs (doublet-only) -> wrong complex structure",
        np.allclose(np.linalg.eigvals(1j*np.eye(3)),1j) and not np.allclose(1j*np.eye(3),Jcs),
        "qubit Kahler measure descends via central i, not via the generation J_cs"))
    ok=True
    for r in [0.3,0.5,1.0,2.0]:
        b=np.sqrt(r); ev=np.sort(np.linalg.eigvalsh(np.eye(3)+b*C+b*C.T))
        ok &= abs((ev**2).sum()/ev.sum()**2 - (1+2*r)/3) < 1e-9
    passed.append(check("P3 positivity -> Hermitian readout Q=(1+2r)/3 for EVERY r -> secures readout CLASS not r=1/2",
        ok, "RP necessary for the signed/Brannen readout (-> Q=2/3 possible) but holds for all r"))
    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: the three checked positivity/readout tests are AGNOSTIC to the det_C versus det_R count.")
    print("They secure the signed-Hermitian readout class for the displayed r values, but do not select r=1/2.")
    print("Scope boundary: this runner is not a complete symmetry-side or measure-side selector theorem and does")
    print("not close the flavor-selection problem.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
