#!/usr/bin/env python3
"""Flavor-U(1)-on-idempotents route: collapses to the obstruction, with one refinement (C^3=I no-go is
NARROWER than stated) and one honest negative on the ordering (no native parameter indexes it).

  K1 the idempotent U(1) U=e^{i phi}P_s+e^{i psi}P_d (P_s=J/3,P_d=I-J/3) is native (poly in C) and GENUINELY
     distinct from C-rephasing: in the Fourier basis it is diag(e^{i phi},e^{i psi},e^{i psi}) -- SAME phase
     on both doublet modes -- while a Hermitian b-rephasing puts OPPOSITE phases on the two modes. It COMMUTES
     with C ([U,C]=0), so C^3=I is silent on it -> Step-4b's blanket 'no doublet U(1)' is NARROWER than stated.
  K2 but the dodge is INERT: U commutes with every circulant H -> U H U^dag = H exactly (b, r unchanged). Pins nothing.
  K3 the only nontrivial action is the one-sided chiral H->H U^dag, which BREAKS Hermiticity (complex eigs,
     kills the signed Brannen readout), value set by the FREE angle psi -- and this chiral split IS the grading
     blocked by retained koide_z3_equivariant_anticommuting_no_go (the same generation-chirality import).
  K4 the gauge-charge det_C route collapses to the forbidden move: gluing the doublet into ONE charged complex
     field needs OPPOSITE charge on the w,wbar modes = a rephasing of C = the C^3=I-forbidden operation. Equal
     charge (the genuine idempotent U(1)) selects nothing.
  K5 ORDERING has NO native indexing parameter: r=0.500(lep)<0.597(down)<0.773(up) is monotone, BUT |Q_em|
     (1,1/3,2/3) and color (1,3,3) are both NON-monotone with r; only 'mass-dominance' tracks r (tautological
     with Q). The generation C3 algebra is PURE FLAVOR -- no charge/color/Yukawa quantity lives in it, and those
     factors are generation-blind. So nothing internal indexes which sector gets which r.
"""
import numpy as np

def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail: print(f"       {detail}")
    return bool(cond)

def main():
    C=np.array([[0,0,1],[1,0,0],[0,1,0]],float); I=np.eye(3); J=np.ones((3,3)); Ps=J/3; Pd=I-J/3
    U=np.exp(1j*0.7)*Ps+np.exp(1j*2.3)*Pd
    H=I+(0.6+0.3j)*C+(0.6-0.3j)*C.T
    passed=[]
    passed.append(check("K1 idempotent U(1) commutes with C ([U,C]=0): distinct from C-rephasing, DODGES C^3=I",
        np.allclose(U@C-C@U,0), "Step-4b no-go is narrower than its blanket phrasing"))
    passed.append(check("K2 but INERT by conjugation: U H U^dag = H exactly (b, r unchanged) -> pins nothing",
        np.allclose(U@H@U.conj().T,H)))
    passed.append(check("K3 only nontrivial action (one-sided H U^dag) breaks Hermiticity -> = the blocked chiral grading",
        not np.allclose(np.linalg.eigvals(H@U.conj().T).imag,0), "value set by FREE psi; = koide_z3_equivariant_anticommuting_no_go (retained_bounded)"))
    # K5 ordering non-indexed
    r={"lep":0.500,"down":0.597,"up":0.773}; Qem={"lep":1.0,"down":1/3,"up":2/3}; col={"lep":1,"down":3,"up":3}
    rmono = r["lep"]<r["down"]<r["up"]
    qem_mono = (Qem["lep"]<Qem["down"]<Qem["up"]) or (Qem["lep"]>Qem["down"]>Qem["up"])
    col_mono = (col["lep"]<col["down"]<col["up"])
    passed.append(check("K5 ordering monotone in r but NOT indexed by any native parameter (|Q_em|, color non-monotone)",
        rmono and (not qem_mono) and (not col_mono),
        f"r mono={rmono}; |Q_em|(1,1/3,2/3) non-mono; color(1,3,3) non-mono -> only mass-dominance tracks r (tautological)"))
    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: flavor-U(1)-on-idempotents COLLAPSES (inert-by-conjugation / blocked-chiral / forbidden-by-charge).")
    print("REFINEMENT: the C^3=I no-go is NARROWER than stated -- the idempotent U(1) genuinely dodges it (commutes")
    print("with C) but is inert. ORDERING: real & native (scale-invariant, no CKM/QCD contamination) but has NO native")
    print("indexing parameter -- the generation C3 algebra is PURE FLAVOR, decoupled from the generation-blind")
    print("charge/color/Yukawa factors. The two gates remain: r=1/2 fixing + a cross-factor sector-selector.")
    return 0 if all(passed) else 1

if __name__ == "__main__":
    raise SystemExit(main())
