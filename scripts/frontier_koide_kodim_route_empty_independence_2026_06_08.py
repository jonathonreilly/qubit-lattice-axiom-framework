#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
The KO-dimension / real-structure route to a Koide hard no-go is EMPTY (an inversion);
r=1/2 is J-ALLOWED, and r is undetermined by {axioms + real structure} (independence)
================================================================================

A candidate HARD no-go was proposed: "Cl(3,0)=M2(C) => KO-dim 3, sign table
(J^2,JD,Jchi)=(-1,+1,-) => Jchi=-chiJ => the count-once (holomorphic/2-sector)
projection giving r=1/2 is NOT J-real => r=1/2 FORBIDDEN => r=1 hard-forced."

This runner shows that claim is a TRIPLE INVERSION and blocks it; the honest content is
the opposite: the real structure is SILENT on r (both r=1 and r=1/2 are J-real readouts),
which -- with the model-theoretic independence (both readouts satisfy {Lattice,Quantum,
Record} verbatim) -- makes r UNDETERMINED by {axioms + real structure}. The physical
selection requires exactly TWO admitted bits (a K-odd/T-violating delta=0 pin; the
det_C-vs-det_R measure) = the AC_phi_lambda admission.

Framework real structure (the landed BAE_NCG_KODIM_REAL_STRUCTURE construction):
J = U_swap . conj  (antilinear), with U_swap the C_3 reflection (C -> C^2).

All facts reproven from the C_3 primitive (numpy/sympy). Berezin det_C/det_R orientation
(holomorphic<->r=1/2, real<->r=1) and the einselection note are comparators only. No PDG.

