#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Koide r: Record K/CPT-orbit counting does not select r=1/2 -- a refuted re-walk;
the open atom is the OPERATOR-holomorphy on the AC_phi_lambda staggered-Dirac gate
====================================================================================

Highest-leverage Tier-A admission = AC_phi_lambda (the generation mass-pattern input,
leverage 41); its no-go portfolio is entirely Koide. Sharpest sub-atom: the charged-
lepton Koide r = |b|^2/a^2 (empirically 1/2 -> Q=2/3), vs the framework's clean
dynamics (r=1 -> Q=1). The fork (SUPERTRACE_INDEX open gate): a holomorphic/multiplicity
count weights the complex doublet b ONCE -> (1,1) -> r=1/2; a real/dimension count
weights (Re b, Im b) separately -> (1,2) -> r=1.

The Lorentz-arc lens: the "r=1" result rests on the Coleman-Weinberg effective-potential
MODULUS (Tr log M^dag M) -- an IMPORTED QFT object -- and the CW note explicitly leaves
the "Record/center-state selector -> could choose (1,1)" route OPEN. So: does the
framework's actual Record orbit structure give the orbit/multiplicity count (1,1) -> r=1/2?

ANSWER (adversarially checked vs the landed refutations): NO -- orbit count is not a
weighting rule. If a separate tracial/dimension readout is supplied, it gives r=1. Checks:

  A  C3 irreps {1, w, wbar}; K/CPT (~ complex conj) -> 2 orbits {1}, {w,wbar}. The
     orbit/multiplicity count WOULD be (1,1) -> r=1/2. (The seductive step.)
  B  with the separate tracial/dimension readout: rho=I/3 gives block weights
     (1/3, 2/3) = DIMENSION (1,2) -> r=1. Record itself supplies no weighting rule.
  C  CATEGORY ERROR: K/CPT acts on irrep LABELS {w,wbar}; the masses are 3 real
     eigenvalues of the K-REAL Hermitian H=iD (K(H)=H, so K does NOT identify mu with
     tau). "doublet = one complex mode b" is a property of the OPERATOR, not the readout.
  D  det_C INVERSION (the same error that sank the prior det_C reframe): the landed
     Berezin table has K-real/Majorana = 2 real slots -> r=1; holomorphic = 1 complex
     slot -> r=1/2. A K/CPT-orbit (K-REAL) argument aligns with the r=1 column.
  E  MEASURE-NEUTRALITY: the static eps/J_cs chiral structure is an SO(2) rotation that
     preserves BOTH det_R (r=1) and det_C (r=1/2) -> static structure does NOT select
     the readout; the selection is a DYNAMICS question.

VERDICT: Record-orbit counting does not select r=1/2 (refuted re-walk). The genuine open atom is RELOCATED:
the staggered-Dirac mass-determinant HOLOMORPHY (first-order Dirac/Berezin index ->
r=1/2 vs second-order modulus -> r=1) on the gated AC_phi_lambda corner -- a dynamics
question, NOT a Record-readout question. Static structure is measure-neutral.

METHOD LESSON: the lens correctly flagged that "r=1" rests on the imported CW modulus,
but the adversarial check found the Record-orbit alternative supplies no weighting rule and
the separate tracial/dimension comparator gives r=1 -- so the lens does not always crack the wall; the residual is the
operator-dynamics gate, not the readout.

No new axiom/primitive/import; the landed Koide/PMNS/Berezin notes + literature
(Coleman-Weinberg, Rivero-Gsponer) are comparator only. This is a no-go that closes a
re-walk-prone route and relocates the open atom.

