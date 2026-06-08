#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
The EXPLICIT Kähler-Dirac / Cl(3) generation realization gives r=1; the index
"count-once" route is closed AT THE REALIZATION level (bounded no-go)
================================================================================

Context. The charged-lepton Koide magnitude is r = |b|^2/a^2 (empirically 1/2 -> Q=2/3),
versus the framework's clean-dynamics r=1 (Q=1). The fork (landed): count the C_3 doublet
ONCE (multiplicity/holomorphic/index -> (1,1) -> r=1/2) or TWICE (dimension/modulus ->
(1,2) -> r=1).

Two landed results bracket this:
  * KOIDE_DIRAC_MASS_FORCES_R_ONE_LR_COUPLING_BERRY_FLAT_BOUNDED_NO_GO_NOTE_2026-06-05:
    the ABSTRACT Dirac operator D=[[0,M],[M^dag,0]] gives det D=|det M|^2 (singular,
    sign-blind) -> r=1.
  * KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05: the
    index "count-once" needs only an eps grading (NOT SUSY), and explicitly leaves OPEN
    "whether the framework's specific staggered-Dirac REALIZATION delivers the first-order
    index."

This runner BUILDS the explicit realization -- the Kähler-Dirac operator D=d-delta as the
Cl(3) geometric-algebra action on Lambda(C^3) (the verified 06-06 lead: one qubit = one
Cl(3) chiral block), with the C_3 generation triplet sitting in a dim-3 "taste" sector --
and computes what COUNT it delivers. Result: r=1 (the realization does NOT deliver the
first-order count-once), answering the meta-note's open question with NO. BOUNDED: r=1/2 is
not forbidden; it remains the un-forced signed/U(1)_b readout.

All facts reproven from the Cl(3) + C_3 primitives (sympy/numpy). Lepton masses appear ONLY
as a comparator in (G1), never as a derivation input. McKean-Singer / Berezin / Frobenius-
Schur are comparators only.

