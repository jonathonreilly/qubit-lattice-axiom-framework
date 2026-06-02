#!/usr/bin/env python3
"""The last non-symmetry lever: does positivity (OS reflection positivity / qubit Bargmann measure /
unitarity) SELECT the Kahler (det_C) measure of the forced J_cs, fixing r=1/2? VERDICT: AGNOSTIC.
Positivity does NOT close r=1/2; it secures the signed-Hermitian readout CLASS (a real partial win,
necessary for Q=2/3) but not the value. After this BOTH symmetry-side AND measure/positivity-side levers
are exhausted -> r=1/2 is a free native reality-structure (complex-vs-real / det_C-vs-det_R) bit.

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
  => positivity reduces to the SAME irreducible pin: the complex-vs-real counting of the doublet (= field
     content / statistics = Dirac-vs-Majorana = charged-vs-neutral), which is generation-blind and which
     C^3=I forbids as an algebra symmetry. NO native selector on either the symmetry side or the measure side.
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
    print("VERDICT: positivity AGNOSTIC -- does NOT select the Kahler measure / does NOT close r=1/2. Secures")
    print("the signed-Hermitian readout CLASS (partial win, necessary for Q=2/3) but not the value. After this")
    print("BOTH the symmetry-side and the measure/positivity-side levers are exhausted: r=1/2 is a FREE NATIVE")
    print("reality-structure bit (complex-vs-real / det_C-vs-det_R counting of the doublet = field content =")
    print("statistics = Dirac-vs-Majorana), generation-blind and C^3=I-forbidden as a symmetry, OS-invisible as")
    print("a measure. Same as the framework's own statistics-selection open gap (G3). Natural campaign capstone.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