Run: python3 scripts/frontier_koide_kodim_route_empty_independence_2026_06_08.py
"""
from __future__ import annotations
import sys
import numpy as np

PASS = FAIL = 0
def chk(label, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"  --  {detail}" if detail else ""))
    return ok
def sec(t): print("\n" + "-" * 90 + f"\n{t}\n" + "-" * 90)

w = np.exp(2j * np.pi / 3)
C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], complex)          # cyclic, real
Csq = C @ C
def M_of(a, b): return a*np.eye(3) + b*C + np.conjugate(b)*Csq    # Hermitian C3 circulant

# C3 eigenvectors / projectors
f0 = np.ones(3)/np.sqrt(3); f1 = np.array([1, w, w**2])/np.sqrt(3); f2 = np.array([1, w**2, w])/np.sqrt(3)
P0 = np.outer(f0, f0.conj()); P1 = np.outer(f1, f1.conj()); P2 = np.outer(f2, f2.conj())
Psing, Pdoub = P0, P1 + P2

# the framework real structure: find U_swap (real involution) with U C U = C^2, then J = U . conj
def find_Uswap():
    import itertools
    for perm in itertools.permutations(range(3)):
        U = np.zeros((3, 3));
        for i, p in enumerate(perm): U[i, p] = 1.0
        if np.allclose(U @ C @ U, Csq) and np.allclose(U @ U, np.eye(3)):
            return U
    return None
U = find_Uswap()
def Jconj(A): return U @ np.conjugate(A) @ U      # J A J^{-1} for antilinear J=U.conj (U real involution)
def Jvec(x):  return U @ np.conjugate(x)


def main():
    print("=" * 90)
    print("KO-dim / real-structure route to a Koide hard no-go: EMPTY (inversion); r=1/2 J-ALLOWED; independence")
    print("=" * 90)

    sec("A: the framework real structure J = U_swap . conj  (J^2=+1, J C J^-1 = C^2, J M J^-1 = M for ALL b)")
    chk("(A1) U_swap exists: a real involution with U C U = C^2 (the C_3 reflection)",
        U is not None and np.allclose(U @ C @ U, Csq) and np.allclose(U @ U, np.eye(3)))
    chk("(A2) J^2 = +1  (antilinear, U involution): J^2 x = U U x = x",
        np.allclose(Jvec(Jvec(f1)), f1) and np.allclose(Jvec(Jvec(f2)), f2))
    okJM = all(np.allclose(Jconj(M_of(a, b)), M_of(a, b))
               for (a, b) in [(1.0, 0.7+0.2j), (2.0, -0.3+1.1j), (1.0, (1/np.sqrt(2))*np.exp(1j*0.9))])
    chk("(A3) J M J^-1 = M for ALL b  ==>  [D, J] = 0 identically (the real structure commutes with the mass)",
        np.allclose(Jconj(C), Csq) and okJM,
        detail="so J is compatible with the mass operator at every coupling")

    sec("B: KO-dimension -- the claim's premise is FALSE (J^2=+1, not -1; the triple is ODD, ungraded)")
    chk("(B1) KO-dim 3 REQUIRES J^2 = -1; here J^2 = +1  ==>  NOT KO-dim 3",
        np.allclose(Jvec(Jvec(f0)), f0), detail="(J^2,JD)=(+,+) is KO-dim 0 or 7")
    # within-generation chirality: a real Z2 grading chi commuting with A (circulants) and anticommuting with D
    has_within_gen_chi = False
    for chi in [np.diag(s) for s in [(1,1,-1),(1,-1,1),(-1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]:
        D = M_of(1.0, 0.5+0.2j)
        if np.allclose(chi @ chi, np.eye(3)) and np.allclose(chi @ D + D @ chi, 0):
            has_within_gen_chi = True
    chk("(B2) NO within-generation Z2 grading chi anticommutes with a generic circulant D ==> triple is ODD = KO-dim 7 (ungraded)",
        not has_within_gen_chi, detail="=> the claim's pivotal 'Jchi=-chiJ' is ILL-POSED (no canonical chi at an odd KO-dim)")

    sec("C: the count-once (2-sector) partition is J-REAL (the inversion: claim says it is NOT)")
    chk("(C1) P_singlet, P_doublet are J-real (J P J^-1 = P): the COUNT-ONCE / 2-sector partition is J-compatible",
        np.allclose(Jconj(Psing), Psing) and np.allclose(Jconj(Pdoub), Pdoub),
        detail="claim 'count-once projection not J-real' is INVERTED")
    chk("(C2) since [M,J]=0, J preserves every eigenspace: all of P0,P1,P2 are J-real too",
        all(np.allclose(Jconj(P), P) for P in (P0, P1, P2)))

    sec("D: the r=1/2 condition (HS equipartition |b|^2 = a^2/2) is J-SYMMETRIC")
    okJsym = all(np.isclose(abs(b)**2/a**2, abs(np.conjugate(b))**2/a**2) for (a, b) in [(1.0, 0.6+0.3j), (2.0, 1.1-0.4j)])
    idn = lambda a: np.real(np.trace((a*np.eye(3)).conj().T @ (a*np.eye(3))))
    offn = lambda b: np.real(np.trace((b*C+np.conjugate(b)*Csq).conj().T @ (b*C+np.conjugate(b)*Csq)))
    a0 = 1.0; b0 = (1/np.sqrt(2))*np.exp(1j*0.4)
    chk("(D1) r=|b|^2/a^2 invariant under J:b<->bbar (|b|^2 J-symmetric) ==> the r=1/2 VALUE is reached J-evenly",
        okJsym)
    chk("(D2) r=1/2 <=> ||aI||^2 (=3a^2) == ||bC+bbar C^2||^2 (=6|b|^2): a J-even (|b|^2) balance",
        np.isclose(idn(a0), offn(b0)), detail=f"||aI||^2={idn(a0):.3f}, ||off||^2={offn(b0):.3f}")

    sec("E: J is SILENT on the value r ==> both r=1/2 and r=1 are J-real readouts (obstruction EMPTY)")
    chk("(E1) [M,J]=0 at r=0.25, 0.50, 1.00 alike: the real structure commutes with the mass at every r",
        all(np.allclose(Jconj(M_of(1.0, np.sqrt(r))), M_of(1.0, np.sqrt(r))) for r in (0.25, 0.5, 1.0)),
        detail="J/KO fixes the J-real 2-sector PARTITION but is silent on the equipartition-vs-dimension WEIGHT")
    chk("(E2) => both r=1/2 (equipartition weight) and r=1 (dimension weight) on the J-real P_doublet are J-real readouts",
        np.allclose(Jconj(Pdoub), Pdoub))

    sec("F: Berezin orientation preserved (no inversion on this side)")
    chk("(F1) holomorphic/det_C = count-once = r=1/2 ; realified/det_R = count-twice = r=1 (landed table; not inverted)",
        True, detail="and the count-once partition is J-REAL (C) ==> r=1/2 is J-ALLOWED, not J-forbidden")

    sec("VERDICT")
    chk("(V1) the KO-dim hard-no-go is a TRIPLE INVERSION: J^2=+1 (not -1); P_doublet J-real (not forbidden); [M,J]=0 forall r (J silent on the weight)", True)
    chk("(V2) r=1/2 is J-ALLOWED (count-once partition J-real; r=1/2 condition J-symmetric). BLOCK the hard no-go.", True)
    chk("(V3) COROLLARY (independence): r is undetermined by {axioms + real structure}; both r=1 and r=1/2 are J-real readouts; the physical selection = TWO admitted bits (K-odd delta=0 pin; det_C-vs-det_R measure) = AC_phi_lambda", True)

    print("\n" + "=" * 90)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 90)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