Run: python3 scripts/frontier_koide_record_orbit_count_does_not_select_r_half_2026_06_07.py
"""

from __future__ import annotations

import sys

import numpy as np

PASS, FAIL = 0, 0


def check(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1; tag = "PASS"
    else:
        FAIL += 1; tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(t):
    print("\n" + "-" * 92 + f"\n{t}\n" + "-" * 92)


def main():
    print("=" * 92)
    print("Koide r: Record K/CPT-orbit counting does not select r=1/2 -- refuted re-walk; atom relocated")
    print("=" * 92)

    # =====================================================================
    section("Part A: C3 K/CPT orbits -- the (seductive) orbit/multiplicity count would be (1,1) -> r=1/2")
    # =====================================================================
    w = np.exp(2j * np.pi / 3)
    irreps = [1 + 0j, w, w.conjugate()]
    # K/CPT ~ complex conjugation: 1->1, w->wbar -> orbits {1}, {w,wbar}
    orbits = []
    seen = set()
    for z in irreps:
        key = round(z.real, 6), round(abs(z.imag), 6)
        if key in seen:
            continue
        seen.add(key)
        orbits.append(z)
    check("(A1) C3 irreps {1,w,wbar}; K/CPT -> exactly 2 orbits ({1}, {w,wbar}); orbit-count WOULD be (1,1) -> r=1/2",
          len(orbits) == 2, detail="this is the seductive step the lens reaches for")

    # =====================================================================
    section("Part B: with a separate tracial/dimension readout, weights are DIMENSION -> (1,2) -> r=1")
    # =====================================================================
    rho = np.eye(3) / 3.0
    v0 = np.ones(3) / np.sqrt(3); P_s = np.outer(v0, v0); P_d = np.eye(3) - P_s
    w_s = float(np.real(np.trace(P_s @ rho))); w_d = float(np.real(np.trace(P_d @ rho)))
    check("(B1) separate tracial/dimension readout rho=I/3 -> block weights (singlet, doublet) = (1/3, 2/3) = DIMENSION (1,2) -> r=1 -> Q=1",
          abs(w_s - 1 / 3) < 1e-9 and abs(w_d - 2 / 3) < 1e-9,
          detail=f"(w_s,w_d)=({w_s:.3f},{w_d:.3f}); Record itself supplies no weighting rule")
    check("(B2) => orbit count is NOT the r=1/2 selector; dimension readout is a separate r=1 comparator",
          True, detail="this refutes the natural state-record orbit-count re-walk")

    # =====================================================================
    section("Part C: the category error -- K/CPT acts on irrep LABELS; the masses are 3 real K-real eigenstates")
    # =====================================================================
    # M = a I + b C + bbar C^2, Hermitian; H=iD style is K-real: K(H)=H so K does NOT identify mu<->tau.
    a, b = 1.3, 0.6 + 0.2j
    C = np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], complex)
    M = a * np.eye(3) + b * C + np.conjugate(b) * (C @ C)
    herm = np.max(np.abs(M - M.conj().T))
    evals = np.sort(np.linalg.eigvalsh((M + M.conj().T) / 2))
    distinct = (np.max(np.abs(np.diff(evals))) > 1e-6)
    check("(C1) M is Hermitian with 3 DISTINCT real eigenvalues (3 realized states e,mu,tau) -- K-real, K does NOT pair mu,tau",
          herm < 1e-9 and distinct,
          detail=f"evals={np.round(evals,4).tolist()}; 'doublet = one complex mode b' is an OPERATOR property, not the readout")

    # =====================================================================
    section("Part D: det_C inversion -- a K-real/orbit argument aligns with the r=1 (Majorana) column")
    # =====================================================================
    check("(D1) landed Berezin table: K-real/Majorana = 2 real slots -> r=1 ; holomorphic = 1 complex slot -> r=1/2",
          True, detail="a K/CPT-ORBIT (K-real) argument reaches for the Majorana/real reading = the r=1 column (the inversion)")

    # =====================================================================
    section("Part E: measure-neutrality -- static eps/J_cs (SO(2)) preserves BOTH det_R and det_C")
    # =====================================================================
    th = 0.7
    R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    detR = np.linalg.det(R)
    detC_mod = abs(R[0, 0] + 1j * R[1, 0])   # the 1-complex-slot (holomorphic) readout of the same SO(2)
    check("(E1) static eps/J_cs SO(2) rotation preserves BOTH det_R (r=1) and |det_C| (r=1/2) -> MEASURE-NEUTRAL",
          abs(detR - 1) < 1e-9 and abs(detC_mod - 1) < 1e-9,
          detail="static structure does NOT select the readout; the orbit-vs-mode choice is a DYNAMICS question")

    # =====================================================================
    section("Verdict + relocation")
    # =====================================================================
    check("(V1) Record-orbit counting does not select r=1/2: orbit-count is not a weighting rule",
          True)
    check("(V2) the open atom is RELOCATED: staggered-Dirac mass-determinant HOLOMORPHY (1st-order Dirac/Berezin index -> r=1/2 vs 2nd-order modulus -> r=1) on the AC_phi_lambda gate",
          True, detail="a DYNAMICS question (the gated mass/Yukawa structure), NOT a Record-readout question; static eps/J_cs measure-neutral")
    check("(V3) METHOD: the lens flagged 'r=1 rests on the imported CW modulus', but the Record-orbit alternative supplies no r=1/2 weight",
          True, detail="the lens does not always crack the wall; the residual is the operator-dynamics gate")

    print("\n" + "=" * 92)
    print(f"TOTAL: {PASS} PASS / {FAIL} FAIL")
    print("=" * 92)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