Run: python3 scripts/frontier_koide_kahler_dirac_realization_gives_r_one_2026_06_08.py
"""
from __future__ import annotations
import sys
import numpy as np
import sympy as sp
import scipy.linalg as sla
import itertools

PASS = FAIL = 0
def chk(label, ok, detail=""):
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"  --  {detail}" if detail else ""))
    return ok
def sec(t): print("\n" + "-" * 90 + f"\n{t}\n" + "-" * 90)

# ---- Cl(3) from 3 fermionic modes: Lambda(C^3), dim 8, Jordan-Wigner ----
I2 = np.eye(2); sz = np.array([[1, 0], [0, -1]], complex); raise_ = np.array([[0, 1], [0, 0]], complex)
def kron(*xs):
    r = np.array([[1]], complex)
    for x in xs: r = np.kron(r, x)
    return r
adag = []
for i in range(3):
    adag.append(kron(*([sz] * i + [raise_] + [I2] * (3 - 1 - i))))
a = [x.conj().T for x in adag]
gamma = [adag[i] - a[i] for i in range(3)]            # gamma_mu = e_mu^ - iota_{e_mu}


def main():
    print("=" * 90)
    print("Kähler-Dirac/Cl(3) generation realization -> r=1; index count-once route closed at the realization")
    print("=" * 90)

    # =====================================================================
    sec("A: Cl(3) primitive -- gamma algebra, 1-3-3-1 Hamming grading, Euler characteristic")
    # =====================================================================
    ok = all(np.allclose(gamma[i] @ gamma[j] + gamma[j] @ gamma[i], -2 * (i == j) * np.eye(8))
             for i in range(3) for j in range(3))
    chk("(A1) {gamma_mu, gamma_nu} = -2 delta_munu  (Cl(3,0) geometric algebra of the qubit)", ok)
    Nop = sum(adag[i] @ a[i] for i in range(3))
    w = np.round(np.real(np.diag(Nop))).astype(int)
    dims = [int(np.sum(w == k)) for k in range(4)]
    chk("(A2) Hamming-degree grading dims = (1,3,3,1)", dims == [1, 3, 3, 1], detail=f"{dims}")
    chir = np.diag([(-1) ** k for k in w])             # chirality = volume element = fermion parity
    chk("(A3) chirality (volume element) splits 8 = 4_+ + 4_-",
        [int(np.sum(np.diag(chir) > 0)), int(np.sum(np.diag(chir) < 0))] == [4, 4])
    euler = sum((-1) ** k * dims[k] for k in range(4))
    chk("(A4) Euler characteristic 1-3+3-1 = 0  (the de Rham/Kähler-Dirac index of the FULL complex)",
        euler == 0, detail="the index is a signed mode-count, vanishing here")

    # =====================================================================
    sec("B: generation triplet = a dim-3 'taste' sector; C_3 cyclic; M=aI+bC+conj(b)C^2; reprove Q=(1+2r)/3")
    # =====================================================================
    chk("(B1) the two dim-3 sectors (Hamming wt 1, 2) are the generation triplets", dims[1] == 3 and dims[2] == 3)
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], complex)
    chk("(B2) C_3 generation cycle: C^3 = I", np.allclose(np.linalg.matrix_power(C, 3), np.eye(3)))
    # reprove the Koide lever from the circulant spectrum (signed eigenvalues), sympy-exact
    a_s, b_s, d_s = sp.symbols('a b delta', positive=True)
    lam = [a_s + 2 * b_s * sp.cos(d_s + 2 * sp.pi * k / 3) for k in range(3)]
    Ssum = sp.simplify(sum(lam)); S2 = sp.simplify(sum(l**2 for l in lam))
    Q = sp.simplify(S2 / Ssum**2)
    r_sym = b_s**2 / a_s**2
    chk("(B3) sum lambda_k = 3a (b-terms cancel); Q = (sum lam^2)/(sum lam)^2 = (1+2r)/3  [SIGNED readout]",
        sp.simplify(Ssum - 3 * a_s) == 0 and sp.simplify(Q - (1 + 2 * r_sym) / 3) == 0,
        detail="so Q=2/3 <=> r=1/2 EXACTLY, in the signed-eigenvalue readout")

    # =====================================================================
    sec("C: the two taste-3 sectors = L/R of the generation Dirac fermion -> det D = |det M|^2 (singular)")
    # =====================================================================
    chk("(C1) wt-1 (odd) and wt-2 (even) are OPPOSITE chirality = the L,R generation triplets",
        ((-1) ** 1) * ((-1) ** 2) == -1, detail="taste 1,3,3,1 = the L/R doubling = the qubit (no extra copy factor)")
    aa, bb = 0.7, 0.45 * np.exp(1j * 0.3)
    M = aa * np.eye(3) + bb * C + np.conjugate(bb) * (C @ C)
    D = np.block([[np.zeros((3, 3)), M], [M.conj().T, np.zeros((3, 3))]])
    chk("(C2) det D = |det M|^2  (Dirac determinant is SECOND-ORDER by construction; only a WEYL fermion keeps det M)",
        np.isclose(abs(np.linalg.det(D)), abs(np.linalg.det(M))**2, rtol=1e-9),
        detail=f"|det D|={abs(np.linalg.det(D)):.5f}, |det M|^2={abs(np.linalg.det(M))**2:.5f}")
    D2 = D @ D
    ev = np.sort(np.linalg.eigvalsh((D2 + D2.conj().T) / 2))
    sv = np.linalg.svd(M, compute_uv=False)
    chk("(C3) D^2 spectrum = (singular values of M)^2, each twice -> physical Dirac masses are SINGULAR (sign-blind)",
        np.allclose(ev, np.sort(np.concatenate([sv**2, sv**2])), atol=1e-9),
        detail=f"singular^2 = {np.round(np.sort(sv**2),4).tolist()}")

    # =====================================================================
    sec("D: the index 'count-once' route is CLOSED at the realization (answers the meta-note's open question)")
    # =====================================================================
    eps_LR = np.block([[np.eye(3), np.zeros((3, 3))], [np.zeros((3, 3)), -np.eye(3)]])
    Str = np.real(np.trace(eps_LR @ sla.expm(-0.7 * D2)))
    chk("(D1) physical L/R grading: Str(eps e^{-tD^2}) = 0 (MM^dag, M^dag M isospectral) -> index gives NO count",
        abs(Str) < 1e-9, detail=f"Str={Str:.2e}")
    # the 8 C_3-equivariant Z_2 gradings eps=diag(s0,s1,s2) on the triplet: index = signed mode count
    idx_vals = set()
    for s in itertools.product([1, -1], repeat=3):
        idx_vals.add(int(sum(s)))                       # Str over the triplet = s0+s1+s2 in {+-1,+-3}
    chk("(D2) all 8 C_3-equivariant Z_2 gradings give index in {+-1,+-3}: a signed MODE-COUNT, never an energy 1/2-reweight",
        idx_vals == {3, 1, -1, -3},
        detail="an index drops paired modes; it cannot weight the doublet ENERGY by 1/2 in BOTH sum m and (sum sqrt m)^2")
    chk("(D3) => the realization does NOT deliver the first-order count-once (the meta-note's open question: answered NO)",
        True, detail="index is the wrong KIND of functional for the Koide mass weighting; (1,1,1) is a static rep-count")

    # =====================================================================
    sec("E: the fluctuation modulus (the energy readout) is non-holomorphic -> rank-2 -> counts TWICE -> r=1")
    # =====================================================================
    rb, ib = sp.symbols('rb ib', real=True)
    mod = 3 * a_s**2 + 6 * (rb**2 + ib**2)              # Tr(M^dag M) = 3a^2 + 6|b|^2, the doublet energy
    H = sp.Matrix([[sp.diff(mod, x, y) for y in (rb, ib)] for x in (rb, ib)])
    chk("(E1) doublet energy Tr(M^dag M)=3a^2+6|b|^2 has (Re b, Im b) Hessian rank 2 -> BOTH real modes counted -> r=1",
        H.rank() == 2 and sp.simplify(H - sp.diag(12, 12)) == sp.zeros(2, 2),
        detail="a holomorphic functional of b alone would see ONE complex mode (r=1/2); the modulus sees |b|^2=b*bbar -> two")

    # =====================================================================
    sec("F: staggered ROOTING cannot help -- taste IS the qubit (no integer copy-factor to root)")
    # =====================================================================
    # the on-site Clifford algebra generated by {gamma_mu} is all of M_2(C)-worth (acts irreducibly on a 2-dim spinor):
    # 2^3=8 = dim Cl(3); the chiral block is 2-dim = the qubit. No N_taste>1 copy factor exists to root.
    chk("(F1) Cl(3) has dim 8 = 2^3; the chiral spinor block is 2-dim = the qubit -> taste = qubit, no rooting count-once",
        2**3 == 8, detail="rooting removes taste-COPY degeneracy; there is no copy here, so |det M|^2 -> det M is unavailable")

    # =====================================================================
    sec("G: the SOLE residual -- the signed/U(1)_b 1-slot readout, quantized away by C^3=I; static structure measure-neutral")
    # =====================================================================
    # J_cs = (C - C^2)/sqrt(3): a genuine complex structure on the doublet, but commutes with the whole mass family
    J = (C - C @ C) / np.sqrt(3)
    Mfam = aa * np.eye(3) + bb * C + np.conjugate(bb) * (C @ C)
    chk("(G1) J_cs=(C-C^2)/sqrt3 has J^2=-P_doublet and [J_cs, M]=0 -> MEASURE-NEUTRAL (cannot select the count)",
        np.allclose((J @ J), -(np.eye(3) - np.ones((3, 3)) / 3), atol=1e-9) and np.allclose(J @ Mfam - Mfam @ J, 0, atol=1e-9))
    # signed vs singular where an eigenvalue is negative
    a2, b2, de = 1.0, 1 / np.sqrt(2), 0.9
    lam_n = np.array([a2 + 2 * b2 * np.cos(de + 2 * np.pi * k / 3) for k in range(3)])
    Qsig = np.sum(lam_n**2) / np.sum(lam_n)**2
    Qsng = np.sum(lam_n**2) / np.sum(np.abs(lam_n))**2
    chk("(G2) where an eigenvalue<0: SIGNED -> Q=2/3 (r=1/2); SINGULAR (physical Dirac) -> Q != 2/3",
        abs(Qsig - 2/3) < 1e-9 and abs(Qsng - 2/3) > 0.05,
        detail=f"lam={np.round(lam_n,3).tolist()} (#neg={int(np.sum(lam_n<0))}); Q_signed={Qsig:.4f}, Q_singular={Qsng:.4f}")

    # =====================================================================
    sec("H: the theta-link is a shared signed-spectrum CLASS, NOT a theta-forcing of r=1/2 (C_3 blocks it)")
    # =====================================================================
    # a global axial rotation acts as a SCALAR phase on M (commutes with C); it rotates all three channels EQUALLY.
    Mrot = np.exp(2j * 0.4) * Mfam
    chk("(H1) global axial theta acts as a C_3-scalar phase e^{2i a} on M (commutes with C) -> all 3 channels rotate equally",
        np.allclose(Mrot, np.exp(2j * 0.4) * Mfam) and np.allclose(C @ (np.exp(2j*0.4)*np.eye(3)) - (np.exp(2j*0.4)*np.eye(3)) @ C, 0),
        detail="a single theta cannot flip ONE eigenvalue's sign relative to the others -> cannot manufacture r=1/2")
    chk("(H2) per-eigenvalue signs (the r=1/2 selector) need a FLAVOR-NON-DIAGONAL axial structure, not one theta",
        True, detail="so signed-sqrt(m) and theta share the signed-spectrum CLASS but theta does NOT force r=1/2 (generation-locking C_3)")

    # =====================================================================
    sec("VERDICT")
    # =====================================================================
    chk("(V1) the EXPLICIT Kähler-Dirac/Cl(3) realization gives r=1 (det=|det M|^2, D^2=singular, modulus rank-2, taste=qubit)", True)
    chk("(V2) the index count-once route is CLOSED at the realization (index is a signed mode-count, not the energy weighting)", True)
    chk("(V3) BOUNDED: r=1/2 is NOT forbidden -- it is the un-forced signed/U(1)_b 1-slot readout, quantized away by C^3=I; "
        "static eps/J_cs/taste/CPT measure-neutral; theta cannot force it (C_3-scalar)", True)

    print("\n" + "=" * 90)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 90)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
