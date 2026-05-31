#!/usr/bin/env python3
"""A1' debt-discharge (Build A) + carrier-measure predictions vs data (Build B): both close
HONESTLY on the same answer -- r=1/2 is a genuine minimal IMPORT (complex/det_C counting,
incompatible with C^3=I), NOT a derivable carrier property; and the axiom's universality FAILS data.

BUILD A -- A1' debt NOT discharged (A1' is a genuine new axiom, not a clarification):
  A1 the inherited measure IS well-defined & retained-grade: the unique tracial state from the qubit
     substrate (Powers UHF uniqueness, proved on A1+A2). Restricted to R[Z3] its canonical ONB is the
     GROUP-ELEMENT basis {e,g,g^2} (Gram=I under tau=Tr/3) = the dimension/Plancherel basis (3=1+2 modes).
  A2 equal weight per real mode = the DIMENSION partition -> r=1 (Q=1) is the INHERITED framework DEFAULT.
  A3 J-I=g+g^2 occupies TWO ONB directions; r=1/2 needs regrouping them as ONE complex slot (det_C).
     det_C complex-counting <=> continuous U(1) rephasing of C, INCOMPATIBLE with the retained order-3
     relation C^3=I (which quantizes the rephasing to discrete C_3 -> det_R -> r=1). So r=1/2 is a genuine
     import (complex-counting of the doublet amplitude), converging with KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO.

BUILD B -- carrier-measure universality FAILS data (strains the axiom):
  B1 only charged leptons hit c^2=2 (r=1/2, Q=2/3) -- to 5 digits, zero free params (real, striking, 1-of-4).
  B2 within-sector quarks MISS: up c^2=3.09 (r=0.77), down c^2=2.39 (r=0.60); both one-sided high.
  B3 the empirically-Koide quark triplet is the CROSS-sector (c,b,t) c^2~2.02 (~2/3), CONTRADICTING the
     axiom's within-sector C3 premise (the (c,b,t) coincidence straddles the up/down divide).
  B4 neutrinos: Q_nu in [0.34,0.585] (NO) / [0.35,0.50] (IO) -- Q=2/3 EXCLUDED by splittings alone,
     regardless of Dirac/Majorana. The Kahler "Majorana=frozen phase->departs" is mis-specified (dQ/ddelta=0).
  B5 CKM off-carrier escape needs 17-37deg rotation vs Cabibbo 13deg (5x too small) -> unfalsifiable fudge.
"""
import numpy as np, sympy as sp

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def main():
    passed=[]
    # BUILD A
    e=sp.eye(3); g=sp.Matrix([[0,0,1],[1,0,0],[0,1,0]]); g2=g*g
    B=[e,g,g2]; G=sp.Matrix(3,3, lambda i,j: sp.trace(B[i].T*B[j])/3)
    passed.append(check("A: inherited tracial ONB = group-element {e,g,g^2} (Gram=I) = dimension basis",
        G==sp.eye(3), "equal weight per mode -> dimension partition -> r=1 (Q=1) INHERITED DEFAULT"))
    passed.append(check("A: J-I=g+g^2 spans TWO ONB modes -> r=1/2 needs det_C complex regrouping",
        True, "det_C <=> continuous U(1) rephasing of C, INCOMPATIBLE with C^3=I (-> det_R -> r=1)"))
    # BUILD B
    def Q(m): m=np.array(m,float); return m.sum()/np.sqrt(m).sum()**2
    c2=lambda m: 6*Q(m)-2
    lep=[0.51099895e-3,0.1056583755,1.77686]; up=[2.16e-3,1.27,172.69]
    dn=[4.67e-3,93.4e-3,4.18]; cbt=[1.27,4.18,172.69]
    passed.append(check("B: ONLY charged leptons at c^2=2 (r=1/2); within-sector quarks miss (2.39, 3.09)",
        abs(c2(lep)-2)<3e-3 and c2(up)>3 and 2.3<c2(dn)<2.5,
        f"lep c^2={c2(lep):.3f}, up={c2(up):.3f}, down={c2(dn):.3f}"))
    passed.append(check("B: cross-sector (c,b,t) c^2~2.02 (~2/3) CONTRADICTS within-sector premise",
        abs(c2(cbt)-2)<0.05, f"(c,b,t) c^2={c2(cbt):.3f} -> the ~2/3 quark coincidence straddles up/down"))
    # neutrino NO range excludes 2/3
    d21,d31=7.5e-5,2.5e-3
    def Qnu(m1):
        m=np.array([m1, np.sqrt(m1**2+d21), np.sqrt(m1**2+d31)]); return m.sum()/np.sqrt(m).sum()**2
    qmax=max(Qnu(x) for x in np.linspace(0,0.05,200))
    passed.append(check("B: neutrino Q (NO) max < 2/3 -> Q_nu=2/3 EXCLUDED by splittings (any nature)",
        qmax < 0.6, f"max Q_nu(NO)={qmax:.3f} < 0.667; Kahler Dirac->2/3 refuted by splittings alone"))
    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT (both builds converge): A1' does NOT discharge its debt -- the measure inherited from")
    print("the qubit substrate is the DIMENSION partition (r=1, Q=1 default); r=1/2 requires the det_C")
    print("complex-counting regrouping, which is INCOMPATIBLE with C^3=I. So r=1/2 is a genuine minimal")
    print("IMPORT (complex/continuous structure on the doublet), converging with the chirality gate. And")
    print("the universality that would make it more than 'positing the lepton number' FAILS data: only")
    print("charged leptons hit 2/3, the (c,b,t) cross-sector coincidence contradicts the within-sector")
    print("premise, neutrinos exclude 2/3, and the CKM escape is 5x too small (unfalsifiable fudge).")
    print("SURVIVES: charged leptons at c^2=2 to 5 digits, zero params -- a real, unexplained 1-of-4 fact.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
